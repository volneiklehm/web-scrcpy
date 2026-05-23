from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit, send
from scrcpy import Scrcpy
import argparse
import queue

scpy_ctx = None
client_sid = None
message_queue = queue.Queue()
audio_message_queue = queue.Queue()
video_bit_rate = "1024000"
new_display = None

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode=None)

@app.route('/')
def index():
    return render_template('index.html')

def video_send_task(sid):
    while client_sid == sid:
        try:
            message = message_queue.get(timeout=0.01)
            socketio.emit('video_data', message, to=sid)
        except queue.Empty:
            pass
        except Exception as e:
            print(f"Error sending video data: {e}")
        finally:
            socketio.sleep(0.001)
    print(f"video_send_task stopped")

def audio_send_task(sid):
    while client_sid == sid:
        try:
            message = audio_message_queue.get(timeout=0.01)
            socketio.emit('audio_data', message, to=sid)
        except queue.Empty:
            pass
        except Exception as e:
            print(f"Error sending audio data: {e}")
        finally:
            socketio.sleep(0.001)
    print(f"audio_send_task stopped")

def send_video_data(data):
    message_queue.put(data)

def send_audio_data(data):
    audio_message_queue.put(data)

@socketio.on('connect')
def handle_connect():
    global scpy_ctx, client_sid
    print('Client connected')

    if scpy_ctx is not None:
        print(f'reject connection, client {scpy_ctx} is already connected')
        return False
    else:
        client_sid = request.sid
        scpy_ctx = Scrcpy()
        scpy_ctx.scrcpy_start(send_video_data, send_audio_data, video_bit_rate, new_display)
        socketio.start_background_task(video_send_task, client_sid)
        socketio.start_background_task(audio_send_task, client_sid)
        print(f'connectioned, client  {scpy_ctx}')

@socketio.on('disconnect')
def handle_disconnect(reason=None):
    global scpy_ctx, client_sid
    client_sid = None
    print('Client disconnected', {scpy_ctx})
    try:
        scpy_ctx.scrcpy_stop()
    except Exception as e:
        print(f'scrcpy_stop error: {e}')
    finally:
        scpy_ctx = None
        with message_queue.mutex:
            message_queue.queue.clear()
        with audio_message_queue.mutex:
            audio_message_queue.queue.clear()
    print('scrcpy stopped')

@socketio.on('control_data')
def handle_control_data(data):
    global scpy_ctx
    if scpy_ctx is not None:
        scpy_ctx.scrcpy_send_control(data)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Web server for scrcpy')
    parser.add_argument('--video_bit_rate', default="1024000", help='scrcpy video bit rate')
    parser.add_argument('--new-display', nargs='?', const='', default=None, metavar='WxH[/DPI]',
                        help='create a virtual display (e.g. 1920x1080/284, 1920x1080, /284, or empty for auto)')
    args = parser.parse_args()
    video_bit_rate = args.video_bit_rate
    new_display = args.new_display
    socketio.run(app, host='0.0.0.0', port=5000, allow_unsafe_werkzeug=True)
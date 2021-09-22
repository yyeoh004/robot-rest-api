from flask import Flask, request
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app, always_connect=True)

"""Message to Output"""
status = {
    "status": -1,
    "text": "Invalid status value"
}

@app.route('/')
def index():
   return "Go to /api/robot/status to retrieve data."

@app.route('/api/robot/status')
def get_status():
    print(status["status"])
    if status["status"] == -1:
        return {"message": status["text"]}, 400
    else:
        return status

"""Standard Event Handlers for Socket IO."""
@socketio.on("connect")
def connect():
    print("[INFO] Client connected: {}".format(request.sid))

@socketio.on("disconnect")
def disconnect():
    print("[INFO] Client disconnected: {}".format(request.sid))

@socketio.on("status")
def handle_message(msg):
    global status 
    status = msg

if __name__ == "__main__":
   socketio.run(app=app, host='0.0.0.0', port=7201)
from os import stat
import rospy
from actionlib_msgs.msg import GoalStatusArray
from flask import Flask


app = Flask(__name__)

class StatusSubscriber():
    def __init__(self):
        # Default message
        self.status = {
            "status": -1,
            "text": "Invalid status value"
        }
        rospy.Subscriber("/move_base/status", GoalStatusArray, self.status_cb)

    def status_cb(self, data):
        try:
            self.status = {
                    "status": data.status_list[0].status,
                    "text": data.status_list[0].text
                }
        except IndexError:
            self.status = {
                    "status": -1,
                    "text": "Invalid status value"
                }


if __name__ == "__main__":
    rospy.init_node("status_listener")
    status_subscriber = StatusSubscriber()
    
    @app.route('/')
    def index():
        return "Go to /api/robot/status to retrieve data."

    @app.route('/api/robot/status')
    def get_status():
        if status_subscriber.status["status"] == -1:
            return {"message": status_subscriber.status["text"]}, 400
        else:
            return status_subscriber.status
    
    app.run(host='0.0.0.0', port=7201, debug=True)
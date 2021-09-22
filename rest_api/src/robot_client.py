#!/usr/bin/env python3

import rospy
import socketio
from actionlib_msgs.msg import GoalStatusArray

server_address = "http://localhost:7201"

class RobotClient():
    def __init__(self):
        self.initialize_client()
        rospy.Subscriber("/move_base/status", GoalStatusArray, self.status_cb)
    
    def initialize_client(self):
        self.sio = socketio.Client()
        
        """Standard Event Handlers for Socket IO."""
        @self.sio.event
        def connect():
            print("[INFO] Connected to server.")

        @self.sio.event
        def connect_error(err):
            print("[INFO] Failed to connect to server.")

        @self.sio.event
        def disconnect():
            print("[INFO] Disconnected from server.")
            
        # Connect to server
        self.sio.connect(
            server_address
        )

        # Allows time for all connection to be done
        rospy.sleep(1)

    def status_cb(self, data):
        try:
            status = data.status_list[0].status
            text = data.status_list[0].text
            message = {
                    "status": status,
                    "text": text
                }
        except IndexError:
            message = {
                    "status": -1,
                    "text": "Invalid status value"
                }
        self.sio.emit("status", message)

if __name__ == "__main__":
    rospy.init_node("status_listener")
    robot = RobotClient()
    
    def shutdown():
        """
        Handler when shutdown signal is received. Stops all functions for graceful exit.
        """
        # Disconnect from socket io
        robot.sio.disconnect()

    rospy.on_shutdown(shutdown)
    rospy.spin()
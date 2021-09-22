# robot-rest-api
Cognicept Robotics Applications Engineer Assignment

## Installing python packages via pip
```
pip3 install flask
pip3 install flask-socketio
pip3 install python-socketio
pip3 install requests
```

## Running turtlebot simulation
```
roslaunch turtlebot3_gazebo turtlebot3_world.launch
roslaunch turtlebot3_navigation turtlebot3_navigation.launch
```
## Running REST API
### Framework 1:
GET Request --> Flask Server (Socket IO Server) <--> (via Socket IO) <--> Socket IO Client (Robot) <--> ROS
```
python3.6 rest_api/src/application_socketio.py
python3.6 rest_api/src/rest_poller.py
rosrun rest_api robot_client.py
```
### Framework 2:
GET Request --> Flask Server (Hosted on Robot) <--> ROS
```
rosrun rest_api application.py
```

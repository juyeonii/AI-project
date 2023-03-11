import os, sys

os.system('scp -P 22 etc@192.168.0.89:/home/etc/section.txt /home')
f = open('section.txt','r')
nlp = f.readline()

if nlp = 1:
    os.system('ros2 action send_goal /navigate_to_pose nav2_msgs/action/NavigateToPose "pose: {header: {frame_id: map}, pose: {position: {x: 1.9, y: 0.8, z: 0.0}, orientation:{x: 0.0, y: 0.0, z: 1.0, w: 1.0000000}}}"')
    os.system('sleep 20s')

elif nlp = 2:
    os.system('ros2 action send_goal /navigate_to_pose nav2_msgs/action/NavigateToPose "pose: {header: {frame_id: map}, pose: {position: {x: 0.0, y: 0.8, z: 0.0}, orientation:{x: 0.0, y: 0.0, z: 0.0, w: 1.0000000}}}"')
    os.system('sleep 20s')
    

elif nlp = 3:
    os.system('ros2 action send_goal /navigate_to_pose nav2_msgs/action/NavigateToPose "pose: {header: {frame_id: map}, pose: {position: {x: 1.9, y: 0.0, z: 0.0}, orientation:{x: 0.0, y: 0.0, z: 1.0, w: 1.0000000}}}"')
    os.system('sleep 20s')
            
os.system('ros2 action send_goal /navigate_to_pose nav2_msgs/action/NavigateToPose "pose: {header: {frame_id: map}, pose: {position: {x: 0.0, y: 0.0, z: 0.0}, orientation:{x: 0.0, y: 0.0, z: 0.0, w: 1.0000000}}}"')











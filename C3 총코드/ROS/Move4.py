import os, sys

os.system('ros2 action send_goal /navigate_to_pose nav2_msgs/action/NavigateToPose "pose: {header: {frame_id: map}, pose: {position: {x: 0.0, y: 0.0, z: 0.0}, orientation:{x: 0.0, y: 0.0, z: 0.0, w: 1.0000000}}}"')
print('4구역으로 이동 중')

os.system('scp -P 22 etc@192.168.0.89:/home/etc/pm/pm.txt /home/c3')
f = open('pm.txt','r')
pm10 = f.readline()
    
while int(pm10) > 40:
    os.system('scp -P 22 etc@192.168.0.89:/home/etc/pm/pm.txt /home/c3')
    f = open('pm.txt','r')
    pm10 = f.readline()
    print('미세먼지 측정 중')
    

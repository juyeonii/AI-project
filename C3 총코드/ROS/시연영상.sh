#bin/bash

ros2 action send_goal /navigate_to_pose nav2_msgs/action/NavigateToPose "pose: {header: {frame_id: map}, pose: {position: {x: 1.9, y: 0.0, z: 0.0}, orientation:{x: 0.0, y: 0.0, z: 1.0, w: 1.0000000}}}"

ros2 action send_goal /navigate_to_pose nav2_msgs/action/NavigateToPose "pose: {header: {frame_id: map}, pose: {position: {x: 1.9, y: 0.8, z: 0.0}, orientation:{x: 0.0, y: 0.0, z: 1.0, w: 1.0000000}}}"



ros2 action send_goal /navigate_to_pose nav2_msgs/action/NavigateToPose "pose: {header: {frame_id: map}, pose: {position: {x: 0.0, y: 0.0, z: 0.0}, orientation:{x: 0.0, y: 0.0, z: 0.0, w: 1.0000000}}}"

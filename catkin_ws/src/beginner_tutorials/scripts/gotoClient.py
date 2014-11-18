#! /usr/bin/env python

import roslib; roslib.load_manifest('beginner_tutorials')
import rospy
import actionlib
from beginner_tutorials.msg import *
from move_base_msgs.msg import *
from geometry_msgs.msg import PoseStamped
from tf.transformations import euler_from_quaternion, quaternion_from_euler




def goto(x, y, yaw = 0, frame = "/map"):
    client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
    client.wait_for_server()

    goal = MoveBaseGoal()
    # Fill in the goal here
    ps = PoseStamped()
    ps.header.frame_id = frame
    ps.header.stamp = rospy.Time.now()
    ps.pose.position.x = x
    ps.pose.position.y = y
    ps.pose.position.z = 0

    q = quaternion_from_euler(0, 0, yaw, 'sxyz')
    ps.pose.orientation.x = q[0]
    ps.pose.orientation.y = q[1]
    ps.pose.orientation.z = q[2]
    ps.pose.orientation.w = q[3]
    goal.target_pose = ps
    client.send_goal(goal)
    client.wait_for_result(rospy.Duration.from_sec(5.0))




if __name__ == '__main__':
    rospy.init_node('goto_Client')
    goto(0, 0)

#! /usr/bin/env python

import roslib; roslib.load_manifest('beginner_tutorials')
import rospy
import actionlib
from beginner_tutorials.msg import *
from move_base_msgs.msg import *
from geometry_msgs.msg import PoseStamped
from tf.transformations import euler_from_quaternion, quaternion_from_euler


from visualization_msgs.msg import *
from interactive_markers.interactive_marker_server import *

from gotoClient import goto



def processFeedback(feedback):
    p = feedback.pose.position
    #print feedback.marker_name + " is now at " + str(p.x) + ", " + str(p.y) + ", " + str(p.z)
    if(feedback.event_type == InteractiveMarkerFeedback.MOUSE_DOWN):
        print feedback.marker_name, " click"
        goto(p.x,p.y)

def makeMarker(server,x,y,des,yaw = 0):


    # create an interactive marker for our server
    int_marker = InteractiveMarker()
    int_marker.header.frame_id = "/map"
    int_marker.name = des
    int_marker.description = des

    int_marker.pose.position.x = x
    int_marker.pose.position.y = y

    # create a grey box marker
    box_marker = Marker()
    box_marker.type = Marker.SPHERE
    box_marker.scale.x = 1.5
    box_marker.scale.y = 1.5
    box_marker.scale.z = 1.5
    box_marker.color.r = 1
    box_marker.color.g = 1
    box_marker.color.b = 1
    box_marker.color.a = .5


    # create a control which will move the box
    # this control does not contain any markers,
    # which will cause RViz to insert two arrows
    button_control = InteractiveMarkerControl()
    button_control.always_visible = True
    button_control.name = des + "_button"
    button_control.interaction_mode = InteractiveMarkerControl.BUTTON

    button_control.markers.append(box_marker)

    # add the control to the interactive marker
    int_marker.controls.append(button_control)

    # add the interactive marker to our collection &
    # tell the server to call processFeedback() when feedback arrives for it
    server.insert(int_marker, processFeedback)

    # 'commit' changes and send to all clients

    server.applyChanges()

if __name__=="__main__":
    rospy.init_node("simple_marker")
    
    # create an interactive marker server on the topic namespace simple_marker
    server = InteractiveMarkerServer("simple_marker")

    f = open('../Marker_Location.txt','r')
    for line in f:
        arr = line.split()
        makeMarker(server,float(arr[0]),float(arr[1]),arr[2])

    while(raw_input('would you like to add more markers to the map?(y/n)') == 'y'):
        x = raw_input('please enter x ')
        y = raw_input('please enter y ')
        des = raw_input('please enter name ')
        yaw = raw_input('please enter angle ')

        makeMarker(server,float(x), float(y), des, yaw)

    rospy.spin()
    

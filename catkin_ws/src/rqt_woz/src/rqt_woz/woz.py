#!/usr/bin/env python

import roslib
roslib.load_manifest('rospy')
roslib.load_manifest('visualization_msgs')
from visualization_msgs.msg import Marker
from geometry_msgs.msg import Quaternion, Pose, Point, Vector3, Twist
import rospy
from qt_gui.plugin import Plugin
from python_qt_binding import QtGui,QtCore
from python_qt_binding.QtGui import QWidget, QFrame
from python_qt_binding.QtGui import QGroupBox
from python_qt_binding.QtCore import QSignalMapper, qWarning, Signal
import os
import time
import math
from 


class WoZPlugin(Plugin):
    def __init__(self, context):
        super(WoZPlugin, self).__init__(context)
        self._widget = QWidget()
        self._widget.setFixedSize(600, 600)
        QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))
        
        large_box = QtGui.QVBoxLayout()

        #Button for outreaching to recieve book from Human
        button_box = QtGui.QVBoxLayout()
        box_1 = QtGui.QHBoxLayout()
        box_2 = QtGui.QHBoxLayout()
        box_3 = QtGui.QHBoxLayout()
        box_4 = QtGui.QHBoxLayout()
        box_5 = QtGui.QHBoxLayout()
        box_6 = QtGui.QHBoxLayout()
        box_7 = QtGui.QHBoxLayout()
        box_8 = QtGui.QHBoxLayout()
        box_9 = QtGui.QHBoxLayout()
        box_10 = QtGui.QHBoxLayout()

        box_1.addWidget(self.create_button('print nice', self.printCallback))

        self._widget.setObjectName('TrashbotGUI')
        self._widget.setLayout(large_box)
        context.add_widget(self._widget)
        
    def create_button(self, name, callback):
        btn = QtGui.QPushButton(name, self._widget)
        btn.clicked.connect(callback)
        btn.setAutoRepeat(True)
        return btn

    def printCallback(self):
        print 'nice'
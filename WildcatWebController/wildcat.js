"use strict"

var rosLocal;
var rosRobot;
var currentPos;

window.onload = function() {
  init();
};

/**
 * Setup all GUI elements when the page is loaded.
 */
function init() {



  // Create the image viewer.
  var imageViewer = new MJPEGCANVAS.Viewer({
    divID : 'mjpeg',
    host : 'localhost',
    width : 640,
    height : 480,
    topic : '/camera/rgb/image_raw'
  });

  // Connect to ROS.
  rosLocal = new ROSLIB.Ros({
    url : 'ws://localhost:9090'
    // url : 'http://leatherback.cs.washington.edu:9090'
  });

  rosRobot = new ROSLIB.Ros({
    // url : 'ws://localhost:9090'
    url : 'ws://128.208.7.174:9090'
  });

  // listenToOdom();

  rosLocal.on('connection', function() {
    console.log('Connected to local websocket server.');
  });

  rosLocal.on('error', function(error) {
    console.log('Error connecting to local websocket server: ', error);
  });

  rosLocal.on('close', function() {
    console.log('Connection to local websocket server closed.');
  });

  rosRobot.on('connection', function() {
    console.log('Connected to robot websocket server.');
  });

  rosRobot.on('error', function(error) {
    console.log('Error connecting to robot websocket server: ', error);
  });

  rosRobot.on('close', function() {
    console.log('Connection to websocket robot server closed.');
  });

  // Create the nav navViewer.
  var navViewer = new ROS2D.Viewer({
    divID : 'nav',
    width : 544,
    height : 512
  });

  // Setup the nav client.
  var nav = NAV2D.OccupancyGridClientNav({
    ros : rosRobot,
    rootObject : navViewer.scene,
    viewer : navViewer,
    serverName : '/move_base'
  });

  $('#forwardButton').mousedown(sendForward);
  $('#backButton').mousedown(sendBackwards);
  $('#leftButton').mousedown(turnLeft);
  $('#rightButton').mousedown(turnRight);
  $('#stopButton').mousedown(stopMotion);
}

// function listenToOdom() {
//   var listener = new ROSLIB.Topic({
//     ros : rosRobot,
//     name : '/odom',
//     messageType : 'Odometery'
//   });

//   listener.subscribe(function(message) {
//     console.log('Received message on ' + listener.name + ': ' + message.data);
//     currentPos = message
//   });
// }

function stopMotion() {
  var cmdPose = new ROSLIB.Topic({
    ros : rosRobot,
    name : 'move_base_simple/goal',
    messageType : 'geometry_msgs/PoseStamped'
  });
  var curPoint = currentPos.pose.pose.position

  var pose = new ROSLIB.Message({
    header : {
      frame_id : "/map",
      stamp : new Date().getTime()
    },
    pose : {
      position: curPoint
    }
  });
  cmdPose.publish(pose);
}


function sendForward() {
  console.log('forward wooooooooo');
  var cmdVel = new ROSLIB.Topic({
    ros : rosRobot,
    name : 'mobile_base/commands/velocity',
    messageType : 'geometry_msgs/Twist'
  });

  var twist = new ROSLIB.Message({
    linear : {
      x : 0.1,
      y : 0,
      z : 0.0
    },
    angular : {
      x : 0,
      y : 0,
      z : 0
    }
  });
  cmdVel.publish(twist);
}

function sendBackwards() {
  console.log('back wooooooooo');
  var cmdVel = new ROSLIB.Topic({
    ros : rosRobot,
    name : 'mobile_base/commands/velocity',
    messageType : 'geometry_msgs/Twist'
  });

  var twist = new ROSLIB.Message({
    linear : {
      x : -0.2,
      y : 0,
      z : 0.0
    },
    angular : {
      x : 0,
      y : 0,
      z : 0
    }
  });
  cmdVel.publish(twist);
}

function turnLeft() {
  console.log('left wooooooooo');
  var cmdVel = new ROSLIB.Topic({
    ros : rosRobot,
    name : 'mobile_base/commands/velocity',
    messageType : 'geometry_msgs/Twist'
  });

  var twist = new ROSLIB.Message({
    linear : {
      x : 0,
      y : 0,
      z : 0.0
    },
    angular : {
      x : 0,
      y : 0,
      z : 1
    }
  });
  cmdVel.publish(twist);
}

function turnRight() {
  console.log('right wooooooooo');
  var cmdVel = new ROSLIB.Topic({
    ros : rosRobot,
    name : 'mobile_base/commands/velocity',
    messageType : 'geometry_msgs/Twist'
  });

  var twist = new ROSLIB.Message({
    linear : {
      x : 0,
      y : 0,
      z : 0.0
    },
    angular : {
      x : 0,
      y : 0,
      z : -1
    }
  });
  cmdVel.publish(twist);
}
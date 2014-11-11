window.onload = function() {
  init();
};

/**
 * Setup all GUI elements when the page is loaded.
 */
function init() {
  // // Connect to ROS.
  // var ros = new ROSLIB.Ros({
  //   url : 'ws://leatherback:9090'
  //   // url : 'http://leatherback.cs.washington.edu:9090'
  // });

  // // Create the nav navViewer.
  // var navViewer = new ROS2D.navViewer({
  //   divID : 'nav',
  //   width : 544,
  //   height : 512
  // });

  // // Setup the nav client.
  // var nav = NAV2D.OccupancyGridClientNav({
  //   ros : ros,
  //   rootObject : navViewer.scene,
  //   navViewer : navViewer,
  //   serverName : '/move_base/goal'
  // });

  // Create the image viewer.
  var imageViewer = new MJPEGCANVAS.Viewer({
    divID : 'mjpeg',
    host : 'localhost',
    width : 640,
    height : 480,
    topic : '/camera/rgb/image_raw'
  });

}
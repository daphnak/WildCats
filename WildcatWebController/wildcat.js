window.onload = function() {
  init();
};

/**
 * Setup all GUI elements when the page is loaded.
 */
function init() {
  // Connect to ROS.
  var ros = new ROSLIB.Ros({
    // url : 'ws://leatherback:9090'
    url : 'http://leatherback.cs.washington.edu:9090'
  });

  // Create the main viewer.
  var viewer = new ROS2D.Viewer({
    divID : 'nav',
    width : 544,
    height : 512
  });

  // Setup the nav client.
  var nav = NAV2D.OccupancyGridClientNav({
    ros : ros,
    rootObject : viewer.scene,
    viewer : viewer,
    serverName : '/move_base/goal'
  });
}
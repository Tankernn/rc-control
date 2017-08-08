$(document).ready(function () {
  var socket = new WebSocket("ws://raspberrypi:54321");
  var keys = [];

  socket.onopen = function() {
    var sendInput = function () {
      socket.send(JSON.stringify(keys));

    };
    setInterval(sendInput, 69);
  }

  $(document).keydown(function(e) {
    if (keys.indexOf(e.keyCode) === -1) {
      keys.push(e.keyCode);
    }
  });

  $(document).keyup(function(e) {
    if (keys.indexOf(e.keyCode) !== -1) {
      keys.splice(keys.indexOf(e.keyCode), 1);
    }
  });
});

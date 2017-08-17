function connect(stream_url, control_url) {
  var socket = new WebSocket(control_url);
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

  $("#stream").append('<img src="' + stream_url + '" width="1280" height="720" />');
}

$(document).ready(function () {
  $("#connect").click(function () {
    connect($("#stream_url").val(), $("#control_url").val());
    $("#settings").remove();
  });
});

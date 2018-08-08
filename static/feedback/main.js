$(document).ready(function() {
  // Correctly decide between ws:// and wss://
  roomId = $("#room_id").text().trim();
  var ws_scheme = window.location.protocol == "https:"
    ? "wss"
    : "ws";
  var ws_path = ws_scheme + '://' + window.location.host + "/feedback/stream/";
  console.log("Connecting to " + ws_path);
  var socket = new ReconnectingWebSocket(ws_path);

  // Helpful debugging
  socket.onopen = function() {
    console.log("Connected to chat socket");
  };
  socket.onclose = function() {
    console.log("Disconnected from chat socket");
  };

  socket.onmessage = function(message) {
    // Decode the JSON
    console.log("Got websocket message " + message.data);
    var data = JSON.parse(message.data);
    // Handle errors
    if (data.error) {
      alert(data.error);
      return;
    }
    // Handle joining
    if (data.join) {
      console.log("Joining room " + data.join);
        // socket.send(JSON.stringify({"command": "send", "room": data.join, "message": "test"}));
      // Handle leaving
    } else if (data.leave) {
      console.log("Leaving room " + data.leave);
    } else if (data.message || data.msg_type != 0) {
      console.log(data)
    } else {
      console.log("Cannot handle message!");
    }
  };

  // Room join/leave
  $("#join-room").click(function() {
    socket.send(JSON.stringify({"command": "join", "room": roomId}));
    // $(this).hide();
    $("#event-details").hide();
    $("#event-feeback").show();
  });



  // socket.send(JSON.stringify({
  //   "command": "leave", // determines which handler will be used (see chat/routing.py)
  //   "room": roomId
  // }));
});

var ws = new WebSocket("ws://localhost:8881/websocket");
ws.onopen = function() {
   ws.send("test websocket");
};
ws.onmessage = function (evt) {
   alert(evt.data);
};
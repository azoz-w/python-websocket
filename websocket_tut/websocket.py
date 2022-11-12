import asyncio
import tornado.web
import tornado.ioloop
import tornado.websocket
import logging
import tornado.escape
import tornado.options
import os.path
import uuid
from tornado.options import define, options

define("port", default=8881, help="run on the given port", type=int)

# this is a handler for the websocket


class EchoWebSocket(tornado.websocket.WebSocketHandler):
    def open(self):
        print("WebSocket opened")

    def on_message(self, message):
        self.write_message(u"You said: " + message)

    def on_close(self):
        print("WebSocket closed")
# this is also a handler


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")


# setting for the application
settings = dict(
    # cookie_secret="this is a secret for the token",
    template_path=os.path.join(os.path.dirname(__file__), "templates"),
    static_path=os.path.join(os.path.dirname(__file__), "static"),
    # xsrf_cookies=True,
    debug=True,
)

# here is where we create the app and set its handlers and settings and other arguments


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler), (r"/websocket", EchoWebSocket)
    ], **settings)


# this is the main fucntion to start every thing just like main in java
async def main():
    app = make_app()
    app.listen(options.port)
    shutdown_event = asyncio.Event()
    await shutdown_event.wait()

# this will call the main
if __name__ == "__main__":
    asyncio.run(main())

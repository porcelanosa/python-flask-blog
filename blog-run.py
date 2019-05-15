# -*- coding: utf-8 -*-
from blog import app
from blog import socketio

# if __name__ == '__main__':
#     app.run()

if __name__ == '__main__':
    socketio.run(app, debug=True)

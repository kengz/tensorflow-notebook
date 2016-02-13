# pip install -U socketIO-client

from socketIO_client import SocketIO

socket = SocketIO('localhost', 8080, wait_for_connection=False)

def main_res(str):
  print("py gotten main", str)

socket.emit('join', 'main.py', print)
socket.on('disconnect', socket.disconnect)

socket.on('take', main_res)

# dc errpr; kill process from bash to solve this
socket.wait()

# pip install -U socketIO-client

from socketIO_client import SocketIO

socket = SocketIO('localhost', 8080)

# print(socket)
# socket.on('connectsss', print("connected"))
def main_res(str):
  print("py gotten main", str)

# socket.on('chat msg', main_res)
socket.on('take', main_res)

socket.emit('join', 'main.py', print)
# socket.on('disconnect', socket.disconnect)

# socket.emit('close')
# socket.emit('mainpy')
# socket.emit('main')
# socket.emit('chat msg', 'from python')

socket.wait()


var socket = require('socket.io-client')('http://localhost:8080')

// first join for serialization
socket.emit('join', 'main2.js', console.log)
socket.on('disconnect', socket.disconnect)

// pass task to target script
socket.emit('pass', {
  str: 'task1',
  to: 'main.py',
  from: 'main2.js'
}, console.log)


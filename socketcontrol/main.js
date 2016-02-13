// hosting server: simulating socketio in hubot
var _ = require('lodash')
var app = require('express')()
var server = app.listen(8080)
var io = require('socket.io')(server)


// process.on('SIGINT', () => {
//   console.log("exitting")
//   _.each(io.sockets.sockets, function(s) {
//     s.disconnect(true)
//   })
//   // io.close()
//   process.exit()
// })


// serialize for direct communication by using join room
io.sockets.on('connection', function(socket) {
  socket.on('join', function(id) {
    socket.join(id)
  })
})


io.on('connection', function(socket) {
  // generic pass to other script
  socket.on('pass', function(msg, fn) {
    fn(msg)
    io.sockets.in(msg.to).emit('take', msg)
  })
})

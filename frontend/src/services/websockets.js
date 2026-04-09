let socket = null

export const connectScanner = (callback) => {

  socket = new WebSocket("ws://127.0.0.1:8001/ws/scan")

  socket.onmessage = (event) => {
    callback(event.data)
  }

}

export const sendPing = () => {

  if(socket){
    socket.send("ping")
  }

}

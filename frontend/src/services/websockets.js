let socket = null

export const connectScanner = (callback) => {

  const API = import.meta.env.VITE_API_URL;

  // 🔥 Convert https → wss (secure websocket)
  const WS_URL = API.replace("https", "wss")

  socket = new WebSocket(`${WS_URL}/ws/scan`)

  socket.onmessage = (event) => {
    callback(event.data)
  }

}

export const sendPing = () => {

  if (socket) {
    socket.send("ping")
  }

}
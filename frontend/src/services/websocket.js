export function createScanSocket(onMessage) {

  const API = import.meta.env.VITE_API_URL;

  // 🔥 Convert https → wss for secure websocket
  const WS_URL = API.replace("https", "wss");

  const ws = new WebSocket(`${WS_URL}/scan/ws`);

  ws.onmessage = (event) => {
    onMessage(JSON.parse(event.data))
  }

  return ws
}
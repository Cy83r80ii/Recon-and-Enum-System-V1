export function createScanSocket(onMessage) {
  const ws = new WebSocket("ws://localhost:8000/scan/ws")

  ws.onmessage = (event) => {
    onMessage(JSON.parse(event.data))
  }

  return ws
}

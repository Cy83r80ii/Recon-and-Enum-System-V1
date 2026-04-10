import { useState } from "react"
import axios from "axios"

export default function ScanPanel() {

  const [target, setTarget] = useState("")
  const [mode, setMode] = useState("quick")

  async function startScan() {

    const API = import.meta.env.VITE_API_URL;

    try {
      await axios.post(`${API}/scan`, {
        target,
        mode
      })
    } catch (err) {
      console.error("Scan failed:", err)
    }

  }

  return (
    <div className="scan-panel">

      <input
        placeholder="https://target.com"
        value={target}
        onChange={(e) => setTarget(e.target.value)}
      />

      <select
        value={mode}
        onChange={(e) => setMode(e.target.value)}
      >
        <option value="quick">Quick</option>
        <option value="deep">Deep</option>
        <option value="aggressive">Aggressive</option>
      </select>

      <button onClick={startScan}>Start Scan</button>

    </div>
  )
}
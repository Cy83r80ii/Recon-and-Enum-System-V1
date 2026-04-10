import { useEffect, useState } from "react"
import axios from "axios"

export default function LiveScanner() {

  const [logs, setLogs] = useState([])

  useEffect(() => {

    const API = import.meta.env.VITE_API_URL;

    const interval = setInterval(async () => {
      try {
        const res = await axios.get(`${API}/logs`)
        setLogs(res.data.logs)
      } catch (err) {
        console.error("Error fetching logs:", err)
      }
    }, 2000)

    return () => clearInterval(interval)

  }, [])

  return (
    <div className="console">
      {logs.map((l, i) => (
        <div key={i}>{"> " + l}</div>
      ))}
    </div>
  )
}
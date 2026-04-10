import { useEffect, useState } from "react"
import axios from "axios"

export default function ProgressBar() {

  const [progress, setProgress] = useState(0)

  useEffect(() => {

    const API = import.meta.env.VITE_API_URL;

    const interval = setInterval(async () => {
      try {
        const res = await axios.get(`${API}/progress`)
        setProgress(res.data.progress)
      } catch (e) {
        console.error("Error fetching progress:", e)
      }
    }, 1000)

    return () => clearInterval(interval)

  }, [])

  return (
    <div className="progress-wrapper">
      <div className="progress-bar">
        <div
          className="progress-fill"
          style={{ width: progress + "%" }}
        />
      </div>
      <p>{progress}%</p>
    </div>
  )
}
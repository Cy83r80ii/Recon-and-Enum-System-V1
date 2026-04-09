import { useEffect, useState } from "react"

function AIAssistant({ stats }) {
  const [text, setText] = useState("Awaiting scan...")

  useEffect(() => {
    if (!stats) return

    if (stats.critical > 0) {
      setText("🚨 Critical vulnerability detected. Immediate patching required.")
    } else if (stats.high > 0) {
      setText("⚠ High-risk findings identified. Review recommended.")
    } else if (stats.total > 0) {
      setText("✅ Scan completed. Review findings below.")
    } else {
      setText("Awaiting scan...")
    }
  }, [stats])

  return (
    <div className="card h-full">
      <h2 className="text-red-500 font-semibold mb-4">
        AI Security Assistant
      </h2>

      <div className="text-gray-300 text-sm font-mono min-h-[120px] leading-relaxed">
        {text}
      </div>
    </div>
  )
}

export default AIAssistant

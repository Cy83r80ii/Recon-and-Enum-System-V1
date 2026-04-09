import { Link } from "react-router-dom"
import CyberBackground from "../components/effects/CyberBackground"

export default function Landing() {

  return (

    <div className="min-h-screen flex items-center justify-center bg-black text-white">

      <CyberBackground/>

      <div className="text-center space-y-6">

        <h1 className="text-5xl font-bold text-red-500">
          ARES‑X
        </h1>

        <p className="text-gray-400">
          AI Vulnerability Assessment Framework
        </p>

        <Link
          to="/dashboard"
          className="bg-red-600 px-6 py-3 rounded-lg hover:bg-red-700"
        >
          Launch Scanner
        </Link>

      </div>

    </div>
  )
}

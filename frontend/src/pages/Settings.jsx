import Navbar from "../components/layout/Navbar"
import Sidebar from "../components/layout/Sidebar"

export default function Settings() {

  return (

    <div className="flex bg-black text-white min-h-screen">

      <Sidebar/>

      <div className="flex-1">

        <Navbar/>

        <div className="p-10">

          <h1 className="text-3xl text-red-500 mb-6">
            Settings
          </h1>

          <div className="bg-gray-900 p-6 rounded-lg space-y-4">

            <p className="text-gray-400">
              Scanner configuration options will appear here.
            </p>

            <div>
              <label className="block text-gray-400 mb-1">
                Default Scan Mode
              </label>

              <select className="bg-black border border-gray-700 p-2 rounded w-60">
                <option>Quick</option>
                <option>Deep</option>
                <option>Aggressive</option>
              </select>
            </div>

          </div>

        </div>

      </div>

    </div>
  )
}

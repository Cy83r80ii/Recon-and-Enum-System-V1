import Navbar from "../components/layout/Navbar"
import Sidebar from "../components/layout/Sidebar"
import PDFButton from "../components/reports/PDFButton"

export default function Reports() {

  return (

    <div className="flex bg-black text-white min-h-screen">

      <Sidebar/>

      <div className="flex-1">

        <Navbar/>

        <div className="p-10">

          <h1 className="text-3xl text-red-500 mb-6">
            Scan Reports
          </h1>

          <div className="bg-gray-900 p-6 rounded-lg">

            <p className="text-gray-400 mb-4">
              Download latest vulnerability scan report.
            </p>

            <PDFButton/>

          </div>

        </div>

      </div>

    </div>
  )
}

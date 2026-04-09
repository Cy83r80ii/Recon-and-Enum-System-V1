export default function RiskHeatmap(){

  const risks = [
    {name:"SQL Injection",level:"High"},
    {name:"XSS",level:"Medium"},
    {name:"IDOR",level:"Low"},
    {name:"Path Traversal",level:"Low"}
  ]

  return(

    <div className="bg-gray-900 p-6 rounded-lg">

      <h2 className="text-red-500 text-xl mb-4">
        Risk Overview
      </h2>

      <div className="grid grid-cols-4 gap-4">

        {risks.map((r,i)=>(
          <div key={i} className="bg-black p-4 rounded text-center">

            <h3 className="text-white">{r.name}</h3>

            <p className="text-red-400">{r.level}</p>

          </div>
        ))}

      </div>

    </div>

  )
}

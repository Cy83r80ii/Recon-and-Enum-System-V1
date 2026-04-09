import { useState } from "react"
import axios from "axios"

export default function ScanPanel(){

const [target,setTarget] = useState("")
const [mode,setMode] = useState("quick")

async function startScan(){

await axios.post("http://127.0.0.1:8001/scan",{
target,
mode
})

}

return(

<div className="scan-panel">

<input
placeholder="https://target.com"
value={target}
onChange={(e)=>setTarget(e.target.value)}
/>

<select
value={mode}
onChange={(e)=>setMode(e.target.value)}
>

<option value="quick">Quick</option>
<option value="deep">Deep</option>
<option value="aggressive">Aggressive</option>

</select>

<button onClick={startScan}>Start Scan</button>

</div>

)

}

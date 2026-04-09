import {useEffect,useState} from "react"
import axios from "axios"

export default function LiveScanner(){

const [logs,setLogs]=useState([])

useEffect(()=>{

const interval=setInterval(async()=>{

const res=await axios.get("http://127.0.0.1:8001/logs")

setLogs(res.data.logs)

},2000)

return ()=>clearInterval(interval)

},[])

return(

<div className="console">

{logs.map((l,i)=>(
<div key={i}>{"> "+l}</div>
))}

</div>

)

}
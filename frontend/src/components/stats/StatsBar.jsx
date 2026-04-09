import {useEffect,useState} from "react"
import axios from "axios"

export default function StatsBar(){

const [stats,setStats] = useState({
critical:0,
high:0,
medium:0,
low:0,
total:0
})

useEffect(()=>{

const interval=setInterval(async ()=>{

const res = await axios.get("http://127.0.0.1:8001/results")

const findings=res.data.findings || []

let critical=0
let high=0
let medium=0
let low=0

findings.forEach(f=>{

if(f.severity==="critical") critical++
if(f.severity==="high") high++
if(f.severity==="medium") medium++
if(f.severity==="low") low++

})

setStats({
critical,
high,
medium,
low,
total:findings.length
})

},3000)

return ()=>clearInterval(interval)

},[])

return(

<div className="stats">

<div>Critical {stats.critical}</div>
<div>High {stats.high}</div>
<div>Medium {stats.medium}</div>
<div>Low {stats.low}</div>
<div>Total {stats.total}</div>

</div>

)

}
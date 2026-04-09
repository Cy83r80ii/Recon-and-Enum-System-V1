import {useEffect,useState} from "react"
import axios from "axios"

export default function ProgressBar(){

const [progress,setProgress] = useState(0)

useEffect(()=>{

const interval=setInterval(async()=>{

try{

const res = await axios.get("http://127.0.0.1:8001/progress")

setProgress(res.data.progress)

}catch(e){}

},1000)

return ()=>clearInterval(interval)

},[])

return(

<div className="progress-wrapper">

<div className="progress-bar">

<div
className="progress-fill"
style={{width:progress+"%"}}
/>

</div>

<p>{progress}%</p>

</div>

)

}
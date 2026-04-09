import React, { useEffect, useState } from "react";
import axios from "axios";

import ScanPanel from "../components/scan/ScanPanel";
import ResultsTable from "../components/results/ResultsTable";

import SeverityChart from "../components/stats/SeverityChart";
import BugChart from "../components/stats/BugChart";
import VulnerabilityCards from "../components/stats/VulnerabilityCards";

export default function Dashboard() {

const [findings,setFindings] = useState([]);

const [stats,setStats] = useState({
critical:0,
high:0,
medium:0,
low:0,
total:0
});

const [progress,setProgress] = useState(0);
const [logs,setLogs] = useState([]);

useEffect(()=>{

const interval = setInterval(async()=>{

try{

// results
const res = await axios.get("http://127.0.0.1:8001/results");
const findingsData = res.data.findings || [];

setFindings(findingsData);

// compute severity stats
let critical=0;
let high=0;
let medium=0;
let low=0;

findingsData.forEach(f=>{

const sev = (f.severity || "").toLowerCase();

if(sev==="critical") critical++;
if(sev==="high") high++;
if(sev==="medium") medium++;
if(sev==="low") low++;

});

setStats({
critical,
high,
medium,
low,
total:findingsData.length
});

}catch(e){}

// progress
try{

const p = await axios.get("http://127.0.0.1:8001/progress");
setProgress(p.data.progress || 0);

}catch(e){}

// logs
try{

const l = await axios.get("http://127.0.0.1:8001/logs");
setLogs(l.data.logs || []);

}catch(e){}

},2000);

return ()=>clearInterval(interval);

},[]);

return(

<div className="dashboard">

{/* TITLE */}

<h1 className="title">ARES‑X Security Scanner</h1>

{/* SCAN PANEL */}

<ScanPanel/>

{/* PROGRESS BAR */}

<div className="panel">

<h3>Scan Progress</h3>

<div className="progress-wrapper">

<div className="progress-bar">

<div
className="progress-fill"
style={{width:progress+"%"}}
/>

</div>

<p>{progress}%</p>

</div>

</div>

{/* VULNERABILITY CARDS */}

<VulnerabilityCards stats={stats}/>

{/* CHARTS */}

<div className="charts">

<SeverityChart stats={stats}/>

<BugChart findings={findings}/>

</div>

{/* LIVE TERMINAL */}

<div className="panel">

<h3>Live Engine Output</h3>

<div className="console">

{logs.length === 0 ? (
<p>Waiting for scan...</p>
) : (
logs.map((log,i)=>(
<div key={i}>{"> "+log}</div>
))
)}

</div>

</div>

{/* RESULTS TABLE */}

<ResultsTable findings={findings}/>

</div>

)

}
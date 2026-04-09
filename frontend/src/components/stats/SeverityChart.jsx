import React from "react";

import {
PieChart,
Pie,
Cell,
Tooltip,
Legend
} from "recharts";

export default function SeverityChart({ stats = {} }) {

const data = [

{ name:"Critical", value: stats.critical || 0 },
{ name:"High", value: stats.high || 0 },
{ name:"Medium", value: stats.medium || 0 },
{ name:"Low", value: stats.low || 0 }

];

const COLORS = [
"#ff0033",
"#ff6b00",
"#ffd000",
"#00ff9c"
];

return(

<div className="chart-panel">

<h3>Severity Distribution</h3>

<PieChart width={350} height={260}>

<Pie
data={data}
dataKey="value"
nameKey="name"
cx="50%"
cy="50%"
outerRadius={90}
label
>

{data.map((entry,index)=>(
<Cell key={index} fill={COLORS[index]} />
))}

</Pie>

<Tooltip/>
<Legend/>

</PieChart>

</div>

)

}
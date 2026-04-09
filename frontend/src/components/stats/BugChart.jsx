import React from "react";

import {
BarChart,
Bar,
XAxis,
YAxis,
Tooltip,
CartesianGrid
} from "recharts";

export default function BugChart({ findings = [] }) {

const counts = {};

findings.forEach(f => {

const type = f.type || "Unknown";

counts[type] = (counts[type] || 0) + 1;

});

const data = Object.keys(counts).map(k => ({
name: k,
value: counts[k]
}));

return(

<div className="chart-panel">

<h3>Vulnerability Types</h3>

<BarChart
width={400}
height={260}
data={data}
>

<CartesianGrid stroke="#222" />

<XAxis dataKey="name" />

<YAxis />

<Tooltip />

<Bar
dataKey="value"
fill="#ff2a2a"
/>

</BarChart>

</div>

)

}
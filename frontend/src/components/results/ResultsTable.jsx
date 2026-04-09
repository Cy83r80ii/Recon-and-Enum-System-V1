import React from "react";

export default function ResultsTable({ findings = [] }) {

return (

<div className="panel">

<h3>Findings</h3>

<table className="results-table">

<thead>
<tr>
<th>Type</th>
<th>URL</th>
<th>Severity</th>
</tr>
</thead>

<tbody>

{findings.length === 0 ? (
<tr>
<td colSpan="3">No findings yet</td>
</tr>
) : (

findings.map((f,i)=>(

<tr key={i}>

<td>{f.type || "unknown"}</td>

<td className="url-cell">
{f.url || "N/A"}
</td>

<td className={`sev-${(f.severity || "low").toLowerCase()}`}>
{f.severity || "low"}
</td>

</tr>

))

)}

</tbody>

</table>

</div>

)

}
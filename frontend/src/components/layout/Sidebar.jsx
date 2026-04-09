import { Link } from "react-router-dom"

export default function Sidebar(){

return(

<div className="sidebar">

<h2 className="logo">ARES‑X</h2>

<Link to="/">
<p className="menu-item">Dashboard</p>
</Link>

<Link to="/reports">
<p className="menu-item">Reports</p>
</Link>

<Link to="/settings">
<p className="menu-item">Settings</p>
</Link>

</div>

)

}
import React, { useEffect, useState } from "react";
import axios from "axios";

import ScanPanel from "../components/scan/ScanPanel";
import ResultsTable from "../components/results/ResultsTable";

import SeverityChart from "../components/stats/SeverityChart";
import BugChart from "../components/stats/BugChart";
import VulnerabilityCards from "../components/stats/VulnerabilityCards";

export default function Dashboard() {

  const [findings, setFindings] = useState([]);

  const [stats, setStats] = useState({
    critical: 0,
    high: 0,
    medium: 0,
    low: 0,
    total: 0
  });

  const [progress, setProgress] = useState(0);
  const [logs, setLogs] = useState([]);

  useEffect(() => {

    const API = import.meta.env.VITE_API_URL;

    const interval = setInterval(async () => {

      // 🔹 RESULTS
      try {
        const res = await axios.get(`${API}/results`);
        const findingsData = res.data.findings || [];

        setFindings(findingsData);

        let critical = 0;
        let high = 0;
        let medium = 0;
        let low = 0;

        findingsData.forEach(f => {
          const sev = (f.severity || "").toLowerCase();
          if (sev === "critical") critical++;
          if (sev === "high") high++;
          if (sev === "medium") medium++;
          if (sev === "low") low++;
        });

        setStats({
          critical,
          high,
          medium,
          low,
          total: findingsData.length
        });

      } catch (e) {
        console.error("Results error:", e);
      }

      // 🔹 PROGRESS
      try {
        const p = await axios.get(`${API}/progress`);
        setProgress(p.data.progress || 0);
      } catch (e) {
        console.error("Progress error:", e);
      }

      // 🔹 LOGS
      try {
        const l = await axios.get(`${API}/logs`);
        setLogs(l.data.logs || []);
      } catch (e) {
        console.error("Logs error:", e);
      }

    }, 2000);

    return () => clearInterval(interval);

  }, []);

  return (
    <div className="dashboard">

      <h1 className="title">ARES‑X Security Scanner</h1>

      <ScanPanel />

      <div className="panel">
        <h3>Scan Progress</h3>

        <div className="progress-wrapper">
          <div className="progress-bar">
            <div
              className="progress-fill"
              style={{ width: progress + "%" }}
            />
          </div>
          <p>{progress}%</p>
        </div>
      </div>

      <VulnerabilityCards stats={stats} />

      <div className="charts">
        <SeverityChart stats={stats} />
        <BugChart findings={findings} />
      </div>

      <div className="panel">
        <h3>Live Engine Output</h3>

        <div className="console">
          {logs.length === 0 ? (
            <p>Waiting for scan...</p>
          ) : (
            logs.map((log, i) => (
              <div key={i}>{"> " + log}</div>
            ))
          )}
        </div>
      </div>

      <ResultsTable findings={findings} />

    </div>
  );
}
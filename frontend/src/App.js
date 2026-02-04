import React, { useState } from "react";
import "./App.css";
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
} from "recharts";

function App() {
  const [file, setFile] = useState(null);
  const [language, setLanguage] = useState("en");
  const [company, setCompany] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [darkMode, setDarkMode] = useState(false);

  const analyzeFile = async () => {
    if (!file || !company) {
      alert("Please enter company name and upload CSV file");
      return;
    }

    setLoading(true);

    try {
      const formData = new FormData();
      formData.append("file", file);
      formData.append("company_name", company);

      const response = await fetch(
         `${process.env.REACT_APP_BACKEND_URL}/analyze?language=${language}`,
        {
          method: "POST",
          body: formData,
        }
      );

      const data = await response.json();
      setResult(data);
    } catch (error) {
      alert("Backend not reachable");
    } finally {
      setLoading(false);
    }
  };

  const chartData =
    result?.raw_metrics
      ? [
          {
            name: "Revenue",
            value: result.raw_metrics["Total Revenue"],
          },
          {
            name: "Expense",
            value: result.raw_metrics["Total Expense"],
          },
        ]
      : [];

  return (
    <div className={darkMode ? "dark" : "light"}>
      <button className="toggle" onClick={() => setDarkMode(!darkMode)}>
        {darkMode ? "☀️ Light" : "🌙 Dark"}
      </button>

      <div className="container">
        <h1 className="title">Financial Health Assessment Tool</h1>

        <div className="controls">
          <input
            type="text"
            placeholder="🏢 Company Name"
            value={company}
            onChange={(e) => setCompany(e.target.value)}
          />

          <input
            type="file"
            accept=".csv"
            onChange={(e) => setFile(e.target.files[0])}
          />

          <select
            value={language}
            onChange={(e) => setLanguage(e.target.value)}
          >
            <option value="en">English</option>
            <option value="hi">Hindi</option>
            <option value="kn">Kannada</option>
          </select>

          <button onClick={analyzeFile}>📊 Analyze</button>
        </div>

        {loading && <p>Analyzing financial data…</p>}

        {result && (
          <>
            <div className="section">
              <h3>📊 Financial Metrics</h3>
              <ul className="metrics-list">
                {result?.metrics &&
                  Object.entries(result.metrics).map(([key, value]) => (
                    <li key={key}>
                      <strong>{key}:</strong> {value}
                    </li>
                  ))}
              </ul>
            </div>

            <div className="section">
              <h3>📈 Revenue vs Expense</h3>
              <ResponsiveContainer width="100%" height={250}>
                <BarChart data={chartData}>
                  <XAxis dataKey="name" />
                  <YAxis />
                  <Tooltip />
                  <Bar dataKey="value" fill="#4f46e5" />
                </BarChart>
              </ResponsiveContainer>
            </div>

            <div className="section">
              <h3>⚠️ AI Insights</h3>
              <div className="ai-box">{result.ai_insights}</div>
            </div>
          </>
        )}
      </div>
    </div>
  );
}

export default App;

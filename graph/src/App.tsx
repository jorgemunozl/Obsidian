import React, { useState, useEffect } from "react";
import { createRoot } from "react-dom/client";
import { Chart } from "chart.js";
import "katex/dist/katex.min.css";
import katex from "katex";

function App() {
  const [expr, setExpr] = useState("2*x + 1");
  const [chartInstance, setChartInstance] = useState<Chart | null>(null);

  const xValues = Array.from({ length: 21 }, (_, i) => i - 10);

  const renderChart = (funcStr: string) => {
    try {
      const f = new Function("x", `return ${funcStr}`);
      const yValues = xValues.map(f);

      if (chartInstance) {
        chartInstance.data.datasets[0].data = yValues;
        chartInstance.update();
      } else {
        const ctx = document.getElementById("plot") as HTMLCanvasElement;
        const newChart = new Chart(ctx, {
          type: "line",
          data: {
            labels: xValues,
            datasets: [{
              label: `y = ${funcStr}`,
              data: yValues,
              borderColor: "blue",
              fill: false,
              tension: 0
            }]
          },
          options: {
            responsive: true,
            scales: {
              x: { title: { display: true, text: 'x' } },
              y: { title: { display: true, text: 'y' } }
            }
          }
        });
        setChartInstance(newChart);
      }
    } catch (err) {
      console.error("Invalid function", err);
    }
  };

  useEffect(() => {
    renderChart(expr);
  }, [expr]);

  const renderLatex = (input: string) => {
    try {
      return katex.renderToString(input, { throwOnError: false });
    } catch {
      return "Invalid LaTeX";
    }
  };

  return (
    <div className="p-4">
      <h1 className="text-xl font-bold mb-2">🧮 Live Function Plotter + LaTeX Renderer</h1>

      <label className="block mb-1">Enter JS expression (e.g., <code>2*x + 1</code>):</label>
      <input
        className="border px-2 py-1 w-full mb-4"
        value={expr}
        onChange={(e) => setExpr(e.target.value)}
      />

      <canvas id="plot" className="mb-4"></canvas>

      <div>
        <h2 className="font-semibold">🧠 Rendered LaTeX:</h2>
        <div
          className="border p-2 mt-2 text-lg"
          dangerouslySetInnerHTML={{ __html: renderLatex(expr) }}
        />
      </div>
    </div>
  );
}

const container = document.getElementById("root");
if (container) {
  const root = createRoot(container);
  root.render(<App />);
}
export default App;

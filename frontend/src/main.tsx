import React from "react";
import { createRoot } from "react-dom/client";

function App(){
  return <div style={{fontFamily:"Arial, sans-serif",padding:20}}>
    <h1>Container Demo Frontend</h1>
    <p>This is a minimal React app served from a container.</p>
    <p>It talks to the API at <code>/api</code> (use proxy in dev)</p>
  </div>;
}

createRoot(document.getElementById("root")!).render(<App />);

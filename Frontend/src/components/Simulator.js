import axios from "axios";
import React from "react";

const Simulator = () => {
  const runScript = () => {
    axios
      .post("http://localhost:5000/run-simulator")
      .then((response) => {
        console.log(response.data.message);
        // Handle success message
      })
      .catch((error) => {
        console.error(error);
        // Handle error message
      });
  };

  return (
    <div>
      <button onClick={runScript}>Run Python Simulator</button>
    </div>
  );
};

export default Simulator;

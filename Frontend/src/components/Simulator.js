import axios from "axios";
import React from "react";

const Simulator = () => {
  const runScript = () => {
    axios
      .post("http://localhost:5000/run-script")
      .then((response) => {
        console.log(response.data.message);
        // Handle success message
      })
      .catch((error) => {
        console.error(error);
        // Handle error message
      });
  };

  const stopScript = () => {
    axios
      .post("http://localhost:5000/stop-script")
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
      <button onClick={runScript}>Run Python Script</button>
      <button onClick={stopScript}>Stop Python Script</button>
    </div>
  );
};

export default Simulator;

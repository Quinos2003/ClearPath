import React from "react";
import CoolButton from "../components/Button/CoolButton";
import { Link } from "react-router-dom";
import VideoUploader from "../components/VideoUploadForm";

const Dashboard = () => {
  return (
    <div className="flex justify-center items-center text-3xl h-full">
      <Link to="/vehiclecount">
        <CoolButton />
      </Link>
    </div>
  );
};

export default Dashboard;

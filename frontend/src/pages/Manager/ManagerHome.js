import React from "react";
import Navbar from "../../components/Navbar";
import { useState } from "react";
import { useNavigate } from "react-router-dom";


function ManagerHome() {
  const [currentTab, setCurrentTab] = useState("home");
  const navigate = useNavigate();

  return (
    <div>
      <Navbar />
      <h1 className="text-3xl font-bold underline">Manager's Home!</h1>
    </div>
  );
}

export default ManagerHome;

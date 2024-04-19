import React from "react";
import Navbar from "../../../components/Navbar";
import { useNavigate } from "react-router-dom";

function CreateCasino() {
  const navigate = useNavigate();

  const handleCasinoClick = (casinoType) => {
    navigate(`/create-casino/customize?type=${casinoType}`);
  };

  return (
    <div>
      <Navbar />
      <h1 className="text-2xl font-semibold mb-4">Select a Casino Type:</h1>
      <div className="space-y-4">
        <button
          onClick={() => handleCasinoClick("A")}
          className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:ring-2 focus:ring-blue-400"
        >
          Type 1 Casino
        </button>
        <button
          onClick={() => handleCasinoClick("B")}
          className="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:ring-2 focus:ring-green-400"
        >
          Type 2 Casino
        </button>
        <button
          onClick={() => handleCasinoClick("C")}
          className="bg-yellow-500 hover:bg-yellow-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:ring-2 focus:ring-yellow-400"
        >
          Type 3 Casino
        </button>
        <button
          onClick={() => handleCasinoClick("D")}
          className="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:ring-2 focus:ring-red-400"
        >
          Type 4 Casino
        </button>
      </div>
    </div>
  );
}

export default CreateCasino;

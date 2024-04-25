import React, { useState } from "react";
import Navbar from "../../components/Navbar";
import { useParams } from "react-router-dom";

function GameTablePlay() {
  const [inputValue, setInputValue] = useState("");
  const [maxValue, setMaxValue] = useState(100); // Specify your max value here
  const { gametableId } = useParams();
  const [gameResponse, setGameResponse] = useState("");
  const userId = localStorage.getItem("userId");
  const gametabletype = gametableId[9];
  // fetch casionId from local storage
  const casinoId = localStorage.getItem("casinoid");
  // console.log("gametableId:", gametableId)
  const handleChange = (event) => {
    const { value } = event.target;
    // Validate input to ensure it's a number and within the specified range
    if (!isNaN(value) && Number(value) >= 0 && Number(value) <= maxValue) {
      setInputValue(value);
    }
  };
  const addMoney = async (amountToAdd) => {
    console.log("Amount to add:", amountToAdd);
    try {
      const response = await fetch(`http://localhost:5000/wallet/addRecordBalance`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        // calculate the total wallet balance as (balance+amountToAdd)
       
        body: JSON.stringify({ user_id: userId, amount: amountToAdd,strategy: "cash", currency:"INR",casino_id:casinoId})
      });
      const data = await response.json();
      console.log(data);
      fetchBalance();  // Re-fetch balance to update the displayed amount
    } catch (error) {
      console.error('Failed to add money:', error);
    }
  };
  const handlePlayClick = async () => {
    try {
      const response = await fetch("/play", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          gametableId: gametableId,
          amount: inputValue,
        }),
      });
      if (!response.ok) {
        throw new Error("Failed to play game table");
      }
      const data = await response.json();
      setGameResponse(data.final_amount);
      console.log("Data received:", data); // Log the received data
    }
    catch (error) {
      console.error("Error playing game table:", error);
    }
  };

  return (
    <div>
      <Navbar />
      <h1 className="text-3xl font-bold underline">User GameTablePlay</h1>
      <div className="text-center mt-8">
        <input
          type="number"
          className="border border-gray-300 rounded-md px-4 py-2"
          value={inputValue}
          onChange={handleChange}
          placeholder={`Enter a number between 0 and ${maxValue}`}
        />
        <button
          className="ml-2 bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded"
          onClick={handlePlayClick}
        >
          {gameResponse ? "Play Again" : "Play"}
        </button>
        {gameResponse && (
          <div className="mt-4">
            <p>Reward: {gameResponse}</p>
            <p>Reward: {gameResponse}</p>
          </div>
        )}
      </div>
    </div>
  );
}

export default GameTablePlay;

import React, { useState,useEffect } from "react";
import Navbar from "../../components/Navbar";
import { useParams } from "react-router-dom";

function GameTablePlay() {
  const [balance, setBalance] = useState(0);
  const [inputValue, setInputValue] = useState("");
  // const [maxValue, setMaxValue] = useState(100); // Specify your max value here
  const { gametableId } = useParams();
  const [gameResponse, setGameResponse] = useState("");
  const userId = localStorage.getItem("userId");
  const gametabletype = gametableId[9]
  // console.log("gametableId:", gametableId)
  const handleChange = (event) => {
    const { value } = event.target;
    // Validate input to ensure it's a number and within the specified range
    if (!isNaN(value) && Number(value) >= 0) {
      setInputValue(value);
    }
  };
  const addMoney = async (amountToAdd) => {
    try {
      const response = await fetch(`http://localhost:5000/wallet/addBalance`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        // calculate the total wallet balance as (balance+amountToAdd)
        body: JSON.stringify({ user_id: userId, amount: amountToAdd,strategy: "cash"})
      });
      const data = await response.json();
      console.log(data);
      fetchBalance();  // Re-fetch balance to update the displayed amount
    } catch (error) {
      console.error('Failed to add money:', error);
    }
  };
  const handlePlayClick = async () => {
    fetchBalance();
    if (balance < inputValue) {
      window.alert('Your balance is less than the input value. Please add more money to your account.');
      return;
    }
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
      setGameResponse(data.final_amount); // Set the final amount from the response
      console.log("Data received:", data); // Log the received data
  
      // Calculate and handle loss here
      const lossAmount = inputValue - data.final_amount; // Ensure no negative loss
      console.log("Loss amount:", lossAmount);
      
      await addMoney(-lossAmount); // Call addMoney with the calculated lossAmount
      
  
    } catch (error) {
      console.error("Error playing game table:", error);
    }
  };
  const fetchBalance = async () => {
    try {
        const response = await fetch(`http://localhost:5000/wallet/balance?user_id=${userId}`);
        const data = await response.json();
        console.log(data);
        setBalance(data); // Adjusted assuming data.balance holds the balance
    } catch (error) {
        console.error('Failed to fetch balance:', error);
    }
  };
  // useEffect hook to call fetchBalance when the component mounts
    useEffect(() => {
        fetchBalance();
    }, []); // The empty array ensures this effect runs only once after the initial render


  return (
    <div>
      <Navbar />
      <h1 className="text-3xl font-bold underline">User GameTablePlay</h1>
      <h2>Your wallet balance is: {balance} tokens</h2>
      <div className="text-center mt-8">
        <input
          type="number"
          className="border border-gray-300 rounded-md px-4 py-2"
          value={inputValue}
          onChange={handleChange}
          placeholder={`Enter money you want to bet`}
        />
        <button
          className="ml-2 bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded"
          onClick={handlePlayClick}
        >
          {gameResponse ? "Play Again" : "Play"}
        </button>
        {gameResponse && (
          <div className="mt-4">
            <p>Final Amount: {gameResponse}</p>
          </div>
        )}
      </div>
    </div>
  );
}

export default GameTablePlay;

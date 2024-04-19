import React, { useState } from "react";
import Navbar from "../../../../components/Navbar";

function CasinoTypeA() {
  // State variables to store input values
  const [gameTableB, setGameTableB] = useState(0);
  const [gameTableD, setGameTableD] = useState(0);
  const [bar, setBar] = useState(0);

  // Function to handle form submission
  const handleSubmit = async (event) => {
    event.preventDefault(); // Prevent default form submission behavior
    let userId = localStorage.getItem("userId")

    // Construct form data
    const formData = {
      userId: userId,
      casinoType: "D",
      gameTableA: 0,
      gameTableB: parseInt(gameTableB), // Convert to integer
      gameTableC: 0,
      gameTableD: parseInt(gameTableD), // Convert to integer
      bar: parseInt(bar)
    };

    // Send form data to the backend
    try {
      const response = await fetch("http://localhost:5000/casino/add", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(formData),
      });

      if (!response.ok) {
        throw new Error("Network response was not ok");
      } else {
        const responseData = await response.json();
        if (responseData.status === "Success") {
          alert("Casino created successfully");
          // console.log("Response:", responseData);
          console.log("Success");
        } else alert("Casino creation failed. Try again.");
      }
    } catch (error) {
      console.error("Error:", error);
      // Handle error from the backend
    }
  };
  const handleInputChange = (e, setter) => {
    const value = parseInt(e.target.value, 10);
    if (!isNaN(value) && value >= 0) {
      setter(value);
    }
  };

  return (
    <div>
      <Navbar />
      <h2 className="text-2xl font-semibold mb-4">Type B Casino Customization</h2>
      <form onSubmit={handleSubmit} className="space-y-4">
        <div>
          <label htmlFor="gameTableA" className="block font-medium">Game Table B:</label>
          <input
            type="number"
            id="gameTableB"
            value={gameTableB}
            onChange={(e) => handleInputChange(e, setGameTableB)}
            className="border border-gray-300 rounded-md py-2 px-4 focus:outline-none focus:border-blue-500"
          />
        </div>
        <div>
          <label htmlFor="gameTableD" className="block font-medium">Game Table D:</label>
          <input
            type="number"
            id="gameTableD"
            value={gameTableD}
            onChange={(e) => handleInputChange(e, setGameTableD)}
            className="border border-gray-300 rounded-md py-2 px-4 focus:outline-none focus:border-blue-500"
          />
        </div>
        <div>
          <label htmlFor="bar" className="block font-medium">Bar:</label>
          <input
            type="number"
            id="bar"
            value={bar}
            onChange={(e) => setBar(e.target.value)}
            className="border border-gray-300 rounded-md py-2 px-4 focus:outline-none focus:border-blue-500"
          />
        </div>
        <button type="submit" className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:ring-2 focus:ring-blue-500">
          Submit
        </button>
      </form>
    </div>
  );
}

export default CasinoTypeA;

import React, { useState } from "react";
import Navbar from "../../../../components/Navbar";

function CasinoTypeA() {
  // State variables to store input values
  const [gameTableA, setGameTableA] = useState(0);
  const [gameTableC, setGameTableC] = useState(0);
  const [bar, setBar] = useState(0);

  // Function to handle form submission
  const handleSubmit = async (event) => {
    event.preventDefault(); // Prevent default form submission behavior
    let userId = localStorage.getItem("userId");
    // Construct form data
    const formData = {
      userId: userId,
      casinoType: "A",
      gameTableA: parseInt(gameTableA), // Convert to integer
      gameTableB: 0,
      gameTableC: parseInt(gameTableC), // Convert to integer
      gameTableD: 0,
      bar: parseInt(bar),
    };
    // console.log("json", JSON.stringify(formData));

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
      <h2 className="text-2xl font-semibold mb-4">
        Type A Casino Customization
      </h2>
      <form onSubmit={handleSubmit} className="space-y-4">
        <div>
          <label htmlFor="gameTableA" className="block font-medium">
            Game Table A:
          </label>
          <input
            type="number"
            id="gameTableA"
            value={gameTableA}
            onChange={(e) => handleInputChange(e, setGameTableA)}
            className="border border-gray-300 rounded-md py-2 px-4 focus:outline-none focus:border-blue-500"
          />
        </div>
        <div>
          <label htmlFor="gameTableB" className="block font-medium">
            Game Table C:
          </label>
          <input
            type="number"
            id="gameTableC"
            value={gameTableC}
            onChange={(e) => handleInputChange(e, setGameTableC)}
            className="border border-gray-300 rounded-md py-2 px-4 focus:outline-none focus:border-blue-500"
          />
        </div>
        <div>
          <label htmlFor="bar" className="block font-medium">
            Bar:
          </label>
          <input
            type="number"
            id="bar"
            value={bar}
            onChange={(e) => handleInputChange(e, setBar)}
            className="border border-gray-300 rounded-md py-2 px-4 focus:outline-none focus:border-blue-500"
          />
        </div>
        <button
          type="submit"
          className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
        >
          Submit
        </button>
      </form>
    </div>
  );
}

export default CasinoTypeA;

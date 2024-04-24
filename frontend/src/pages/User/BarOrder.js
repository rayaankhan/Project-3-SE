import React from "react";
import Navbar from "../../components/Navbar";
import { useState,useEffect } from "react";

function BarOrder() {
  
  const [paymentMethod, setPaymentMethod] = useState('cash'); // default payment method
  const [amountToAdd, setAmountToAdd] = useState('');
  const userId = localStorage.getItem("userId");
  // Function to add money to the wallet
    // Function to fetch balance from the backend
  
  const addMoney = async (amountToAdd) => {
    try {
      const response = await fetch(`http://localhost:4000/bar/pay`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        // calculate the total wallet balance as (balance+amountToAdd)
        body: JSON.stringify({ user_id: userId, amount: amountToAdd,strategy: paymentMethod})
      });
      const data = await response.json();
      console.log(data);
      // fetchBalance();  // Re-fetch balance to update the displayed amount
    } catch (error) {
      console.error('Failed to add money:', error);
    }
    window.alert(`Payment of ${amountToAdd} received. Thank you!`);
  };
  return (
    // payment component
    <div>
      <Navbar />
      <h1 className="text-3xl font-bold underline">User's Bar Order!</h1>
      <label>
        Cash
        <input type="radio" name="paymentMethod" value="cash"
          checked={paymentMethod === 'cash'}
          onChange={() => setPaymentMethod('cash')} />
      </label>
      <label>
        Card
        <input type="radio" name="paymentMethod" value="card"
          checked={paymentMethod === 'card'}
          onChange={() => setPaymentMethod('card')} />
      </label>
      <label>
        UPI
        <input type="radio" name="paymentMethod" value="upi"
          checked={paymentMethod === 'upi'}
          onChange={() => setPaymentMethod('upi')} />
      </label>
      <input
                    type="number"
                    value={amountToAdd}
                    onChange={e => setAmountToAdd(e.target.value)}
                    placeholder="Amount to pay"
                />
      <button onClick={() => addMoney(amountToAdd)}>Pay Bill Amount</button>
      
      
    </div>
  );
}

export default BarOrder;

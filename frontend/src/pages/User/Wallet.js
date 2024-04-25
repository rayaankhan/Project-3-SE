import React, { useState, useEffect } from 'react';
import Navbar from "../../components/Navbar";

// Get the userid from local storage
const userId = localStorage.getItem("userId");

function Wallet() {
    // State to store the balance and the amount to add
    const [balance, setBalance] = useState(0);
    const [amountToAdd, setAmountToAdd] = useState('');
    const [paymentMethod, setPaymentMethod] = useState('cash');  // Default to 'cash'

    // Function to fetch balance from the backend
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
    // function to create wallet
    const createWallet = async () => {
        try {
            const response = await fetch(`http://localhost:5000/wallet/create`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ user_id: userId })
            });
            const data = await response.json();
            console.log(data);
            fetchBalance();  // Re-fetch balance to update the displayed amount
        } catch (error) {
            console.error('Failed to create wallet:', error);
        }
    }

    // Function to add money to the wallet
    const addMoney = async () => {
        try {
            const response = await fetch(`http://localhost:5000/wallet/update`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                // calculate the total wallet balance as (balance+amountToAdd)
                body: JSON.stringify({ user_id: userId, amount: parseInt(balance) + parseInt(amountToAdd) })
                // body: JSON.stringify({ user_id: userId, amount:  })
            });
            const data = await response.json();
            console.log(data);
            fetchBalance();  // Re-fetch balance to update the displayed amount
        } catch (error) {
            console.error('Failed to add money:', error);
        }
    };

    // useEffect hook to call fetchBalance when the component mounts
    useEffect(() => {
        fetchBalance();
    }, []); // The empty array ensures this effect runs only once after the initial render

    return (
        <div>
            <Navbar />
            <h1>Welcome to Wallet</h1>
            <h2>Your wallet balance is: ${balance}</h2>
            <div>
                
                <button onClick={createWallet}>Create Wallet</button>
                <br/>
                <input
                    type="number"
                    value={amountToAdd}
                    onChange={e => setAmountToAdd(e.target.value)}
                    placeholder="Amount to add"
                />
                <div>
                    <label>
                        <input 
                            type="radio" 
                            value="cash" 
                            checked={paymentMethod === 'cash'} 
                            onChange={() => setPaymentMethod('cash')} 
                        /> Cash
                    </label>
                    <label>
                        <input 
                            type="radio" 
                            value="card" 
                            checked={paymentMethod === 'card'} 
                            onChange={() => setPaymentMethod('card')} 
                        /> Card
                    </label>
                    <label>
                        <input 
                            type="radio" 
                            value="upi" 
                            checked={paymentMethod === 'upi'} 
                            onChange={() => setPaymentMethod('upi')} 
                        /> UPI
                    </label>
                </div>
                <button onClick={addMoney}>Add Money</button>
                
            </div>
        </div>
    );
}
export default Wallet;
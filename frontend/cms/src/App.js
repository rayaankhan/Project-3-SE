import logo from './log~o.svg';
import './App.css';
import React from 'react';
import { useEffect, useState } from 'react';

function App() {
  const [message, setMessage] = useState('Loading...');
  useEffect(() => {
    fetch('http://localhost:5000/hello')
      .then(response => response.json())
      .then(data => setMessage(data.message));
  }, []);
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
        <p>{message}</p>
      </header>
    </div>
  );
}

export default App;

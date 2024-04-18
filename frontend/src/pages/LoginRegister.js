import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { CSSTransition } from "react-transition-group";
import "../styles/transition.css";

function LoginRegister() {
  const [isLogin, setIsLogin] = useState(true);

  const toggleForm = () => {
    setIsLogin(!isLogin);
  };

  return (
    <div className="flex min-h-screen bg-gray-100">
      <div
        className="w-3/5 bg-cover bg-center bg-gray-100"
        style={{
          backgroundImage: `url('/images/casino.webp')`,
          boxShadow: "-4px 0 6px 0 white inset",
        }}
      ></div>
      <div className="w-2/5 flex flex-col justify-center items-center px-16">
        {isLogin ? <LoginForm /> : <RegisterForm />}
        <button className="mt-4 text-gray-600" onClick={toggleForm}>
          {isLogin ? "Need an account? Register" : "Already registered? Login"}
        </button>
      </div>
    </div>
  );
}

function LoginForm() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const navigate = useNavigate();
  const handleLogin = async (event) => {
    event.preventDefault();
    console.log("Logging in with:", username, password);
    // Create a user object with form data
    const user = {
      username,
      password,
    };

    try {
      const response = await fetch('http://localhost:5000/users/login', { 
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(user),
      });

      if (!response.ok) {
        // Handle error from backend
        const errorData = await response.json();
        console.error('Login failed:', errorData);
      } else {
        // Login successful
        console.log('User logged in successfully!');
        // set currentTab in local storage or state management
        localStorage.setItem("currentTab", "home");
        // save the user id in local storage
        const userData = await response.json();
        console.log('User data:', userData);
        localStorage.setItem("userId", userData.id);
        localStorage.setItem("userRole", userData.role);
        // navigate to the home page
        navigate("/home");
      }
    } catch (error) {
      console.error('Login error:', error);
    }
  }
  return (
    <form onSubmit={handleLogin} className="w-96">
      <h2 className="text-2xl font-semibold text-gray-700 mb-2">Login</h2>
      <div className="space-y-4">
        <input
          type="text"
          placeholder="Username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          className="w-full p-3 border border-gray-300 rounded-md"
        />
        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          className="w-full p-3 border border-gray-300 rounded-md"
        />
        <button
          type="submit"
          className="w-full bg-blue-500 hover:bg-blue-600 text-white font-semibold p-3 rounded-md"
        >
          Login
        </button>
      </div>
    </form>
  );
}

function RegisterForm() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [email, setEmail] = useState("");
  const [age, setAge] = useState("");
  const navigate = useNavigate();

  const handleRegister = async (event) => {
    event.preventDefault();
    console.log("Registering with:", username, email, age);
    // Create a user object with form data
    const user = {
      username,
      email,
      password,
      age,
    };

    try {
      const response = await fetch('http://localhost:5000/users/add', { 
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(user),
      });

      if (!response.ok) {
        // Handle error from backend
        const errorData = await response.json();
        console.error('Registration failed:', errorData);
      } else {
        // Registration successful
        console.log('User registered successfully!');
        // navigate to the home page
        // set currentTab in local storage or state management
        localStorage.setItem("currentTab", "home");
        navigate("/home");
      }
    } catch (error) {
      console.error('Registration error:', error);
    }
  };
  return (
    <form onSubmit={handleRegister} className="w-96">
      <h2 className="text-2xl font-semibold text-gray-700 mb-2">Register</h2>
      <div className="space-y-4">
        <input
          type="text"
          placeholder="Username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          className="w-full p-3 border border-gray-300 rounded-md"
        />
        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          className="w-full p-3 border border-gray-300 rounded-md"
        />
        <input
          type="email"
          placeholder="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          className="w-full p-3 border border-gray-300 rounded-md"
        />
        <input
          type="number"
          placeholder="Age"
          value={age}
          onChange={(e) => setAge(e.target.value)}
          className="w-full p-3 border border-gray-300 rounded-md"
        />
        <button
          type="submit"
          className="w-full bg-blue-500 hover:bg-blue-600 text-white font-semibold p-3 rounded-md"
        >
          Register
        </button>
      </div>
    </form>
  );
}

// export default LoginRegister;
export {RegisterForm, LoginForm, LoginRegister}

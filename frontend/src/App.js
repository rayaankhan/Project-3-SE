import React from 'react';
import { useState, useEffect } from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import UserHome from './pages/UserHome';
import ManagerHome from './pages/ManagerHome';
import AdminHome from './pages/AdminHome';
import {LoginRegister} from './pages/LoginRegister';
// import PrivateRoute from './components/PrivateRoute';
import UserAnalytics from './pages/UserAnalytics';
import ManagerAnalytics from './pages/ManagerAnalytics';

function App() {
  const [userRole, setUserRole] = useState(null);

  useEffect(() => {
    // Fetch user role from local storage or state management
    const storedRole = localStorage.getItem('userRole');
    setUserRole(storedRole);
  }, []);

  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<LoginRegister />} />
        <Route path="/home" element={userRole === 'admin' ? <AdminHome /> : userRole === 'manager' ? <ManagerHome /> : <UserHome />} />
        <Route path="/analytics" element={userRole === 'user' ? <UserAnalytics />:<ManagerAnalytics />}/>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
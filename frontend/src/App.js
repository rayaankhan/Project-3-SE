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
import CreateCasino from './pages/createCasino/CreateCasino';
import CasinoTypeRouter from './pages/createCasino/CasinoTypeRouter';
import UserCasino from './pages/UserCasino';
import ManagerCasino from './pages/ManagerCasino';
import CasinoInfo from './pages/CasinoInfo';
import GameTableInfo from './pages/GameTableInfo';
import BarInfo from './pages/BarInfo';

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
        <Route path="/create-casino" element={<CreateCasino />} />
        <Route path="/create-casino/customize" element={<CasinoTypeRouter />} />
        <Route path="/casinos" element={userRole === 'manager' ? <ManagerCasino /> : <UserCasino />} />
        <Route path="/casinos/:casinoId" element={<CasinoInfo />} />
        <Route path="/gametable/:gametableId" element={<GameTableInfo />} />
        <Route path="/bar/:barId" element={<BarInfo />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
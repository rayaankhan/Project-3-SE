import React from 'react';
import { useState, useEffect } from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import UserHome from './pages/User/UserHome';
import ManagerHome from './pages/Manager/ManagerHome';
import AdminHome from './pages/AdminHome';
import {LoginRegister} from './pages/LoginRegister';
// import PrivateRoute from './components/PrivateRoute';
import UserAnalytics from './pages/User/UserAnalytics';
import ManagerAnalytics from './pages/Manager/ManagerAnalytics';
import CreateCasino from './pages/Manager/createCasino/CreateCasino';
import CasinoTypeRouter from './pages/Manager/createCasino/CasinoTypeRouter';
import UserCasino from './pages/User/UserCasino';
import ManagerCasino from './pages/Manager/ManagerCasino';
import CasinoInfo from './pages/Manager/CasinoInfo';
import GameTableInfo from './pages/Manager/GameTableInfo';
import BarInfo from './pages/Manager/BarInfo';
import UserCasinoInfo from './pages/User/UserCasinoInfo';
import GameTablePlay from './pages/User/GameTablePlay';
import BarOrder from './pages/User/BarOrder';
import UserNotifications from './pages/User/UserNotifications';
import MCasinoAnalyticInfo from './pages/Manager/MCasinoAnalyticInfo';
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
        <Route path="/analytics" element={userRole === 'manager' ? <ManagerAnalytics />:<UserAnalytics />}/>
        <Route path="/create-casino" element={<CreateCasino />} />
        <Route path="/create-casino/customize" element={<CasinoTypeRouter />} />
        <Route path="/casinos" element={userRole === 'manager' ? <ManagerCasino /> : <UserCasino />} />
        <Route path="/casinos/:casinoId" element={<CasinoInfo />} />
        <Route path="/mcasinosanalytics/:casinoId" element={<MCasinoAnalyticInfo />} />
        <Route path="/gametable/:gametableId" element={<GameTableInfo />} />
        <Route path="/bar/:barId" element={<BarInfo />} />
        <Route path="/user/:casinoId" element={<UserCasinoInfo />} />
        <Route path="/play/gametable/:gametableId" element={<GameTablePlay />} />
        <Route path="/order/bar/:barId" element={<BarOrder />} />
        <Route path="/notifications" element={<UserNotifications />} />

      </Routes>
    </BrowserRouter>
  );
}

export default App;
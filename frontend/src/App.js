import React from 'react';
import { useState, useEffect } from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { useNavigate } from 'react-router-dom'; 
import UserHome from './pages/User/UserHome';
import ManagerHome from './pages/Manager/ManagerHome';
import AdminHome from './pages/AdminHome';
import {LoginRegister} from './pages/LoginRegister';
import ProtectedRoute from './components/ProtectedRoute';
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
import {jwtDecode} from "jwt-decode";


function App() {
  const [userRole, setUserRole] = useState(null);

  useEffect(() => {
    // Fetch user role from local storage or state management
    const token = localStorage.getItem("token")
    if (token) {
      const decoded = jwtDecode(token);
      setUserRole(decoded.role);
    }
  }, []);

  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<LoginRegister />} />
        <Route path='/home' element={<ProtectedRoute element={userRole === 'admin' ? <AdminHome /> : userRole === 'manager' ? <ManagerHome /> : <UserHome />} />} />
        <Route path='/analytics' element={<ProtectedRoute element={userRole === 'user' ? <UserAnalytics />:<ManagerAnalytics />} />} />
        <Route path='/create-casino' element={<ProtectedRoute element={<CreateCasino />} />} />
        <Route path='/create-casino/customize' element={<ProtectedRoute element={<CasinoTypeRouter />} />} />
        <Route path='/casinos' element={<ProtectedRoute element={userRole === 'manager' ? <ManagerCasino /> : <UserCasino />} />} />
        <Route path='/casinos/:casinoId' element={<ProtectedRoute element={<CasinoInfo />} />} />
        <Route path='/gametable/:gametableId' element={<ProtectedRoute element={<GameTableInfo />} />} />
        <Route path='/bar/:barId' element={<ProtectedRoute element={<BarInfo />} />} />
        <Route path='/user/:casinoId' element={<ProtectedRoute element={<UserCasinoInfo />} />} />
        <Route path='/play/gametable/:gametableId' element={<ProtectedRoute element={<GameTablePlay />} />} />
        <Route path='/order/bar/:barId' element={<ProtectedRoute element={<BarOrder />} />} />
        <Route path='/notifications' element={<ProtectedRoute element={<UserNotifications />} />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
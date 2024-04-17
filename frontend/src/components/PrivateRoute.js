import React from 'react';
import { Navigate, Outlet } from 'react-router-dom';

const PrivateRoute = ({ userRole, allowedRoles, children }) => {
  if (!userRole || !allowedRoles.includes(userRole)) {
    alert('You are not authorized to view this page');
    return <Navigate to="/" />;
  }
    return <Outlet />;
}

export default PrivateRoute;
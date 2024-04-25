import React from "react";
import { Route, Navigate } from "react-router-dom";

const ProtectedRoute = ({ element }) => {
  const accessToken = localStorage.getItem("token");
  if (!accessToken) {
  
    return (
    <Navigate to="/" />
    )
  }
  return element;
};

export default ProtectedRoute;
import React from "react";
import Navbar from "../components/Navbar";

function UserHome() {
  return (
    // use tailwind css for styling and making navbar
    <div>
      <Navbar />
      <h1 className="text-3xl font-bold underline">User's Home!</h1>
    </div>
  );
}

export default UserHome;

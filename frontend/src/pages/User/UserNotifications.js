import React from "react";
import { useState, useEffect } from "react";
import Navbar from "../../components/Navbar";

function UserNotifications() {
  const userId = localStorage.getItem("userId");
  const [notifications, setNotifications] = useState([]);

  useEffect(() => {
    async function fetchNotifications() {
      try {
        const response = await fetch("/get_user_notifications", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ userId: userId }),
        });
        if (!response.ok) {
          throw new Error("Failed to fetch notifications");
        }
        const data = await response.json();
        console.log(data.notifications);
        setNotifications(data.notifications);
      } catch (error) {
        console.error("Error fetching notifications:", error);
      }
    }

    fetchNotifications();
  }, [userId]);
  return (
    <div>
      <Navbar />
      <h1 className="text-3xl font-bold underline">User's Notifications!</h1>
      <div className="flex flex-col space-y-4">
        {/* make a table to show notifications, table has 3 columns: message, casinoid. table should have partition lines */}
        {notifications.length > 0 && (
            <table className="table-auto border-collapse w-full">
                <thead>
                <tr>
                    <th className="border border-gray-400 px-4 py-2">Message</th>
                    <th className="border border-gray-400 px-4 py-2">Casino Name</th>
                </tr>
                </thead>
                <tbody>
                {notifications.map((notification, index) => (
                    <tr
                    key={index}
                    className="bg-gray-100 border border-gray-400"
                    >
                    <td className="border border-gray-400 px-4 py-2">
                        {notification.message}
                    </td>
                    <td className="border border-gray-400 px-4 py-2">
                        {notification.casinoname}
                    </td>
                    </tr>
                ))}
                </tbody>
            </table>
        )}

        {notifications.length === 0 && (
          <p className="text-lg font-bold">No notifications to show</p>
        )}
      </div>
    </div>
  );
}

export default UserNotifications;
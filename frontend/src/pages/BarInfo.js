import React, { useState, useEffect } from "react";
import Navbar from "../components/Navbar";
import { useParams } from "react-router-dom";

function BarInfo() {
  const { barId } = useParams();
  const [staffId, setStaffId] = useState("");
  const [drinks, setDrinks] = useState("");
  const [availStaff, setAvailStaff] = useState([]);
  const [selectedStaffId, setSelectedStaffId] = useState("");
  const managerId = localStorage.getItem("userId");

  useEffect(() => {
    async function fetchAvailStaff() {
      try {
        const response = await fetch("/avail_staff", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            managerId: managerId,
          }),
        });
        if (!response.ok) {
          throw new Error("Failed to fetch available staff");
        }
        const data = await response.json();
        // console.log("Data received:", data); // Log the received data
        setAvailStaff(data.avail_staff);
      } catch (error) {
        console.error("Error fetching available staff:", error);
      }
    }
  
    fetchAvailStaff();
  }, [managerId]);


  useEffect(() => {
    async function fetchBarInfo() {
      try {
        const response = await fetch("/bar_info", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            managerId: managerId,
            barId: barId,
          }),
        });
        if (!response.ok) {
          throw new Error("Failed to fetch bar info");
        }
        const data = await response.json();
        const barInfo = JSON.parse(data.bar_info);
        // console.log("Data received:", barInfo); // Log the received data
        setStaffId(barInfo.staffid);
        setDrinks(barInfo.drinks);
      } catch (error) {
        console.error("Error fetching bar info:", error);
      }
    }
  
    fetchBarInfo();
  }, [managerId, barId]);

  // Function to handle selection of staff member
  const handleStaffSelection = (event) => {
    setSelectedStaffId(event.target.value);
  };

  // Function to handle form submission
  const handleFormSubmit = async (event) => {
    event.preventDefault();
    console.log("Selected staff ID:", selectedStaffId);
    try {
      const response = await fetch("/update_bar_staff", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          managerId: managerId,
          barId: barId,
          staffId: selectedStaffId,
        }),
      });
      if (!response.ok) {
        throw new Error("Failed to update staff");
      }
      // Optionally, you can fetch the updated game table info here
    } catch (error) {
      console.error("Error updating staff:", error);
    }
  };
  

  return (
    <div>
      <Navbar />
      <table className="casino-table">
        <thead>
          <tr>
            <th>Staff ID</th>
            <th>Drinks</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>{staffId}</td>
            <td>{drinks}</td>
          </tr>
        </tbody>
      </table>
      <div className="container mt-4">
  <div className="row justify-content-center">
    <div className="col-lg-6">
      <div className="card p-3">
        <form onSubmit={handleFormSubmit}>
          <div className="mb-3">
            <label htmlFor="staffSelect" className="form-label">Select New Staff</label>
            <select id="staffSelect" value={selectedStaffId} onChange={handleStaffSelection} className="form-select">
              <option value="">Select...</option>
              {availStaff.map((staffId) => (
                <option key={staffId} value={staffId}>
                  Staff ID: {staffId}
                </option>
              ))}
            </select>
          </div>
          <button type="submit" className="btn btn-primary btn-sm">Submit</button>
        </form>
      </div>
    </div>
  </div>
</div>
    </div>
  );
}

export default BarInfo;

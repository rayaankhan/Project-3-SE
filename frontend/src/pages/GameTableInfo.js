import React, { useState, useEffect } from "react";
import Navbar from "../components/Navbar";
import { useParams } from "react-router-dom";

function GameTableInfo() {
  const { gametableId } = useParams();
  const [staffId, setStaffId] = useState("");
  const [prob, setProb] = useState("");
  const [type, setType] = useState("");
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
    async function fetchGameTableInfo() {
      try {
        const response = await fetch("/gametable_info", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            managerId: managerId,
            gametableId: gametableId,
          }),
        });
        if (!response.ok) {
          throw new Error("Failed to fetch game table info");
        }
        const data = await response.json();
        // console.log("Data received:", data); // Log the received data
        const gametableInfo = JSON.parse(data.gametable_info);
        setStaffId(gametableInfo.staffid);
        setProb(gametableInfo.prob);
        setType(gametableInfo.type);
      } catch (error) {
        console.error("Error fetching game table info:", error);
      }
    }
  
    fetchGameTableInfo();
  }, [managerId, gametableId]);

  // Function to handle selection of staff member
  const handleStaffSelection = (event) => {
    setSelectedStaffId(event.target.value);
  };

  // Function to handle form submission
  const handleFormSubmit = async (event) => {
    event.preventDefault();
    console.log("Selected staff ID:", selectedStaffId);
    try {
      const response = await fetch("/update_gametable_staff", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          managerId: managerId,
          gametableId: gametableId,
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
            <th>Probability</th>
            <th>Type</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>{staffId}</td>
            <td>{prob}</td>
            <td>{type}</td>
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

export default GameTableInfo;

import React, { useState, useEffect } from "react";
import Navbar from "../../components/Navbar";
import { useParams } from "react-router-dom";

function GameTableInfo() {
  const { gametableId } = useParams();
  const [staffId, setStaffId] = useState("");
  const [staffName, setStaffName] = useState("");
  const [prob, setProb] = useState("");
  const [type, setType] = useState("");
  const [availStaffId, setAvailStaffId] = useState([]);
  const [availStaffName, setAvailStaffName] = useState([]);
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
        setAvailStaffId(data.avail_staff.staffid);
        setAvailStaffName(data.avail_staff.staffname);
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
        setStaffName(gametableInfo.staffname);
      } catch (error) {
        console.error("Error fetching game table info:", error);
      }
    }

    fetchGameTableInfo();
  }, [managerId, gametableId]);

  // Function to handle selection of staff member
  const handleStaffSelection = (event) => {
    for(let i = 0; i < availStaffName.length; i++) {
      if(availStaffName[i] === event.target.value) {
        setSelectedStaffId(availStaffId[i]);
        break;
      }
    }
    console.log("Selected staff ID:", selectedStaffId);
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
          oldStaffId: staffId,
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

  const handleDelete = async () => {
    try {
      const response = await fetch("/delete_gametable", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ gametableId: gametableId }),
      });
      if (!response.ok) {
        throw new Error("Failed to delete gametable");
      }
      console.log("deleted");
    } catch (error) {
      console.error("Error handling the button", error);
    }
  };

  return (
    <div>
      <Navbar />
      <table className="casino-table">
        <thead>
          <tr>
            <th>Staff Name</th>
            <th>Probability</th>
            <th>Type</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>{staffName}</td>
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
                  <label htmlFor="staffSelect" className="form-label">
                    Select New Staff
                  </label>
                  <select
                    id="staffSelect"
                    defaultValue={selectedStaffId}
                    onChange={handleStaffSelection}
                    className="form-select"
                  >
                    <option value="">Select...</option>
                    {availStaffName.map((staffName) => (
                      <option value={staffName}>{staffName}</option>
                    ))}
                  </select>
                </div>
                <button type="submit" className="btn btn-primary btn-sm">
                  Submit
                </button>
              </form>
            </div>
          </div>
        </div>
      </div>
      <div>
        <button onClick={handleDelete} className="btn btn-primary">
          Delete GameTable
        </button>
      </div>
    </div>
  );
}

export default GameTableInfo;

import React, { useState, useEffect } from "react";
import Navbar from "../../components/Navbar";
import { useParams } from "react-router-dom";

function BarInfo() {
  const { barId } = useParams();
  const [staffId, setStaffId] = useState("");
  const [drinks, setDrinks] = useState("");
  const [availStaffId, setAvailStaffId] = useState([]);
  const [availStaffName, setAvailStaffName] = useState([]);
  const [selectedStaffId, setSelectedStaffId] = useState("");
  const managerId = localStorage.getItem("userId");
  const [barName, setBarName] = useState("");
  const [staffname, setStaffName] = useState("");

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
        setBarName(barInfo.name);
        setStaffId(barInfo.staffid);
        setStaffName(barInfo.staffname);
        setDrinks(barInfo.drinks);
      } catch (error) {
        console.error("Error fetching bar info:", error);
      }
    }

    fetchBarInfo();
  }, [managerId, barId]);

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
      const response = await fetch("/update_bar_staff", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          managerId: managerId,
          barId: barId,
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
      const response = await fetch("/delete_bar", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ barId: barId }),
      });
      if (!response.ok) {
        throw new Error("Failed to delete bar");
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
            <th>Bar Name</th>
            <th>Staff ID</th>
            <th>Drinks</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>{barName}</td>
            <td>{staffname}</td>
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

export default BarInfo;

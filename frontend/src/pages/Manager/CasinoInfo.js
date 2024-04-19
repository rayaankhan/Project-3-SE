import React, { useState, useEffect } from "react";
import Navbar from "../../components/Navbar";
import { useParams, useNavigate } from "react-router-dom";
import "../../styles/form.css";
import "../../styles/notification.css";

function CasinoInfo() {
  const { casinoId } = useParams();
  const casinoType = casinoId[6];
  let allowedTables = [];
  // console.log("casinoType", casinoType)
  if(casinoType === "A"){
    allowedTables = ['A', 'C']
  }
  else if(casinoType === "B"){
    allowedTables = ['A', 'B']
  }
  else if(casinoType === "C"){
    allowedTables = ['C', 'D']
  }
  else if(casinoType === "D"){
    allowedTables = ['B', 'D']
  }
  console.log("allowedTables", allowedTables)
  const [tokencounterid, setTokencounterid] = useState("");
  const [gametableid, setGametableid] = useState([
    [], // gametableA_list
    [], // gametableB_list
    [], // gametableC_list
    [], // gametableD_list
  ]);

  const [gametablename, setGametablename] = useState([
    [], // gametableA_list
    [], // gametableB_list
    [], // gametableC_list
    [], // gametableD_list
  ]);
  const [barid, setBarid] = useState([]);
  const [barname, setBarname] = useState([]);
  const [gameTables, setGameTables] = useState({
    A: [],
    B: [],
    C: [],
    D: [],
  });
  const [staffFormData, setStaffFormData] = useState({
    Name: "",
    Salary: 0,
  });
  const managerId = localStorage.getItem("userId");

  useEffect(() => {
    async function fetchCasinos() {
      try {
        const response = await fetch("/casino_info", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ managerId: managerId, casinoId: casinoId }),
        });
        if (!response.ok) {
          throw new Error("Failed to fetch casinos");
        }
        const data = await response.json();
        setGametableid(data.casino_info.table_id_list);
        setBarid(data.casino_info.bar_id_list);
        setTokencounterid(data.casino_info.tokencounterid);

        setGametablename(data.casino_info.table_name_list);
        setBarname(data.casino_info.bar_name_list);
      } catch (error) {
        console.error("Error fetching casinos:", error);
      }
    }

    fetchCasinos();
  }, [managerId, casinoId]);

  useEffect(() => {
    const [gameTableA, gameTableB, gameTableC, gameTableD] = gametablename;
    setGameTables({
      A: gameTableA,
      B: gameTableB,
      C: gameTableC,
      D: gameTableD,
    });
  }, [gametableid]);

  // Filter out empty gameTables
  const nonEmptyGameTables = Object.fromEntries(
    Object.entries(gameTables).filter(([key, value]) => value.length > 0)
  );

  const gameTableTypes = Object.keys(nonEmptyGameTables);

  const navigate = useNavigate();

  const handleGameTableClick = (clickedgametablename) => {
    let row_idx = 0;
    let column_idx = 0;
    for (let i = 0; i < gametablename.length; i++) {
      const row = gametablename[i];
      for (let j = 0; j < row.length; j++) {
        if (row[j] === clickedgametablename) {
          row_idx = i;
          column_idx = j;
        }
      }
    }
    // console.log()
    let clickedgametableid = gametableid[row_idx][column_idx];
    navigate("/gametable/" + clickedgametableid);
  };

  const handleBarClick = (barname) => {
    // Add logic for handling cell click here
    let idx = 0;
    for (let i = 0; i < barname.length; i++) {
      if (barname[i] === barname) {
        idx = i;
      }
    }
    let clickedbarid = barid[idx];
    navigate("/bar/" + clickedbarid);
  };

  const handleTokenCounterClick = (value) => {
    // Add logic for handling cell click here
    // navigate("/tokencounter/" + value)
  };

  const [formData, setFormData] = useState({
    A: 0,
    B: 0,
    C: 0,
    D: 0,
    bar: 0,
    casinoId: casinoId,
  });

  const handleChange = (event, type) => {
    const { value } = event.target;
    setFormData({ ...formData, [type]: value });
  };

  const handleFormSubmit = async (event) => {
    event.preventDefault();
    try {
      const response = await fetch("/add_gametable_bar", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(formData),
      });
      if (!response.ok) {
        throw new Error("Failed to submit form data");
      }
      console.log(response.data);
      // Handle successful response if needed
      console.log("Form data submitted successfully");
    } catch (error) {
      console.error("Error submitting form data:", error);
    }
  };

  const handleDelete = async () => {
    try {
      const response = await fetch("/delete_casino", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ casinoId: casinoId }),
      });
      if (!response.ok) {
        throw new Error("Failed to delete casino");
      }
      console.log("deleted");
    } catch (error) {
      console.error("Error handling the button", error);
    }
  };

  const handleStaffChange = (event, type) => {
    const { value } = event.target;
    setStaffFormData({ ...staffFormData, [type]: value });
  };

  const handleStaffFormSubmit = async (event) => {
    event.preventDefault();
    try {
      console.log(staffFormData);
      const response = await fetch("/add_staff", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(staffFormData),
      });
      if (!response.ok) {
        throw new Error("Failed to submit form data");
      }
      const data = await response.json();
      console.log(data);
      // Handle successful response if needed
      console.log("Form data submitted successfully");
    } catch (error) {
      console.error("Error submitting form data:", error);
    }
  };

  const [text, setText] = useState('');

  const handleNotificationChange = (event) => {
    setText(event.target.value);
  };

  const handleNotifyClick = async () => {
    try {
      const response = await fetch("/notify", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          casinoId: casinoId,
          text: text,
          managerId: managerId,
        }),
      });
      if (!response.ok) {
        throw new Error("Failed to submit form data");
      }
      const data = await response.json();
      console.log(data);
      // Handle successful response if needed
      console.log("Notified successfully");
    } catch (error) {
      console.error("Error notifying:", error);
    }
  };

  return (
    <div>
      <Navbar />
      <table className="casino-table">
        <thead>
          <tr>
            {Object.keys(nonEmptyGameTables).map((key, index) => (
              <th key={index}>gameTable{key}</th>
            ))}
          </tr>
        </thead>
        <tbody>
          {Array.from({
            length: Math.max(
              ...Object.values(nonEmptyGameTables).map((arr) => arr.length)
            ),
          }).map((_, rowIndex) => (
            <tr key={rowIndex}>
              {Object.values(nonEmptyGameTables).map(
                (gameTable, columnIndex) => (
                  <td key={columnIndex}>
                    {gameTable[rowIndex] && (
                      <button
                        onClick={() => {
                          handleGameTableClick(gameTable[rowIndex]);
                        }}
                      >
                        {gameTable[rowIndex]}
                      </button>
                    )}
                  </td>
                )
              )}
            </tr>
          ))}
        </tbody>
      </table>
      <div>
        <table className="casino-table">
          <thead>
            <tr>
              <th>Bars</th>
            </tr>
          </thead>
          <tbody>
            {barname.map((id, index) => (
              <tr key={index}>
                <td>
                  <button onClick={() => handleBarClick(id)}> {id}</button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
      <div>
        <table className="casino-table">
          <thead>
            <tr>
              <th>TokenCounter</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>
                <button onClick={() => handleTokenCounterClick(tokencounterid)}>
                  {" "}
                  {tokencounterid}
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
      <div className="notification-div">
  <input
    type="text"
    value={text}
    onChange={handleNotificationChange}
    placeholder="Enter your notification here"
    className="notification-input"
  />
  <button onClick={handleNotifyClick} className="notify-button">
    Notify
  </button>
</div>

      <div className="container">
        <form onSubmit={handleFormSubmit} className="form">
          <h2 className="form-heading">How many more tables/bars you need?</h2>
          {allowedTables.map((type, index) => (
            <div key={index} className="form-group">
              <label htmlFor={`gameTable${type}`} className="form-label">
                GameTable{type}:{" "}
              </label>
              <input
                type="number"
                id={type}
                name={type}
                min="0"
                className="form-input"
                onChange={(event) => handleChange(event, type)}
                defaultValue={0}
                required
              />
            </div>
          ))}
          <div className="form-group">
            <label htmlFor={`bar`} className="form-label">
              Bar:{" "}
            </label>
            <input
              type="number"
              id={`bar`}
              name={`bar`}
              min="0"
              className="form-input"
              onChange={(event) => handleChange(event, "bar")}
              defaultValue={0}
              required
            />
          </div>
          <button type="submit" className="btn">
            Submit
          </button>
        </form>

        <form onSubmit={handleStaffFormSubmit} className="form">
          <h2 className="form-heading">Add New Staff</h2>
          <div className="form-group">
            <label htmlFor={`Name`} className="form-label">
              Name{" "}
            </label>
            <input
              type="text"
              id={`Name`}
              name={`Name`}
              className="form-input"
              onChange={(event) => handleStaffChange(event, "Name")}
              required
            />
            <label htmlFor={`Salary`} className="form-label">
              Salary{" "}
            </label>
            <input
              type="number"
              id={`Salary`}
              name={`Salary`}
              min="0"
              className="form-input"
              onChange={(event) => handleStaffChange(event, "Salary")}
              defaultValue={0}
              required
            />
          </div>
          <button type="submit" className="btn">
            Submit
          </button>
        </form>
      </div>
      <div>
        <button onClick={handleDelete} className="btn btn-primary">
          Delete Casino
        </button>
      </div>
    </div>
  );
}

export default CasinoInfo;

import React, { useState, useEffect } from "react";
import Navbar from "../../components/Navbar";
import { useParams, useNavigate } from "react-router-dom";

function UserCasinoInfo() {
  const { casinoId } = useParams();
  const userId = localStorage.getItem("userId");
  const [subscribe, setSubscribe] = useState("Subscribe");
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
  const [tokencounterid, setTokencounterid] = useState("");
  const [gameTables, setGameTables] = useState({
    A: [],
    B: [],
    C: [],
    D: [],
  });

  useEffect(() => {
    async function fetchCasinos() {
      try {
        const response = await fetch("/check_subscription", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ userId: userId, casinoId: casinoId }),
        });
        if (!response.ok) {
          throw new Error("Failed to fetch casinos");
        }
        const data = await response.json();
        if(data.status === "subscribed"){
          setSubscribe("unsubscribe");
        }
        else{
          setSubscribe("subscribe");
        }
      } catch (error) {
        console.error("Error fetching casinos:", error);
      }
    }

    fetchCasinos();
  }, [userId, casinoId]);



  useEffect(() => {
    async function fetchCasinos() {
      try {
        const response = await fetch("/casino_info", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ userId: userId, casinoId: casinoId }),
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
  }, [userId, casinoId]);

  useEffect(() => {
    const [gameTableA, gameTableB, gameTableC, gameTableD] = gametablename;
    setGameTables({
      A: gameTableA,
      B: gameTableB,
      C: gameTableC,
      D: gameTableD,
    });
    console.log("Game tables:", gameTables);
  }, [gametableid]);

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
    navigate("/play/gametable/" + clickedgametableid);
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
    navigate("/order/bar/" + clickedbarid);
  };

  const handleSubscribeClick = async () => {
    console.log("Subscribe clicked", userId, casinoId);
    try {
      const response = await fetch("/subscribe", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ userId: userId, casinoId: casinoId }),
      });
      if (!response.ok) {
        throw new Error("Failed to fetch casinos");
      }
      const data = await response.json();
      if(data.status === "subscribed"){
        alert("Subscribed successfully");
        setSubscribe("unsubscribe");
      }
      else{
        alert("Unsubscribed");
        setSubscribe("subscribe");
      }
    } catch (error) {
      console.error("Error fetching casinos:", error);
    }
  };

  return (
    <div>
      <Navbar />
      <h1 className="text-3xl font-bold underline">
        See all the gametbles and bar and subscribe
      </h1>
      <table className="casino-table">
        <thead>
          <tr>
            <th>TABLE-A</th>
            <th>TABLE-B</th>
            <th>TABLE-C</th>
            <th>TABLE-D</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            {[0, 1, 2, 3].map((columnIndex) => (
              <td key={columnIndex}>
                <ol>
                  {gametablename
                    .reduce((acc, gametableList) => {
                      return acc.concat(
                        gametableList.filter((gametable) =>
                          gametable.startsWith(
                            `GameTable${String.fromCharCode(65 + columnIndex)}-`
                          )
                        )
                      );
                    }, [])
                    .map((gametable, index) => {
                      const casinoId = gametableid[columnIndex][index];
                      return (
                        <li key={casinoId}>
                          <button
                            onClick={() => handleGameTableClick(casinoId)}
                          >
                            {/* {casino} (Index: {casinoIndex}) */}
                            {gametable}
                          </button>
                        </li>
                      );
                    })}
                </ol>
              </td>
            ))}
          </tr>
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
        <button
          type="button"
          className="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-4 py-2 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
          onClick={() => handleSubscribeClick()}
        >
          {subscribe}
        </button>
      </div>
    </div>
  );
}

export default UserCasinoInfo;
import React, { useState, useEffect } from "react";
import Navbar from "../../components/Navbar";
import "../../styles/managerCasinos.css";
import { useNavigate } from "react-router-dom";

function ManagerCasino() {
  const navigate = useNavigate();
  const [casinosid, setCasinosid] = useState([
    [], // casinoA_list
    [], // casinoB_list
    [], // casinoC_list
    [], // casinoD_list
  ]);
  const [casinosname, setCasinosname] = useState([
    [], // casinoA_list
    [], // casinoB_list
    [], // casinoC_list
    [], // casinoD_list
  ]);
  let managerId = localStorage.getItem("userId");

  useEffect(() => {
    async function fetchCasinos() {
      try {
        const response = await fetch("/manager_casinos", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ managerId: managerId }),
        });
        if (!response.ok) {
          throw new Error("Failed to fetch casinos");
        }
        const data = await response.json();
        // console.log(data.casino_list)
        setCasinosid(data.casino_id_list);
        setCasinosname(data.casino_name_list);
      } catch (error) {
        console.error("Error fetching casinos:", error);
      }
    }

    fetchCasinos();
  }, [managerId]); // Empty dependency array ensures the effect runs only once

  useEffect(() => {
    console.log("Updated casinos name:", casinosname[0]);
    console.log("Updated casinos id:", casinosid[0]);
  }, [casinosid, casinosname]); // Log updated casinos whenever the state changes

  const [currentTab, setCurrentTab] = useState("home");

  const handleClick = (tab) => {
    setCurrentTab(tab);
    // Store the current tab in local storage
    localStorage.setItem("currentTab", tab);
    navigate("/create-casino");
  };

  const handleCasinoClick = (casinoId) => {
    navigate(`/casinos/${casinoId}`);
  };
  return (
    <div>
      <Navbar />
      <h1 className="text-3xl font-bold underline">Manager's Casino Page!</h1>
      <table className="casino-table">
        <thead>
          <tr>
            <th>casinoA</th>
            <th>casinoB</th>
            <th>casinoC</th>
            <th>casinoD</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            {[0, 1, 2, 3].map((columnIndex) => (
              <td key={columnIndex}>
                <ol>
                  {casinosname
                    .reduce((acc, casinoList) => {
                      {
                        /* console.log("casinoList:", casinoList); */
                      }
                      return acc.concat(
                        casinoList.filter((casino) =>
                          casino.startsWith(
                            `Casino${String.fromCharCode(65 + columnIndex)}-`
                          )
                        )
                      );
                    }, [])
                    .map((casino, index) => {
                      const casinoId = casinosid[columnIndex][index];
                      return (
                        <li key={casinoId}>
                          <button onClick={() => handleCasinoClick(casinoId)}>
                            {/* {casino} (Index: {casinoIndex}) */}
                            {casino}
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
      <button
        type="button"
        className="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-4 py-2 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
        onClick={() => handleClick("casino_addition")}
      >
        Create Casino
      </button>
    </div>
  );
}

export default ManagerCasino;

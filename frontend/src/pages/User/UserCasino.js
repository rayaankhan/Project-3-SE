import React, { useState, useEffect } from "react";
import Navbar from "../../components/Navbar";
import { useNavigate } from "react-router-dom";

function UserCasino() {

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
  let userId = localStorage.getItem("userId");

  useEffect(() => {
    async function fetchCasinos() {
      try {
        const response = await fetch("/all_casinos", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ userId: userId }),
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
  }, [userId]); // Empty dependency array ensures the effect runs only once

  useEffect(() => {
    console.log("Updated casinos name:", casinosname[0]);
    console.log("Updated casinos id:", casinosid[0]);
  }, [casinosid, casinosname]); // Log updated casinos whenever the state changes

  const [currentTab, setCurrentTab] = useState("home");

  const handleCasinoClick = (casinoId) => {
    navigate(`/user/${casinoId}`);
  };
  return (
    <div>
      <Navbar />
      <h1 className="text-3xl font-bold underline">User's Casino Page!</h1>
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
    </div>
  );
}

export default UserCasino;

import React, { useState, useEffect } from "react";
import Navbar from "../../components/Navbar";
import { useParams, useNavigate } from "react-router-dom";
import "../../styles/form.css";
import "../../styles/notification.css";
import { Bar } from 'react-chartjs-2';
import { Chart as ChartJS } from 'chart.js/auto';
import Slider from 'react-slick';


function MCasinoAnalyticInfo() {
  const { casinoId } = useParams();
  const managerId = localStorage.getItem("userId");
  const navigate = useNavigate();
  const [tableData, setTableData] = useState([]);
  const [gameTables, setGameTables] = useState([]);
  const [tableInfo,setTableInfo]= useState([]);
  const [tokencounterid, setTokencounterid] = useState("");
  useEffect(() => {
    async function fetchData() {
      try {
        const response = await fetch("/gametable_analytics", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
    
          body: JSON.stringify({ gameTables: gameTables}),
        });
        if (!response.ok) {
          throw new Error("Failed to fetch data");
        }
        const data = await response.json();
        // console.log("data:",data);
        const modifiedTableInfo = data.gametable_info_list.map((tableInfo) => {
          const datetimeParts = tableInfo.datetime.split(" ");
          const date = datetimeParts[0];
          const time = datetimeParts[1];
          return {
            ...tableInfo,
            date,
            time
          };
        });
        setTableInfo(modifiedTableInfo); // Set the received data from the backend to the tableInfo state variable
        // console.log("modi_info:",modifiedTableInfo)
        // Process the data received from the backend

        const tableNetAmounts = {};
        modifiedTableInfo.forEach((tableInfo) => {
          // console.log("tableInfo:",tableInfo)
          const { gametablename, date, amount } = tableInfo;
          // console.log("vals:",gametablename,date,amount)
          if (gametablename in tableNetAmounts) {
            if (date in tableNetAmounts[gametablename]) {
              tableNetAmounts[gametablename][date] += amount;
            } else {
              tableNetAmounts[gametablename][date] = amount;
            }
          } else {
            tableNetAmounts[gametablename] = { [date]: amount };
          }
        });
        // console.log("tableNetAmounts:",tableNetAmounts);
        const sortedTableNetAmounts = Object.entries(tableNetAmounts).map(([gametablename, netAmounts]) =>({
            gametablename,
            netAmounts: Object.entries(netAmounts).sort((a,b)=>new Date(a[0])-new Date(b[0])),
          }));
        console.log("sorted:",sortedTableNetAmounts);
        // sortedTableNetAmounts.sort((a,b)=>a.tablename.localeCompare(b.tablename));
        // console.log("sorted:",sortedTableNetAmounts);
        setTableData(sortedTableNetAmounts);
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    }

    fetchData();
  }, [gameTables]);



  useEffect(() => {
    async function fetchData() {
      try {
        const response = await fetch("/casino_info", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ managerId, casinoId }),
        });
        if (!response.ok) {
          throw new Error("Failed to fetch casino information");
        }
        const data = await response.json();
        setGameTables(data.casino_info.table_name_list.flat());
        setTokencounterid(data.casino_info.tokencounterid);
      } catch (error) {
        console.error("Error fetching casino information:", error);
      }
    }

    fetchData();
  }, [managerId, casinoId]);
  const sliderSettings = {
    dots: true,
    infinite: false,
    speed: 500,
    slidesToShow: 1,
    slidesToScroll: 1,
    adaptiveHeight: true
  };

  const getChartData = (netAmounts) => {
    return {
      labels: netAmounts.map(([date]) => date),
      datasets: [
        {
          label: 'Net Amount',
          data: netAmounts.map(([date, amount]) => amount),
          backgroundColor: 'rgba(255, 99, 132, 0.5)',
          borderColor: 'rgba(255, 99, 132, 1)',
          borderWidth: 1,
        }
      ]
    };
  };

  return (
    <div>
      <Navbar />
      <h1 className="text-3xl font-bold underline">Casino Information</h1>

      <div className="list-container">
        <h2 className="text-xl font-bold mb-4">Game Tables:</h2>
        <ul>
          {gameTables.map((tableName, index) => (
            <li key={index}>
              {tableName}
            </li>
          ))}
        </ul>
      </div>

      <div className="slider-container" style={{ width: '100%', marginTop: '2rem' }}>
        <Slider {...sliderSettings}>
          {tableData.map((table) => (
            <div key={table.tablename}>
              <h3>{table.tablename}</h3>
              <Bar
                data={getChartData(table.netAmounts)}
                options={{
                  scales: {
                    y: {
                      beginAtZero: true
                    }
                  },
                  plugins: {
                    legend: {
                      display: false
                    },
                    title: {
                      display: true,
                      text: `Net Amounts for ${table.gametablename}`
                    }
                  }
                }}
              />
            </div>
          ))}
        </Slider>
      </div>
    </div>
  );
}

export default MCasinoAnalyticInfo;
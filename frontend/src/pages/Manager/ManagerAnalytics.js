import React, { useState, useEffect } from 'react';
import Navbar from '../../components/Navbar';
import '../../styles/managerCasinos.css';
import { useNavigate } from 'react-router-dom';
import { Bar } from 'react-chartjs-2';
import { Chart as ChartJS } from 'chart.js/auto';
import Slider from 'react-slick';

function ManagerAnalytics() {
  const navigate = useNavigate();
  const [casinos, setCasinos] = useState([]);
  const [casinoInfo, setCasinoInfo] = useState([]);
  const [casinoData, setCasinoData] = useState([]);
  useEffect(() => {
    async function fetchData() {
      try {
        const response = await fetch("/casino_analytics", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${localStorage.getItem("token")}`,
          },
    
          body: JSON.stringify({casinos: casinos}),
        });
        if (!response.ok) {
          throw new Error("Failed to fetch data");
        }
        const data = await response.json();
        const modifiedCasinoInfo = data.casino_info_list.map((casinoInfo) => {
          const datetimeParts = casinoInfo.datetime.split(" ");
          const date = datetimeParts[0];
          const time = datetimeParts[1];
          return {
            ...casinoInfo,
            date,
            time
          };
        });

        setCasinoInfo(modifiedCasinoInfo);
        // console.log(modifiedCasinoInfo)
        // Create a dictionary to store the net amount for each date
        const casinoNetAmounts = {};

        // Iterate through the modifiedCasinoInfo array
        modifiedCasinoInfo.forEach((casinoInfo) => {
          const { casinoname, date, amount } = casinoInfo;

          // Check if the casinoname already exists in the dictionary
          if (casinoname in casinoNetAmounts) {
            // Check if the date already exists for the casinoname
            if (date in casinoNetAmounts[casinoname]) {
              // Add the amount to the existing date
              casinoNetAmounts[casinoname][date] += amount;
            } else {
              // Create a new entry for the date and set the amount
              casinoNetAmounts[casinoname][date] = amount;
            }
          } else {
            // Create a new entry for the casinoname and date
            casinoNetAmounts[casinoname] = { [date]: amount };
          }
        });

        // Sort the casinoNetAmounts dictionary based on the dates
        const sortedCasinoNetAmounts = Object.entries(casinoNetAmounts).map(([casinoname, netAmounts]) => ({
          casinoname,
          netAmounts: Object.entries(netAmounts).sort((a, b) => new Date(a[0]) - new Date(b[0])),
        }));

        // Sort the sortedCasinoNetAmounts array based on the casinoname
        sortedCasinoNetAmounts.sort((a, b) => a.casinoname.localeCompare(b.casinoname));
        
        console.log(sortedCasinoNetAmounts);
        setCasinoData(sortedCasinoNetAmounts);
        
        // Process the data received from the backend
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    }

    fetchData();
  }, [casinos]);


  useEffect(() => {
    async function fetchCasinos() {
      try {
        const response = await fetch("/manager_casinos", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${localStorage.getItem("token")}`,
          },
          body: JSON.stringify({}),
        });
        if (!response.ok) {
          throw new Error("Failed to fetch casinos");
        }
        const data = await response.json();
        // console.log("Casino data:", data);
        const flattenedCasinos = data.casino_id_list.flat().map((id, index) => ({
          id,
          name: data.casino_name_list.flat()[index]
        }));
        setCasinos(flattenedCasinos);
      } catch (error) {
        console.error("Error fetching casinos:", error);
      }
    }

    fetchCasinos();
  }, []);
  const handleCasinoClick = (casinoId) => {
    navigate(`/mcasinosanalytics/${casinoId}`);
  };
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
          backgroundColor: 'rgba(255, 99, 132, 0.5)'
        }
      ]
    };
  };


  return (
    <div>
      <Navbar />
      <h1 className="text-3xl font-bold underline">Manager's Casino Page!</h1>
      <div className="casinos-list">
        <h2 className="text-xl font-bold mb-4">List of Casinos:</h2>
        <ul>
          {casinos.map((casino) => (
            <li key={casino.id}>
              <button onClick={() => handleCasinoClick(casino.id)}>
                {casino.name}
              </button>
            </li>
          ))}
        </ul>
      </div>
      <div className="slider-container">
        <Slider {...sliderSettings}>
          {casinoData.map((casino) => (
            <div key={casino.casinoname}>
              <h3>{casino.casinoname}</h3>
              <Bar
                data={getChartData(casino.netAmounts)}
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
                      text: `Net Amounts for ${casino.casinoname}`
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

export default ManagerAnalytics;
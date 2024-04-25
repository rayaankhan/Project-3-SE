import React, { useState, useEffect } from 'react';
import Navbar from '../../components/Navbar';
import '../../styles/managerCasinos.css';
import { useNavigate } from 'react-router-dom';
import { Bar } from 'react-chartjs-2';
import { Chart as ChartJS } from 'chart.js/auto';
import Slider from 'react-slick';

function UserAnalytics() {
  const navigate = useNavigate();
  const [casinos, setCasinos] = useState([]);
  const [casinoInfo, setCasinoInfo] = useState([]);
  const [casinoData, setCasinoData] = useState([]);
  let userId = localStorage.getItem('userId');
  useEffect(() => {
    async function fetchCasinos() {
      console.log("HOI!!!!")
      try {
        const response = await fetch("/user_casinos", {
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
        console.log("Casinos of User data:", data);
        const modifiedCasinoInfo = data
        // const modifiedCasinoInfo = data.casinos.map((casinoInfo) => {
        //   const datetimeParts = casinoInfo.datetime.split(" ");
        //   const date = datetimeParts[0];
        //   const time = datetimeParts[1];
        //   return {
        //     ...casinoInfo,
        //     date,
        //     time
        //   };
        // }
        setCasinoInfo(data.casinos);

        const casinoNetAmounts = {};
        modifiedCasinoInfo.forEach((casinoInfo) => {
          const { casinoname, date, amount } = casinoInfo;
          if (casinoname in casinoNetAmounts) {
            if (date in casinoNetAmounts[casinoname]) {
              casinoNetAmounts[casinoname][date] += amount;
            } else {
              casinoNetAmounts[casinoname][date] = amount;
            }
          } else {
            casinoNetAmounts[casinoname] = { [date]: amount };
          }
        });
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
        console.error("Error fetching casinos:", error);
      }
    }

    fetchCasinos();
  }, [userId]);


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

  const sliderSettings = {
    dots: true,
    infinite: false,
    speed: 500,
    slidesToShow: 1,
    slidesToScroll: 1,
    adaptiveHeight: true
  };
  return (
    <div>
      <Navbar />
      <h1 className="text-3xl font-bold underline">User's Casino Page!</h1>
      <div className="casinos-list">
        <h2 className="text-xl font-bold mb-4">List of Casinos:</h2>
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

export default UserAnalytics;
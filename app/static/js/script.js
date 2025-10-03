document.addEventListener("DOMContentLoaded", () => {
  const uploadForm = document.getElementById("upload-form");
  const imageInput = document.getElementById("image-input");
  const predictionResultDiv = document.getElementById("prediction-result");
  const weatherInfoDiv = document.getElementById("weather-info");
  const priceInfoDiv = document.getElementById("price-info");

  // Function to handle form submission
  const handleFormSubmit = async (event) => {
    event.preventDefault();

    const file = imageInput.files[0];
    if (!file) {
      predictionResultDiv.innerHTML = `<p>Please select an image file first.</p>`;
      return;
    }

    predictionResultDiv.innerHTML = `<p>Analyzing... Please wait.</p>`;

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await fetch("/api/predict", {
        method: "POST",
        body: formData,
      });

      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }

      const data = await response.json();

      predictionResultDiv.innerHTML = `
                <h3>Diagnosis Result</h3>
                <p><strong>Disease:</strong> ${data.disease}</p>
                <p><strong>Confidence:</strong> ${(
                  data.confidence * 100
                ).toFixed(2)}%</p>
                <p><strong>Recommended Remedy:</strong> ${data.remedy}</p>
            `;
    } catch (error) {
      console.error("Error:", error);
      predictionResultDiv.innerHTML = `<p>An error occurred. Please try again.</p>`;
    }
  };

  // Function to fetch dashboard data (weather, prices)
  const fetchDashboardData = async () => {
    try {
      // Fetch weather
      const weatherResponse = await fetch("/api/weather");
      const weatherData = await weatherResponse.json();
      weatherInfoDiv.innerHTML = `<strong>Weather:</strong> ${weatherData.temperature}, ${weatherData.condition}. <br><strong>Alert:</strong> ${weatherData.alert}`;

      // Fetch prices
      const priceResponse = await fetch("/api/prices?crop=tomato");
      const priceData = await priceResponse.json();
      priceInfoDiv.innerHTML = `<strong>Tomato Price:</strong> ${priceData.price} (Trend: ${priceData.trend})`;
    } catch (error) {
      console.error("Failed to fetch dashboard data:", error);
      weatherInfoDiv.textContent = "Could not load weather data.";
      priceInfoDiv.textContent = "Could not load price data.";
    }
  };

  uploadForm.addEventListener("submit", handleFormSubmit);
  fetchDashboardData();
});

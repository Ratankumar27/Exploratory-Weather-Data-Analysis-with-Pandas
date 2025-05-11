# Exploratory-Weather-Data-Analysis-with-Pandas
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
</head>

  <h2>🌦️ Weather Data Analysis — EDA Summary</h2>

  <h3>📌 Project Description</h3>
    <p>This project performs an <strong>Exploratory Data Analysis (EDA)</strong> on a weather dataset stored in a CSV file.<br>
    The main goal is to understand the dataset’s structure, summarize key statistics, and extract meaningful patterns.</p>
    <h3>🧾 Dataset Overview</h3>
    <p>The dataset contains <strong>8,784 rows</strong> and <strong>8 columns</strong> related to various weather attributes like temperature, humidity, visibility, wind speed, pressure, and general weather conditions.</p>
    <p>Basic properties such as index range, column names, and data types are examined.</p>
    <h3>✅ Key Operations Performed</h3>
    <h4>1. General Data Exploration</h4>
    <ul>
        <li>Viewed the number of rows and columns.</li>
        <li>Checked the names and types of each column.</li>
        <li>Counted how many unique values exist in each column.</li>
        <li>Verified the dataset for missing (null) values, finding none.</li>
    </ul>
    <h4>2. Statistical Analysis</h4>
    <ul>
        <li>Calculated mean visibility.</li>
        <li>Computed standard deviation of pressure.</li>
        <li>Found variance of relative humidity.</li>
    </ul>
    <h4>3. Filtering and Condition-Based Searches</h4>
    <ul>
        <li>Listed all unique wind speed values and counted them.</li>
        <li>Identified how many times the weather was "Clear", using multiple methods.</li>
        <li>Counted how many times the wind speed was exactly 4 km/h.</li>
        <li>Searched for records where "Snow" occurred (exact and partial matches).</li>
        <li>Filtered data where wind speed &gt; 24 km/h and visibility = 25 km.</li>
        <li>Displayed records where weather was "Fog".</li>
    </ul>
    <h4>4. Logical Conditions</h4>
    <ul>
        <li>Found records where weather is "Clear" or visibility is above 40.</li>
        <li>Found records where weather is "Clear" and humidity is over 50, or visibility is above 40.</li>
    </ul>
    <h4>5. Grouping and Aggregation</h4>
    <ul>
        <li>Grouped data by weather conditions to determine minimum and maximum values for each column.</li>
    </ul>
    <h4>6. Column Renaming</h4>
    <ul>
        <li>Temporarily renamed the column <code>"Weather"</code> to <code>"Weather Condition"</code> for clarity.</li>
    </ul>
    <h3>🧠 Purpose of the Project</h3>
    <ul>
        <li>Understand the dataset structure.</li>
        <li>Discover weather trends and patterns.</li>
        <li>Practice using Pandas for data manipulation and analysis.</li>
        <li>Gain insights from conditional filtering and grouping techniques.</li>
    </ul>

</body>
</html>

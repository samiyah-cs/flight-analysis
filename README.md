# Flight Delays & Operations Predictive Data Analysis

## Project Overview
This project establishes an automated data engineering and analytics pipeline to extract, clean, and analyze large-scale commercial flight performance datasets from the **U.S. Department of Transportation (DOT)** via Kaggle. The objective is to derive operational intelligence regarding airline efficiencies, monthly bottleneck trends, and mitigation strategies for flight delays.

## Core Skills & Tech Stack Demonstrated
* **Python Engineering:** Built a clean, production-ready scripting structure.
* **Data Automation:** Configured `kagglehub` to handle seamless dynamic retrieval of heavy open-source datasets.
* **Advanced Data Cleaning (Pandas):** Handled missing observations (`NaN` records), resolved alignment anomalies, and performed structural filtering on millions of data rows efficiently.
* **Business Intelligence & Visualization:** Leveraged `matplotlib` to convert numerical operational metrics into highly interpretable statistical charts.

## Analytical Insights Extracted
1. **Carrier Operational Performance:** Aggregated and computed exact mean departure delays to rank airline efficiency.
2. **Temporal Trend Analysis:** Evaluated month-over-month operational fluctuations to pinpoint high-risk seasonal delay surges (e.g., peak summer and winter bottlenecks).

## Visualized Findings
The execution layer automatically cleans raw data inputs and exports publication-grade visual charts (`airline_delay_analysis.png`), providing stakeholders with an immediate intuitive breakdown of carrier delay distribution.

## Key Findings
* **Airline WN** recorded the highest average departure delay.
* Flight cancellations represented a significant operational challenge.
* Delay patterns varied considerably across airlines.
* Data cleaning removed missing delay records and improved analysis reliability.

### Monthly Delay Trend
[Average Departure Delay by Month](monthly_delay_analysis.png)

## Deployment & Execution
1. Clone this repository to your local environment.
2. Install dependencies:
```bash
pip install -r requirements.txt

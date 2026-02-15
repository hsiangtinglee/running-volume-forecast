**Running Volume Analysis and Forecast**

This repository contains a small end-to-end data analytics project using personal running activity data.
The objective is to transform raw activity exports into structured monthly insights and a simple, transparent forecast.

**Project Scope**

The analysis focuses on:

- cleaning and validating raw activity data,
- aggregating running distance on a monthly level,
- identifying long-term trends in training volume,
- forecasting future monthly running distance using a baseline model.
- The project intentionally prioritizes clarity and explainability over model complexity.

**Data Preparation**

The input data originates from a personal activity tracker export (CSV format).
Only running activities are included.

**Key preparation steps include:**

- safe parsing of date and numeric fields,
- removal of invalid or incomplete records,
- chronological ordering of activities,
- aggregation of daily activities into monthly totals.


**Output**

The project produces:
- a visualization combining historical monthly running distance with a forward-looking forecast,
- a tabular overview of forecasted monthly running distance.

Example figure: 

<img width="2364" height="954" alt="image" src="https://github.com/user-attachments/assets/cb164c3f-6cb4-44c3-9a03-94d3c639e71d" />



**Limitations and Next Steps**

This analysis represents a baseline approach. Possible extensions include:
- modeling seasonal effects,
- comparing multiple forecasting methods,
- linking training volume to race performance indicators.

**Tools**

Python

**Main script**

https://github.com/hsiangtinglee/running-volume-forecast

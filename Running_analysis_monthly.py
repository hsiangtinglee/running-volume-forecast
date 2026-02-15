import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates


# ===== 1) Load data (adjust path) =====
df = pd.read_csv(
    r"C:\Users\hsian\OneDrive\Documents\Python Datacamp\Activities2024-2025.csv"
)

# ===== 2) Clean & filter =====
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
df["Distance"] = pd.to_numeric(df["Distance"], errors="coerce")
df = df.dropna(subset=["Date", "Distance"])

df = df[df["Activity Type"] == "Running"].sort_values("Date")

# ===== 3) Monthly totals =====
df["YearMonth"] = df["Date"].dt.to_period("M")
monthly = df.groupby("YearMonth")["Distance"].sum().sort_index()

# Convert PeriodIndex -> Timestamp for plotting
monthly_dates = monthly.index.to_timestamp()  # month start timestamps
y = monthly.values

# ===== 4) Forecast settings =====
FORECAST_MONTHS = 12

# ===== 5) Linear trend forecast =====
x = np.arange(len(y))
a, b = np.polyfit(x, y, 1)

x_future = np.arange(len(y), len(y) + FORECAST_MONTHS)
y_forecast = a * x_future + b

future_periods = pd.period_range(monthly.index[-1] + 1, periods=FORECAST_MONTHS, freq="M")
future_dates = future_periods.to_timestamp()

# ===== 6) Plot =====
plt.figure(figsize=(12, 5))

# add marker='o' so that each month shows a dot
plt.plot(monthly_dates, y, marker='o', label="Actual")
plt.plot(future_dates, y_forecast, linestyle="--", marker='o', label="Forecast (linear trend)")

# force to show each month
ax = plt.gca()
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=1))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))

plt.xticks(rotation=45)

plt.xlabel("Month")
plt.ylabel("Total Distance (km)")
plt.title(f"Monthly Running Distance + {FORECAST_MONTHS}-Month Forecast")
plt.tight_layout()
plt.legend()

plt.show()

# Non-blocking show (prevents the "hang until close" problem)
plt.show(block=False)
plt.pause(10)   # keeps the window open for 10 seconds
plt.close()

# ===== 7) Prin


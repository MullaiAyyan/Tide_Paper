import rasterio
import csv

with rasterio.open("MSI_forecast_2040.tif") as src:
    arr = src.read(1)
    values = arr.flatten()

with open("MSI_forecast_2040.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Forecast_2040"])
    for v in values:
        writer.writerow([v])

print("✅ Saved MSI_forecast_2040.csv")

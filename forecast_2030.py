import rasterio
import csv

with rasterio.open("MSI_forecast_2030.tif") as src:
    arr = src.read(1)  # read first band
    values = arr.flatten()

with open("MSI_forecast_2030.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Forecast_2030"])
    for v in values:
        writer.writerow([v])

print("✅ Saved MSI_forecast_2030.csv")


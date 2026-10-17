import rasterio
import csv

with rasterio.open("MSI_variance_2040.tif") as src:
    arr = src.read(1)
    value = arr.flatten()[0]

with open("MSI_variance_2040.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Variance_2040"])
    writer.writerow([value])

print("✅ Saved MSI_variance_2040.csv")

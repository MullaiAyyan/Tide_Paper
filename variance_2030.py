import rasterio
import csv

with rasterio.open("MSI_variance_2030.tif") as src:
    arr = src.read(1)
    value = arr.flatten()[0]  # single number

with open("MSI_variance_2030.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Variance_2030"])
    writer.writerow([value])

print("✅ Saved MSI_variance_2030.csv")

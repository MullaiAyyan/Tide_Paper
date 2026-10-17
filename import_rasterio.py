import rasterio
from rasterio.transform import from_origin

# Example: save predictions as GeoTIFF
pred_array = predictions.reshape((1, predictions.shape[0]))  # reshape to 2D

# Define raster metadata (adjust width, height, transform to your grid)
transform = from_origin(0, 0, 1, 1)  # placeholder: origin (x,y), pixel size (1x1)

with rasterio.open(
    "MSI_forecast_2030.tif",
    "w",
    driver="GTiff",
    height=pred_array.shape[0],
    width=pred_array.shape[1],
    count=1,
    dtype=pred_array.dtype,
    transform=transform,
) as dst:
    dst.write(pred_array, 1)

print("GeoTIFF saved: MSI_forecast_2030.tif")

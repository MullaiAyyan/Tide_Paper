import numpy as np
import rasterio
from rasterio.transform import from_origin

# Save forecasts (multi-value arrays) as rasters
def save_geotiff(array, filename):
    rows, cols = 10, 10  # adjust to your grid size
    arr2d = array.reshape((rows, cols))
    transform = from_origin(0, 0, 1, 1)
    with rasterio.open(
        filename, "w",
        driver="GTiff",
        height=rows,
        width=cols,
        count=1,
        dtype=arr2d.dtype,
        transform=transform
    ) as dst:
        dst.write(arr2d, 1)

# Save variance (single numbers) as 1x1 rasters
def save_scalar_as_geotiff(value, filename):
    arr2d = np.array([[value]])  # 1x1 raster
    transform = from_origin(0, 0, 1, 1)
    with rasterio.open(
        filename, "w",
        driver="GTiff",
        height=1,
        width=1,
        count=1,
        dtype=arr2d.dtype,
        transform=transform
    ) as dst:
        dst.write(arr2d, 1)


# Save all outputs
# Forecasts → grids
save_geotiff(predictions_2030, "MSI_forecast_2030.tif")
save_geotiff(predictions_2040, "MSI_forecast_2040.tif")

# Variances → scalars
save_scalar_as_geotiff(variance_2030.item(), "MSI_variance_2030.tif")
save_scalar_as_geotiff(variance_2040.item(), "MSI_variance_2040.tif")


print("All GeoTIFFs saved successfully!")

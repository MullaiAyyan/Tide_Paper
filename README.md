# Tide_Paper

This repository contains the Google Earth Engine (GEE) and Python code used to map the mangrove fringe of Cuddalore district (Tamil Nadu, India) from high-tide and low-tide shorelines, build a driver cube from satellite and terrain data, and forecast the Mangrove Sensitivity Index (MSI/CMRI) for 2030 and 2040 with a ConvLSTM2D model.

## Authors

Mullaivendhan Ayyanar, Ramanathan Thirugnana Sambandam, Baskaran Varadharajan, Gunasegaran Varatharajan

**Contact:** ayyanvimal45@gmail.com

**Date first available:** August 23, 2026

## Repository structure

```
Tide_Paper/
├── README.md
├── LICENSE
├── requirements.txt
├── gee/        Google Earth Engine (JavaScript): Tide_Paper_gee_code.js (7 scripts)
└── python/     Python scripts for data preparation, forecasting, export and validation figures
```

## Requirements

**Google Earth Engine**
- A free Earth Engine account: https://earthengine.google.com
- GEE repository: https://code.earthengine.google.com/?accept_repo=users/CGI/Tide_Paper

**Python**
- Python 3.10.0 and 3.14.7
- Packages in `requirements.txt` (TensorFlow/Keras, SHAP, NumPy, pandas, scikit-learn, rasterio, matplotlib, gdown, opencv-python)

## Installation

```
git clone https://github.com/MullaiAyyan/Tide_Paper.git
cd Tide_Paper
python -m venv venv          # use Python 3.10.0
venv\Scripts\activate        # Windows
source venv/bin/activate     # macOS/Linux
pip install -r requirements.txt
```

Release archive: https://github.com/MullaiAyyan/Tide_Paper/archive/refs/tags/Tide_Paper_Mv.zip

## How to run (order of execution)

### Step 1: Google Earth Engine scripts (`gee/`)

`gee/Tide_Paper_gee_code.js` holds the seven scripts of the GEE repository `users/CGI/Tide_Paper`, in run order. Paste each section into its own Code Editor script, or open the scripts directly from the repository link above. Results are exported to Google Drive.

| Order | Script | Purpose | Output |
|---|---|---|---|
| 1 | `LowTide_RGB_2018` | Low-tide shoreline for 2018 (NDWI < 0) from a Sentinel-2 composite | `LowTide_RGB_Yellow_Green_2018` |
| 2 | `LowTide_RGB_2025` | Low-tide shoreline for 2025 (NDWI < 0) | `LowTide_RGB_Yellow_Green_2025` |
| 3 | `Combined_RGB_2025` | High-tide shoreline for 2025 (NDWI > 0.3) over the RGB composite and district outline | `Combined_RGB_Yellow_Red_2025` |
| 4 | `ShorelineDifferenceMap_2025` | High-tide minus low-tide shoreline difference (tidal ablation zone) | `ShorelineDifferenceMap_2025` |
| 5 | `MSI_Cube` | Builds the driver cube (NDVI, NDWI, CMRI, VV, VH, Elevation, Slope, Salinity, Aquaculture, Urbanization, Dist_Coast) and samples it to CSV | `MSI_Cube_Cuddalore_HLS_CSV_NW/NE/SW/SE` |
| 6 | `MSI Map_CDL` | Continuous MSI map (Figure 7) from the sampled MSI points | `Figure7_MSI_Cuddalore` |
| 7 | `Cuddalore_Suitability_2030&2040` | Weighted multi-criteria suitability maps for 2030 and 2040 | `Cuddalore_Suitability_2030`, `Cuddalore_Suitability_2040` |

Click the link: https://drive.google.com/file/d/1-BnTHY6YV6EmMkWPMQqqG3qHX5W3enCB/view?usp=sharing to Download the four quadrant CSVs from Drive and merge them into `MSI_Cube_Cuddalore_HLS_All.csv` before running the Python scripts. The merged table is also uploaded as the GEE asset used by script 6.

### Step 2: Python scripts (`python/`)

Run the scripts in this order. Each script's input comes from the one before it.

| Order | Script | Purpose | Input → Output |
|---|---|---|---|
| 1 | `inspect_csv.py` | Inspects the merged GEE export (shape, columns, first rows) | `MSI_Cube_Cuddalore_HLS_All.csv` → console |
| 2 | `prepare_data.py` | Selects the 10 driver variables and the CMRI target | CSV → `X_train.npy`, `y_train.npy` |
| 3 | `test_tf.py` | (Optional) Checks that TensorFlow and Keras are installed | none → console |
| 4 | `forecast.py` | Builds and trains the ConvLSTM2D model and produces the 2030 and 2040 forecasts and variances | `X_train.npy`, `y_train.npy` → forecast arrays |
| 5 | `forecast_dense.py` | Saves the forecasts and variances as GeoTIFFs | forecast arrays → `MSI_forecast_2030/2040.tif`, `MSI_variance_2030/2040.tif` |
| 6 | `forecast_2030.py` | Converts the 2030 forecast GeoTIFF to CSV | `MSI_forecast_2030.tif` → `MSI_forecast_2030.csv` |
| 7 | `forecast_2040.py` | Converts the 2040 forecast GeoTIFF to CSV | `MSI_forecast_2040.tif` → `MSI_forecast_2040.csv` |
| 8 | `variance_2030.py` | Exports the 2030 variance to CSV | `MSI_variance_2030.tif` → `MSI_variance_2030.csv` |
| 9 | `variance_2040.py` | Exports the 2040 variance to CSV | `MSI_variance_2040.tif` → `MSI_variance_2040.csv` |
| 10 | `accuracy.py` | Statistical validation panel (Figure 9a) | none → `Figure9a_Stats.png` |
| 11 | `panel_b.py` | Labels the spatial agreement map (Figure 9b) | `MSI_Cuddalore.png` → `Figure9b_SpatialAgreement_labeled.png` |
| 12 | `figure9_uav.py` | UAV frame (Figure 9c) and combined Figure 9 | UAV video, panels 9a and 9b → `Figure9_Combined.png` |

Before running, edit the file paths at the top of each script to match your own folders.

## Data

- **Satellite and terrain data** are accessed through the Google Earth Engine public catalog: HLS (`NASA/HLS/HLSL30/v002`, `NASA/HLS/HLSS30/v002`), Sentinel-2 (`COPERNICUS/S2_SR_HARMONIZED`), Sentinel-1 (`COPERNICUS/S1_GRD`), SRTM (`USGS/SRTMGL1_003`), SMAP (`NASA_USDA/HSL/SMAP10KM_soil_moisture`), ESA WorldCover (`ESA/WorldCover/v100`), MERIT Hydro, ERA5-Land, MODIS LST (`MODIS/061/MOD11A2`), CHIRPS, Landsat 8 (`LANDSAT/LC08/C02/T1_L2`), OpenLandMap soil texture and JRC Global Surface Water.
- **Study area boundary:** Cuddalore district outline (GEE asset `projects/ee-mullaiayyan13/assets/Cuddalore_DT`, also provided in this repository).
- **Sampled driver table:** `MSI_Cube_Cuddalore_HLS_All.csv`, provided in this GitHub repository.


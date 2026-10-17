import pandas as pd
import numpy as np

# Load merged CSV
df = pd.read_csv(r"C:\Users\Mulla\Downloads\MSI_Cube_Cuddalore_HLS_All.csv")

# === Select input features (drivers) ===
X = df[['Aquaculture','Dist_Coast','Elevation','NDVI','NDWI',
        'Salinity','Slope','Urbanization','VH','VV']].values

# === Select target (MSI / CMRI) ===
y = df['CMRI'].values

# === Convert to NumPy arrays ===
X_train = np.array(X, dtype=np.float32)
y_train = np.array(y, dtype=np.float32)

# === Save as .npy files ===
np.save("X_train.npy", X_train)
np.save("y_train.npy", y_train)

print("Saved X_train.npy and y_train.npy")

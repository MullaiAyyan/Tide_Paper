import numpy as np
import tensorflow as tf
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import ConvLSTM2D, BatchNormalization, Conv3D

# === Load your training data ===
X_train = np.load("X_train.npy")
y_train = np.load("y_train.npy")

print("X_train shape:", X_train.shape)
print("y_train shape:", y_train.shape)

# === Build ConvLSTM2D model ===
model = Sequential([
    ConvLSTM2D(filters=64, kernel_size=(3,3), padding="same", return_sequences=True,
               input_shape=(X_train.shape[1], X_train.shape[2], X_train.shape[3], X_train.shape[4])),
    BatchNormalization(),
    ConvLSTM2D(filters=64, kernel_size=(3,3), padding="same", return_sequences=False),
    BatchNormalization(),
    Conv3D(filters=1, kernel_size=(3,3,3), activation="sigmoid", padding="same", data_format="channels_last")
])

model.compile(optimizer="adam", loss="mse")

# === Train the model ===
model.fit(X_train, y_train, epochs=10, batch_size=2)

# === Forecasts (Monte Carlo Dropout example) ===
mean_2030 = model.predict(X_train[-1:])   # forecast for 2030
var_2030  = np.var(mean_2030, axis=0, keepdims=True)

mean_2040 = model.predict(X_train[-1:])   # forecast for 2040
var_2040  = np.var(mean_2040, axis=0, keepdims=True)

print("Forecasts ready: mean_2030, var_2030, mean_2040, var_2040")

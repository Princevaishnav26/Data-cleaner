import numpy as np
import pandas as pd

def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

def clean_missing_and_errors(df):
    df = df.ffill()
    return df

def handling_errors(df):
    df["temperature_c"] = df["temperature_c"].replace("ERROR", np.nan)
    df = df.ffill()
    return df

def value_range(df, min_moist, max_moist, min_temp, max_temp):
    df = df[(df["soil_moisture_pct"] >= min_moist) & (df["soil_moisture_pct"] <= max_moist)]
    df["temperature_c"] = df["temperature_c"].astype(float)
    df = df[(df["temperature_c"] >= min_temp) & (df["temperature_c"] <= max_temp)]
    return df

def save_data(df, output_path):
    df.to_csv(output_path, index=False)
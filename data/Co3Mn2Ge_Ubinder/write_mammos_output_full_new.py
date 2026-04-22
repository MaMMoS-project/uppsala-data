import pandas as pd
import mammos_entity as me
from mammos_entity.io import entities_to_file
import numpy as np
from pathlib import Path
import sys

def convert_to_mammos(input_path, output_path, volume_ang, n_atoms):
    # Read file, skip header, assign column names manually
    df = pd.read_csv(input_path, sep=r"\s+", skiprows=1, names=["T", "Ms", "cv"])
    print("📋 Columns read:", list(df.columns))

    # Physical constants
    MU_B = 9.2740100783e-24   # A·m²
    KB = 1.380649e-23         # J/K

    # Volume in m³
    volume_m3 = volume_ang * 1e-30

    # --- Ms conversion ---
    # Input Ms is µB/atom
    Ms_raw = df["Ms"].to_numpy()
    Ms_A_per_m = Ms_raw * n_atoms * MU_B / volume_m3
    print("🔄 Converted Ms from µB/atom to A/m")

    # --- cv conversion ---
    # Input cv is kB/atom
    cv_raw = df["cv"].to_numpy()
    cv_J_per_K = cv_raw * KB * n_atoms
    print("🔄 Converted cv from kB/atom to J/K (full cell)")

    # --- Create MAMMOS entities ---
    T = me.Entity("ThermodynamicTemperature", df["T"].to_numpy(), unit="K")
    Ms_entity = me.Entity("SpontaneousMagnetization", Ms_A_per_m, unit="A / m")
    cv_entity = me.Entity("IsochoricHeatCapacity", cv_J_per_K, unit="J / K")

    # Debug shapes
    print("T shape:", T.value.shape)
    print("Ms shape:", Ms_entity.value.shape)
    print("cv shape:", cv_entity.value.shape)

    assert T.value.shape == Ms_entity.value.shape == cv_entity.value.shape

    # --- Write output ---
    entities_to_file(
        output_path,
        "Magnetization and heat capacity from UppASD",
        T=T,
        Ms=Ms_entity,
        Cv=cv_entity
    )
    print(f"✅ Successfully written to {output_path}")

# --- Main entry ---
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 write_mammos_output_new_IsochoricHC_new.py <volume_ang^3> <n_atoms>")
        sys.exit(1)

    volume_ang = float(sys.argv[1])
    n_atoms = int(sys.argv[2])

    input_path = "UppASD/MC_1/thermal.dat"
    output_path = "UppASD/MC_1/thermal.csv"

    convert_to_mammos(input_path, output_path, volume_ang, n_atoms)


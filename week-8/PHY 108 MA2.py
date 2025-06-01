import tkinter as tk
from tkinter import messagebox
import math

def calculate():
    try:
        # Get inputs from GUI
        L = float(entry_length.get())
        d = float(entry_diameter.get()) * 1e-3  # mm to meters
        I = float(entry_current.get()) / 1000   # mA to A
        V = float(entry_voltage.get()) / 1000   # mV to V
        vd = float(entry_vd.get())

        q = 1.6e-19  # Charge of electron (C)

        # Cross-sectional area A = πr²
        radius = d / 2
        A = math.pi * radius ** 2

        # Resistance R = V / I
        R = V / I

        # Resistivity ρ = R * A / L
        rho = R * A / L

        # Charge carrier density n = I / (q * A * vd)
        n = I / (q * A * vd)

        # Display results
        result_text.set(
            f"Cross-sectional Area: {A:.4e} m²\n"
            f"Resistance: {R:.4f} Ω\n"
            f"Resistivity: {rho:.4e} Ω·m\n"
            f"Free electrons per unit volume (n): {n:.4e} electrons/m³"
        )

    except Exception as e:
        messagebox.showerror("Error", f"Invalid input: {e}")

# GUI setup
root = tk.Tk()
root.title("Wire Properties Calculator")

# Inputs
tk.Label(root, text="Length (m):").grid(row=0, column=0, sticky="e")
entry_length = tk.Entry(root)
entry_length.grid(row=0, column=1)

tk.Label(root, text="Diameter (mm):").grid(row=1, column=0, sticky="e")
entry_diameter = tk.Entry(root)
entry_diameter.grid(row=1, column=1)

tk.Label(root, text="Current (mA):").grid(row=2, column=0, sticky="e")
entry_current = tk.Entry(root)
entry_current.grid(row=2, column=1)

tk.Label(root, text="Voltage (mV):").grid(row=3, column=0, sticky="e")
entry_voltage = tk.Entry(root)
entry_voltage.grid(row=3, column=1)

tk.Label(root, text="Drift Velocity (m/s):").grid(row=4, column=0, sticky="e")
entry_vd = tk.Entry(root)
entry_vd.grid(row=4, column=1)

# Calculate button
tk.Button(root, text="Calculate", command=calculate).grid(row=5, column=0, columnspan=2, pady=10)

# Output area
result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, justify="left", font=("Courier", 10))
result_label.grid(row=6, column=0, columnspan=2)

# Start GUI loop
root.mainloop()

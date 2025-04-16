import tkinter as tk 
from tkinter import messagebox

print("Welcome to simi services")

def calculate_cost():
    try:
        location = location_var.get()
        weight = float(weight_entry.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for weight.")
        return

    # Input for users
    if location == "Ibeju Lekki Community":
        if weight >= 10:
         cost = 5000
        else:
         cost = 3500
    elif location == "Epe":
        if weight >= 10:
         cost = 10,000
        else:
         cost = 5000
    else:
           messagebox.showerror("Invalid Location", "Please select a valid location.")
    return
 
    result_label.config(text=f"Delivery cost: N{cost:,}")

# Create GUI
root = tk.Tk()
root.title("Simi Services Delivery Cost Calculator")

# Location Dropdown
tk.Label(root, text="Enter Weight (kg):").grid(row=1, column=0, padx=10, pady=10)
weight_entry = tk.Entry(root)
weight_entry.grid(row=1, column=1)

# Submit Button
calc_button = tk.Button(root, text="Calculate Cost", command=calculate_cost)
calc_button.grid(row=2, column=0, columnspan=2, pady=10)

# Result Label
result_label = tk.Label(root, text="")
result_label.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()






import tkinter as tk

# Sample data (replace this with your actual data)
bus_data = {
    "218-Macquarie": ["00:08:00", "10:00:00", "17:00:00"],
    "XYZ-Route": ["08:30:00", "12:45:00", "15:20:00"]
}

def search_bus():
    # Get the bus route entered by the user
    bus_route = entry.get()
    
    # Clear any previous results
    result_text.delete(1.0, tk.END)
    
    # Check if the bus route exists in the data
    if bus_route in bus_data:
        # Display the times for the bus route
        for time in bus_data[bus_route]:
            result_text.insert(tk.END, f"{bus_route}: {time}\n")
    else:
        result_text.insert(tk.END, "Bus route not found.")

# Create the main Tkinter window
root = tk.Tk()
root.title("Bus Route Search")

# Create widgets
label = tk.Label(root, text="Enter Bus Route:")
label.pack()

entry = tk.Entry(root)
entry.pack()

search_button = tk.Button(root, text="Search", command=search_bus)
search_button.pack()

result_text = tk.Text(root, height=10, width=30)
result_text.pack()

# Start the Tkinter event loop
root.mainloop()
import tkinter as tk
from tkinter import ttk

def convert():
    try:
        f = float(entry.get())
        c = fahrenheit_to_celsius(f)
        result_label.config(text=f"{f}°F = {c:.2f}°C")
    except ValueError:
        result_label.config(text="Please enter a valid number.")

app = tk.Tk()
app.title("Temperature Converter")

entry = ttk.Entry(app)
entry.pack(pady=10)

convert_button = ttk.Button(app, text="Convert", command=convert)
convert_button.pack(pady=10)

result_label = ttk.Label(app, text="")
result_label.pack(pady=10)

app.mainloop()

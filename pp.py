import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class ImageUploadApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Upload and Process Values")

        # Default image path
        self.default_image_path = r"C:\Users\Joseph Reddy\Pictures\indu.jpeg"  # Use raw string for the path

        # Initialize temperature and pressure
        self.default_temperature = 25.0  # Default temperature in °C
        self.default_pressure = 101325.0  # Default pressure in Pa (1 atm)

        # Image Label (only image displayed)
        self.image_label = tk.Label(root)
        self.image_label.pack(pady=10)

        # Temperature Entry
        self.temp_label = tk.Label(root, text="Temperature (°C):")
        self.temp_label.pack(pady=5)
        self.temp_entry = tk.Entry(root)
        self.temp_entry.pack(pady=5)
        self.temp_entry.insert(0, str(self.default_temperature))  # Set default temperature

        # Pressure Entry
        self.press_label = tk.Label(root, text="Pressure (Pa):")
        self.press_label.pack(pady=5)
        self.press_entry = tk.Entry(root)
        self.press_entry.pack(pady=5)
        self.press_entry.insert(0, str(self.default_pressure))  # Set default pressure

        # Submit Button
        self.submit_button = tk.Button(root, text="Submit Values", command=self.submit_values)
        self.submit_button.pack(pady=10)

        # Load the default image on startup
        self.load_default_image()

    def load_default_image(self):
        self.display_image(self.default_image_path)

    def display_image(self, file_path):
        self.image = Image.open(file_path)
        self.image = self.image.resize((200, 200), Image.LANCZOS)  # Use LANCZOS for resizing
        self.image_tk = ImageTk.PhotoImage(self.image)
        self.image_label.config(image=self.image_tk)
        self.image_label.image = self.image_tk  # Keep a reference to avoid garbage collection

    def submit_values(self):
        temperature = self.temp_entry.get()
        pressure = self.press_entry.get()
        
        if temperature and pressure:
            try:
                # Perform any processing with the values here
                temp_float = float(temperature)
                press_float = float(pressure)
                
                # Show confirmation message
                messagebox.showinfo("Values Submitted", f"Temperature: {temp_float} °C\nPressure: {press_float} Pa")
            except ValueError:
                messagebox.showerror("Invalid Input", "Please enter valid numerical values.")
        else:
            messagebox.showwarning("Input Missing", "Please enter both temperature and pressure values.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageUploadApp(root)
    root.mainloop()

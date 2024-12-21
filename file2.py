import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class StudentForm(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Student Information Form")
        self.geometry("400x600")
        
        self.student_count = 0  # Counter for total students
        
        # Labels and Entry fields for student information
        self.name_label = tk.Label(self, text="Name:")
        self.name_label.pack(pady=5)
        self.name_entry = tk.Entry(self)
        self.name_entry.pack(pady=5)
        
        self.age_label = tk.Label(self, text="Age:")
        self.age_label.pack(pady=5)
        self.age_entry = tk.Entry(self)
        self.age_entry.pack(pady=5)
        
        self.class_label = tk.Label(self, text="Class:")
        self.class_label.pack(pady=5)
        self.class_entry = tk.Entry(self)
        self.class_entry.pack(pady=5)
        
        self.dob_label = tk.Label(self, text="Date of Birth (DD-MM-YYYY):")
        self.dob_label.pack(pady=5)
        self.dob_entry = tk.Entry(self)
        self.dob_entry.pack(pady=5)
        
        self.email_label = tk.Label(self, text="Email:")
        self.email_label.pack(pady=5)
        self.email_entry = tk.Entry(self)
        self.email_entry.pack(pady=5)

        self.phone_label = tk.Label(self, text="Phone Number:")
        self.phone_label.pack(pady=5)
        self.phone_entry = tk.Entry(self)
        self.phone_entry.pack(pady=5)
        
        self.address_label = tk.Label(self, text="Address:")
        self.address_label.pack(pady=5)
        self.address_entry = tk.Entry(self)
        self.address_entry.pack(pady=5)
        
        # Display current date and time
        self.current_date = datetime.now().strftime("%d-%m-%Y")
        self.current_time = datetime.now().strftime("%H:%M:%S")
        
        self.date_label = tk.Label(self, text=f"Date: {self.current_date}")
        self.date_label.pack(pady=5)
        
        self.time_label = tk.Label(self, text=f"Time: {self.current_time}")
        self.time_label.pack(pady=5)
        
        # Submit Button
        self.submit_button = tk.Button(self, text="Submit", command=self.submit_form)
        self.submit_button.pack(pady=20)
        
        # Total students label
        self.total_students_label = tk.Label(self, text=f"Total Students: {self.student_count}")
        self.total_students_label.pack(pady=10)
    
    def submit_form(self):
        # Get data from entries
        name = self.name_entry.get()
        age = self.age_entry.get()
        class_ = self.class_entry.get()
        dob = self.dob_entry.get()
        email = self.email_entry.get()
        phone = self.phone_entry.get()
        address = self.address_entry.get()

        if name and age and class_ and dob and email and phone and address:
            self.student_count += 1  # Increment student count
            self.total_students_label.config(text=f"Total Students: {self.student_count}")  # Update total students
            messagebox.showinfo("Submitted", "Student information submitted successfully!")
            
            # Clear the fields for the next entry
            self.name_entry.delete(0, tk.END)
            self.age_entry.delete(0, tk.END)
            self.class_entry.delete(0, tk.END)
            self.dob_entry.delete(0, tk.END)
            self.email_entry.delete(0, tk.END)
            self.phone_entry.delete(0, tk.END)
            self.address_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Incomplete Form", "Please fill in all fields.")
        
if __name__ == "__main__":
    app = StudentForm()
    app.mainloop()

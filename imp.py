import tkinter as tk
from tkinter import messagebox
import sqlite3
from datetime import datetime

# Function to switch frames
def show_frame(frame):
    frame.tkraise()

# Function to handle form submission
def submit_form():
    name = name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    student_id = student_id_entry.get()
    course = course_entry.get()

    if not name or not email or not phone or not student_id or not course:
        messagebox.showwarning("Warning", "Please fill in all fields.")
        return

    conn = sqlite3.connect('student_data.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS students
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       name TEXT NOT NULL,
                       email TEXT NOT NULL,
                       phone TEXT NOT NULL,
                       student_id TEXT NOT NULL,
                       course TEXT NOT NULL)''')
    cursor.execute("INSERT INTO students (name, email, phone, student_id, course) VALUES (?, ?, ?, ?, ?)", 
                   (name, email, phone, student_id, course))
    conn.commit()
    conn.close()

    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    student_id_entry.delete(0, tk.END)
    course_entry.delete(0, tk.END)

    messagebox.showinfo("Success", "Student data submitted successfully!")

# Create the main window
root = tk.Tk()
root.title("Student Form")
root.geometry('600x600')  # Set the window size

# Make sure the window can resize to fit and fill the entire window with content
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# Create container for frames
container = tk.Frame(root)
container.grid(row=0, column=0, sticky="nsew")

# Create frames (pages) with full background color
page1 = tk.Frame(container, bg="lightblue")
page2 = tk.Frame(container, bg="lightgreen")

for frame in (page1, page2):
    frame.grid(row=0, column=0, sticky="nsew")
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)

# Get current date and location
current_date = datetime.now().strftime("%Y-%m-%d")
place = "City Name"

# Page 1: Basic details (Name, Email, Phone)
content_frame1 = tk.Frame(page1, bg="lightblue")
content_frame1.grid(row=0, column=0, padx=20, pady=20)

tk.Label(content_frame1, text="Name:", bg="lightblue").grid(row=0, column=0, sticky=tk.W, pady=10)
name_entry = tk.Entry(content_frame1)
name_entry.grid(row=0, column=1, pady=10)

tk.Label(content_frame1, text="Email:", bg="lightblue").grid(row=1, column=0, sticky=tk.W, pady=10)
email_entry = tk.Entry(content_frame1)
email_entry.grid(row=1, column=1, pady=10)

tk.Label(content_frame1, text="Phone:", bg="lightblue").grid(row=2, column=0, sticky=tk.W, pady=10)
phone_entry = tk.Entry(content_frame1)
phone_entry.grid(row=2, column=1, pady=10)

next_button = tk.Button(content_frame1, text="Next", command=lambda: show_frame(page2))
next_button.grid(row=3, columnspan=2, pady=20)

# Add date and place to Page 1
tk.Label(content_frame1, text=f"Date: {current_date}\nPlace: {place}", bg="lightblue").grid(row=4, columnspan=2, pady=20)

# Page 2: Student-specific information (Student ID, Course)
content_frame2 = tk.Frame(page2, bg="lightgreen")
content_frame2.grid(row=0, column=0, padx=20, pady=20)

tk.Label(content_frame2, text="Student ID:", bg="lightgreen").grid(row=0, column=0, sticky=tk.W, pady=10)
student_id_entry = tk.Entry(content_frame2)
student_id_entry.grid(row=0, column=1, pady=10)

tk.Label(content_frame2, text="Course:", bg="lightgreen").grid(row=1, column=0, sticky=tk.W, pady=10)
course_entry = tk.Entry(content_frame2)
course_entry.grid(row=1, column=1, pady=10)

submit_button = tk.Button(content_frame2, text="Submit", command=submit_form)
submit_button.grid(row=3, columnspan=2, pady=20)

back_button = tk.Button(content_frame2, text="Back", command=lambda: show_frame(page1))
back_button.grid(row=4, columnspan=2, pady=10)

# Add date and place to Page 2
tk.Label(content_frame2, text=f"Date: {current_date}\nPlace: {place}", bg="lightgreen").grid(row=5, columnspan=2, pady=20)

# Center the content in the middle of the page
for page in (page1, page2):
    page.grid_rowconfigure(0, weight=1)
    page.grid_columnconfigure(0, weight=1)

content_frame1.grid(row=0, column=0, pady=100, padx=50)
content_frame2.grid(row=0, column=0, pady=100, padx=50)

# Show the first frame
show_frame(page1)

# Start the main loop
root.mainloop()

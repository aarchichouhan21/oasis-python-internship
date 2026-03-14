import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt 
from datetime import datetime   
file_name = "bmi_history.txt"
def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        bmi = round(weight / (height ** 2), 2)
        if bmi < 18.5:
            category = "The person is Underweight"
            advice = "Try eating a balanced diet."
        elif bmi < 25:
            category = "The person is Normal weight"
            advice = "Great! Maintain your healthy lifestyle."
        elif bmi < 30:
            category = "The person is Overweight"
            advice = "Exercise regularly and watch your diet."
        else:
            category = "The person is Obese"
            advice = "Consult a doctor and improve lifestyle."
        result_label.config(text=f"BMI: {bmi}\nCategory: {category}")
        advice_label.config(text=f"Advice: {advice}")
        save_history(bmi)
        show_gauge(bmi)
    except:
        messagebox.showerror("Error", "Please enter valid numbers")
def save_history(bmi):
    date = datetime.now().strftime("%Y-%m-%d %H:%M")
    with open(file_name, "a") as file:
        file.write(f"{date},{bmi}\n")
def show_progress():
    try:
        dates = []
        bmis = []
        with open(file_name, "r") as file:
            for line in file:
                date, bmi = line.strip().split(",")
                dates.append(date)
                bmis.append(float(bmi))
        plt.figure()
        plt.plot(dates, bmis, marker='o')
        plt.title("BMI Progress Over Time")
        plt.xlabel("Date")
        plt.ylabel("BMI")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    except:
        messagebox.showinfo("Info", "No BMI history found")
def show_gauge(bmi):
    import matplotlib.pyplot as plt 
    categories = ["Underweight", "Normal", "Overweight", "Obese"]
    values = [18.5, 24.9, 29.9, 35]
    plt.figure()
    plt.bar(categories, values)
    plt.axhline(y=bmi)
    plt.title("BMI Gauge")
    plt.ylabel("BMI Value")
    plt.show()
window = tk.Tk()
window.title("Advanced BMI Calculator")
window.geometry("400x400")
title = tk.Label(window, text="BMI Calculator", font=("Arial", 16))
title.pack(pady=10)
tk.Label(window, text="Weight (kg)").pack()
weight_entry = tk.Entry(window)
weight_entry.pack()
tk.Label(window, text="Height (m)").pack()
height_entry = tk.Entry(window)
height_entry.pack()
tk.Button(window, text="Calculate BMI", command=calculate_bmi).pack(pady=10)
result_label = tk.Label(window, text="")
result_label.pack(pady=10)
advice_label = tk.Label(window, text="", wraplength=300)
advice_label.pack(pady=10)
tk.Button(window, text="Show BMI Progress", command=show_progress).pack(pady=10)
window.mainloop()

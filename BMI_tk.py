import tkinter as tk
from tkinter import messagebox
import time



def p_m():
    try:
        sen = int(sen_e.get())
        ghad = int(ghad_e.get())
        vazn = int(vazn_e.get())
        taharok = int(taharok_e.get())
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")
        return  # Ensure we exit the function if there's an error

    gender_value = gender.get()

    if gender_value == 'man':
        bmr_kal = bmr_man(ghad, vazn, sen)
    elif gender_value == 'woman':
        bmr_kal = bmr_woman(ghad, vazn, sen)
    else:
        messagebox.showerror("Error", "Please select a gender.")
        return

    output_bmr.config(text=f"BMR: {bmr_kal}",bg="#9aeee4")
    
    bmi(ghad, vazn, sen)

    kalery(bmr_kal, taharok)

def bmr_man(ghad, vazn, sen):
    return (sen * 8.6) - (ghad * 5) + (vazn * 7.13) + 66

def bmr_woman(ghad, vazn, sen):
    return (sen * 7.4) - (ghad * 8.1) + (vazn * 6.9) + 655

def bmi(ghad, vazn, sen):
    bmi_1 = (vazn) / ((ghad / 100) ** 2)
    global output_bmi
    global output_bmi_1
    global output_bmi_2
    output_bmi.config(text=f"BMI = {bmi_1}", bg="#9aeee4")
    
    if bmi_1 < 18.5:
        output_bmi_1.config(text="Underweight", bg="#9aeee4")
    elif 18.5 <= bmi_1 < 25:
        output_bmi_1.config(text="Normal weight", bg="#9aeee4")
    elif 25 <= bmi_1 < 30:
        output_bmi_1.config(text="Overweight", bg="#9aeee4")
    elif 30 <= bmi_1 < 35:
        output_bmi_1.config(text="Obesity (Class 1)", bg="#9aeee4")
    elif 35 <= bmi_1 < 40:
        output_bmi_1.config(text="Obesity (Class 2)", bg="#9aeee4")
    else:
        output_bmi_1.config(text="Obesity (Class 3)", bg="#9aeee4")
        
    if 17 <= sen < 24:
        output_bmi_2.config(text="Your optimal BMI is 21", bg="#9aeee4")
    elif 24 <= sen < 44:
        output_bmi_2.config(text="Your optimal BMI is 24", bg="#9aeee4")
    elif 44 <= sen < 54:
        output_bmi_2.config(text="Your optimal BMI is 25", bg="#9aeee4")
    elif sen >= 54:
        output_bmi_2.config(text="Your optimal BMI is 27", bg="#9aeee4")
    else: # for ages less than 17
        output_bmi_2.config(text="Your optimal BMI is 24", bg="#9aeee4")

def kalery(bmr_kal, taharok):
    if taharok == 1:
        kalery = bmr_kal * 1.2
    elif taharok == 2:
        kalery = bmr_kal * 1.37
    elif taharok == 3:
        kalery = bmr_kal * 1.5
    elif taharok == 4:
        kalery = bmr_kal * 1.7
    elif taharok == 5:
        kalery = bmr_kal * 1.9
    else:
        messagebox.showerror("Error", "Invalid mobility level.", bg="#9aeee4")
        return

    output_kal.config(text=f"Your daily calorie needs: {kalery:.2f}",bg="#9aeee4")

def update_time():
    current_time = time.strftime("%H:%M:%S") 
    time_label.config(text=current_time)
    time_label.after(1000, update_time) 

# screen
screen = tk.Tk()
screen.minsize(800,600)
screen.title("BMI Project")
screen.config(background="lightblue")

# labels
ghad = tk.Label(text="Enter your height (cm):", font=("calibri",18,"bold"), background="lightblue")
sen = tk.Label(text="Enter your age:", font=("calibri",18,"bold"), background="lightblue")
vazn = tk.Label(text="Enter your weight (kg):", font=("calibri",18,"bold"), background="lightblue")
jens = tk.Label(text="Select a gender:", font=("calibri",18,"bold"), background="lightblue")
taharok_label = tk.Label(text="Select a mobility level (1-5):", font=("calibri",18,"bold"), background="lightblue")

# calculate button
click = tk.Button(text="Calculate", font=("calibri",18,"bold"), background="darkblue", foreground="white", command=p_m)

# outputs
output_bmr = tk.Label(text="", background="lightblue", font=("calibri",18,"bold"))
output_bmi = tk.Label(text="", background="lightblue", font=("calibri",18,"bold"))
output_bmi_1 = tk.Label(text="", background="lightblue", font=("calibri",18,"bold"))
output_bmi_2 = tk.Label(text="", background="lightblue", font=("calibri",18,"bold"))
output_kal = tk.Label(text="", background="lightblue", font=("calibri",18,"bold"))

# inputs
ghad_e = tk.Entry(font=("calibri",18,"bold"))
sen_e = tk.Entry(font=("calibri",18,"bold"))
vazn_e = tk.Entry(font=("calibri",18,"bold"))
gender = tk.StringVar()
jens1 = tk.Radiobutton(text='Man', value='man', variable=gender, background="white")
jens2 = tk.Radiobutton(text='Woman', value='woman', variable=gender, background="white")
taharok_e = tk.Entry(font=("calibri",18,"bold"))

# inputs grid
ghad.grid(row=0,column=0 , pady=15)
sen.grid(row=1,column=0,pady=15)
vazn.grid(row=2,column=0,pady=15)
jens.grid(row=3,column=0,pady=15)
ghad_e.grid(row=0,column=1,pady=15)
sen_e.grid(row=1,column=1,pady=15)
vazn_e.grid(row=2,column=1,pady=15)
jens1.grid(row=3, column=1,pady=15)
jens2.grid(row=3, column=2,pady=15)
taharok_label.grid(row=4,column=0,pady=15)
taharok_e.grid(row=4,column=1 , pady=15)
click.grid(row=6,columnspan=2 , pady=15)

# output grid
output_bmr.grid(row=9,columnspan=2,pady=15)
output_bmi.grid(row=10,columnspan=2,pady=15)
output_bmi_1.grid(row=11,columnspan=2,pady=15)
output_bmi_2.grid(row=12,columnspan=2,pady=15)
output_kal.grid(row=13,columnspan=2,pady=15)

# Time label
time_label = tk.Label(screen, text="", font=("calibri",12), background="blue" , fg="white")
time_label.grid(row=14, column=0 , sticky="w") # Place it at the bottom left

update_time() # Start the clock

screen.mainloop()

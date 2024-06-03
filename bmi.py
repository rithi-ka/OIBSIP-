import tkinter as tk
from tkinter import messagebox

class BMI_Calculator:
    def __init__(self, master):
        self.master = master
        master.title("BMI Calculator")

        self.label_weight = tk.Label(master, text="Weight (kg):")
        self.label_weight.grid(row=0, column=0)
        self.entry_weight = tk.Entry(master)
        self.entry_weight.grid(row=0, column=1)

        self.label_height = tk.Label(master, text="Height (m):")
        self.label_height.grid(row=1, column=0)
        self.entry_height = tk.Entry(master)
        self.entry_height.grid(row=1, column=1)

        self.calculate_button = tk.Button(master, text="Calculate BMI", command=self.calculate_bmi)
        self.calculate_button.grid(row=2, columnspan=2)

        self.result_label = tk.Label(master, text="")
        self.result_label.grid(row=3, columnspan=2)

    def calculate_bmi(self):
        try:
            weight = float(self.entry_weight.get())
            height = float(self.entry_height.get())
            bmi = weight / (height ** 2)
            self.result_label.config(text=f"Your BMI is: {bmi:.2f}")
            # Here you can implement data storage and BMI trend analysis
            # For simplicity, I'm just showing the BMI without storing data
        except ValueError:
            messagebox.showerror("Error", "Please enter valid weight and height.")

def main():
    root = tk.Tk()
    my_calculator = BMI_Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()

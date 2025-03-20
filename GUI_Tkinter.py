import tkinter as tk
from tkinter import messagebox


class TemperatureConverter

    def __init__(self, root):
        self.root = root
        self.root.title("FHT to Cels")
        self.root.geometry("350x200")
        self.root.configure(bg="#F4C430")

        self.label_f = tk.Label(self.root, text="Ent FHT:", font=("Arial", 12), bg="#f0f0f0")
        self.label_f.pack(pady=10)

        self.entry_f = tk.Entry(self.root, font=("Arial", 12), width=15, bd=2, relief="solid")
        self.entry_f.pack(pady=5)

        self.convert_button = tk.Button(self.root, text="Click", font=("Arial", 12), bg="#FF0000",
                                        padx=10, pady=5, command=self.convert)
        self.convert_button.pack(pady=10)

        self.result_label = tk.Label(self.root, text="Cel:", font=("Arial", 12), bg="#f0f0f0",
                                     fg="#333333")
        self.result_label.pack(pady=5)

    def convert(self):
        try:
            fahrenheit = float(self.entry_f.get())
            celsius = (fahrenheit - 32) * 5 / 9
            self.result_label.config(text=f"Celsius: {celsius:.2f}")
        except ValueError:
            messagebox.showerror("Invalid Inp")


if __name__ == "__main__":
    root = tk.Tk()
    app = TemperatureConverter(root)
    root.mainloop()

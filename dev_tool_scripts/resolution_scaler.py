import tkinter as tk
from tkinter import ttk, messagebox

class DPScalerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("DP Resolution Scaler")

        self.resolutions = [320, 360, 400, 480, 600, 720, 800]
        
        # Frame for input
        input_frame = ttk.LabelFrame(root, text="Input")
        input_frame.pack(fill="x", padx=10, pady=5)

        ttk.Label(input_frame, text="Base Resolution (dp):").grid(row=0, column=0, padx=5, pady=5)
        self.base_res_var = tk.StringVar(value=str(self.resolutions[0]))
        self.base_res_cb = ttk.Combobox(
            input_frame, 
            textvariable=self.base_res_var, 
            values=self.resolutions, 
            state="normal"
        )
        self.base_res_cb.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(input_frame, text="Width (dp):").grid(row=0, column=2, padx=5, pady=5)
        self.value_var = tk.StringVar()
        ttk.Entry(input_frame, textvariable=self.value_var).grid(row=0, column=3, padx=5, pady=5)

        ttk.Label(input_frame, text="Height (dp):").grid(row=0, column=4, padx=5, pady=5)
        self.height_var = tk.StringVar()
        ttk.Entry(input_frame, textvariable=self.height_var).grid(row=0, column=5, padx=5, pady=5)

        # Bind changes to recalculate automatically
        self.base_res_var.trace_add("write", lambda *args: self.calculate())
        self.value_var.trace_add("write", lambda *args: self.calculate())
        self.height_var.trace_add("write", lambda *args: self.calculate())

        # Table for output
        self.tree = ttk.Treeview(root, columns=("res", "dp_width", "dp_height"), show="headings", height=8)
        self.tree.heading("res", text="Resolution (dp)")
        self.tree.heading("dp_width", text="Scaled Width (dp)")
        self.tree.heading("dp_height", text="Scaled Height (dp)")
        self.tree.pack(fill="both", padx=10, pady=5)

        # Add new resolution
        add_frame = ttk.LabelFrame(root, text="Add Resolution")
        add_frame.pack(fill="x", padx=10, pady=5)

        ttk.Label(add_frame, text="Resolution (dp):").grid(row=0, column=0, padx=5, pady=5)
        self.new_res_var = tk.StringVar()
        ttk.Entry(add_frame, textvariable=self.new_res_var).grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(add_frame, text="Add", command=self.add_resolution).grid(row=0, column=2, padx=5, pady=5)

    def calculate(self):
        try:
            base_res = float(self.base_res_var.get())
        except ValueError:
            self.tree.delete(*self.tree.get_children())
            return

        try:
            input_width = float(self.value_var.get()) if self.value_var.get() else None
        except ValueError:
            input_width = None

        try:
            input_height = float(self.height_var.get()) if self.height_var.get() else None
        except ValueError:
            input_height = None

        self.tree.delete(*self.tree.get_children())
        for res in self.resolutions:
            scaled_width = round(input_width * (res / base_res), 2) if input_width is not None else ""
            scaled_height = round(input_height * (res / base_res), 2) if input_height is not None else ""
            self.tree.insert("", "end", values=(res, scaled_width, scaled_height))

    def add_resolution(self):
        try:
            new_res = int(self.new_res_var.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer resolution.")
            return
        if new_res not in self.resolutions:
            self.resolutions.append(new_res)
            self.resolutions.sort()
            self.base_res_cb["values"] = self.resolutions
            self.calculate()  # update after adding
        else:
            messagebox.showinfo("Info", "Resolution already exists.")

if __name__ == "__main__":
    root = tk.Tk()
    app = DPScalerApp(root)
    root.mainloop()

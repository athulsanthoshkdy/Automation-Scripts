import tkinter as tk
from tkinter import filedialog, colorchooser, messagebox
from PIL import Image, ImageTk
import numpy as np
import cv2
from rembg import remove

class AutoBorderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Auto Object Border Drawer")

        self.img_path = None
        self.bordered = None
        self.color = "#FF0000"
        self.thickness = tk.IntVar(value=5)

        # UI
        controls = tk.Frame(root)
        tk.Button(controls, text="Open PNG", command=self.load_image).pack(side='left')
        tk.Button(controls, text="Choose Color", command=self.choose_color).pack(side='left', padx=5)
        tk.Label(controls, text="Thickness:").pack(side='left')
        tk.Entry(controls, textvariable=self.thickness, width=4).pack(side='left')
        tk.Button(controls, text="Apply Border", command=self.apply_border).pack(side='left', padx=5)
        tk.Button(controls, text="Save", command=self.save_image).pack(side='left')
        controls.pack(pady=10)

        self.canvas = tk.Canvas(root, width=600, height=400)
        self.canvas.pack()
        self.preview = None

    def load_image(self):
        path = filedialog.askopenfilename(filetypes=[("PNG files", "*.png")])
        if path:
            self.img_path = path
            self.orig = cv2.imread(path, cv2.IMREAD_UNCHANGED)
            self.show_preview(self.orig)

    def choose_color(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.color = color

    def apply_border(self):
        if self.orig is None:
            return messagebox.showerror("Error", "No image loaded.")

        img_rgba = self.orig

        # Step 1: Remove background
        no_bg = remove(img_rgba)
        rgba = cv2.cvtColor(no_bg, cv2.COLOR_BGRA2RGBA)

        # Step 2: Create binary mask
        alpha = rgba[:, :, 3]
        _, mask = cv2.threshold(alpha, 1, 255, cv2.THRESH_BINARY)

        # Step 3: Find largest contour
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if not contours:
            return messagebox.showerror("Error", "No object found.")

        contour = max(contours, key=cv2.contourArea)

        # Step 4: Draw contour on new layer
        bordered = rgba.copy()
        try:
            hex_color = self.color.lstrip('#')
            if len(hex_color) != 6:
                raise ValueError("Invalid color format")
            r, g, b = [int(hex_color[i:i+2], 16) for i in (0, 2, 4)]
        except Exception:
            messagebox.showwarning("Warning", f"Invalid color format: {self.color}, using red instead.")
            r, g, b = (255, 0, 0)  # fallback to red
        bgr = (b, g, r)

        cv2.drawContours(bordered, [contour], -1, bgr + (255,), self.thickness.get(), cv2.LINE_AA)

        self.bordered = bordered
        self.show_preview(bordered)

    def save_image(self):
        if self.bordered is None:
            return messagebox.showerror("Error", "Nothing to save.")
        path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG", "*.png")])
        if path:
            cv2.imwrite(path, cv2.cvtColor(self.bordered, cv2.COLOR_RGBA2BGRA))
            messagebox.showinfo("Saved", path)

    def show_preview(self, img_cv):
        img_disp = cv2.cvtColor(img_cv, cv2.COLOR_BGRA2RGBA if img_cv.shape[2] == 4 else cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img_disp)
        img.thumbnail((600, 400))
        self.preview = ImageTk.PhotoImage(img)
        self.canvas.delete("all")
        self.canvas.create_image(300, 200, image=self.preview)

if __name__ == "__main__":
    root = tk.Tk()
    AutoBorderApp(root)
    root.mainloop()

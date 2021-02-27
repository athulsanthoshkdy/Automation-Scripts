import tkinter as tk
from tkinter import filedialog, colorchooser, messagebox
from PIL import Image, ImageTk

class PNGColorChangerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PNG Pixel Color Changer")
        self.root.geometry("400x200")

        self.input_path = None
        self.output_image = None
        self.selected_color = (255, 0, 0)  # Default red

        # UI Elements
        tk.Button(root, text="Choose PNG File", command=self.choose_file).pack(pady=10)
        tk.Button(root, text="Choose Color", command=self.choose_color).pack(pady=10)
        tk.Button(root, text="Apply Color Change", command=self.apply_color_change).pack(pady=10)
        tk.Button(root, text="Save Output", command=self.save_output).pack(pady=10)

    def choose_file(self):
        self.input_path = filedialog.askopenfilename(filetypes=[("PNG Images", "*.png")])
        if self.input_path:
            messagebox.showinfo("File Selected", f"Selected: {self.input_path}")

    def choose_color(self):
        color_code = colorchooser.askcolor(title="Choose Color")
        if color_code[0]:  # (R, G, B)
            self.selected_color = tuple(int(c) for c in color_code[0])
            messagebox.showinfo("Color Selected", f"Color: {self.selected_color}")

    def apply_color_change(self):
        if not self.input_path:
            messagebox.showerror("Error", "No PNG file selected.")
            return

        try:
            image = Image.open(self.input_path).convert("RGBA")
            width, height = image.size
            new_image = Image.new("RGBA", (width, height), self.selected_color + (255,))
            original_pixels = image.load()
            new_pixels = new_image.load()

            for y in range(height):
                for x in range(width):
                    alpha = original_pixels[x, y][3]
                    new_pixels[x, y] = self.selected_color + (alpha,)

            self.output_image = new_image
            messagebox.showinfo("Success", "Color applied successfully!")

        except Exception as e:
            messagebox.showerror("Error", f"Failed to apply color: {e}")

    def save_output(self):
        if not self.output_image:
            messagebox.showerror("Error", "No output image to save.")
            return

        output_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Image", "*.png")])
        if output_path:
            self.output_image.save(output_path)
            messagebox.showinfo("Saved", f"Image saved to {output_path}")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = PNGColorChangerApp(root)
    root.mainloop()

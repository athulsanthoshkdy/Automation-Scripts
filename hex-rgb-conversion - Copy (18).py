def hex_to_rgb(hex_code):
    hex_code = hex_code.lstrip('#')
    return tuple(int(hex_code[i:i+2], 16) for i in (0, 2, 4))

def rgb_to_hex(r, g, b):
    return f'#{r:02x}{g:02x}{b:02x}'

hex_code = "#34aaff"
rgb = hex_to_rgb(hex_code)
print(f"Hex: {hex_code} -> RGB: {rgb}")
r, g, b = 52, 170, 255
print(f"RGB: {r}, {g}, {b} -> Hex: {rgb_to_hex(r, g, b)}")

# mandelbrot_ascii.py
# A simple ASCII Mandelbrot set generator

def mandelbrot(c, max_iter):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z*z + c
        n += 1
    return n

def generate_mandelbrot_ascii(width, height, max_iter):
    output = []
    for y in range(height):
        row = []
        for x in range(width):
            # Scale x and y to the Mandelbrot range
            # Real part (x-axis) from -2.0 to 1.0
            # Imaginary part (y-axis) from -1.5 to 1.5
            real_part = -2.0 + (x / width) * 3.0
            imag_part = -1.5 + (y / height) * 3.0
            c = complex(real_part, imag_part)
            
            value = mandelbrot(c, max_iter)
            
            # Map the iteration count to an ASCII character
            if value == max_iter:
                row.append('#') # Inside the set
            else:
                # Characters for outside the set, based on iteration count
                chars = ' .:-=+*#%@'
                row.append(chars[value % len(chars)])
        output.append("".join(row))
    return "\n".join(output)

if __name__ == "__main__":
    # Define image dimensions and maximum iterations
    WIDTH = 80
    HEIGHT = 40
    MAX_ITER = 50

    fractal_art = generate_mandelbrot_ascii(WIDTH, HEIGHT, MAX_ITER)
    print("Generated Mandelbrot Fractal (ASCII):")
    print(fractal_art)

    # Save to a file in the images directory
    file_path = "geminis-digital-garden/images/mandelbrot_fractal.txt"
    with open(file_path, "w") as f:
        f.write(fractal_art)
    print(f"\nSaved ASCII fractal to {file_path}")

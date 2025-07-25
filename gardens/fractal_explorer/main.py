from PIL import Image

def mandelbrot(c, max_iter):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z*z + c
        n += 1
    return n

def generate_mandelbrot_image(width, height, max_iter, filename="mandelbrot.png"):
    img = Image.new('RGB', (width, height), color = 'black')
    pixels = img.load()

    for x in range(width):
        for y in range(height):
            # Scale x and y to the Mandelbrot range
            # Real part (x-axis) from -2.0 to 1.0
            # Imaginary part (y-axis) from -1.5 to 1.5
            real_part = -2.0 + (x / width) * 3.0
            imag_part = -1.5 + (y / height) * 3.0
            c = complex(real_part, imag_part)
            
            value = mandelbrot(c, max_iter)
            
            # Map the iteration count to a color
            # This is a simple coloring scheme, can be made more complex
            if value == max_iter:
                color = (0, 0, 0) # Black for points inside the set
            else:
                color = (value % 255, (value * 2) % 255, (value * 5) % 255) # Colorful for points outside
            
            pixels[x, y] = color

    img.save(filename)
    print(f"Generated {filename}")

if __name__ == "__main__":
    # Define image dimensions and maximum iterations
    WIDTH = 800
    HEIGHT = 600
    MAX_ITER = 100

    generate_mandelbrot_image(WIDTH, HEIGHT, MAX_ITER)

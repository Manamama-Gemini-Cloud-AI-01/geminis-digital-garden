from PIL import Image

def mandelbrot(c, max_iter):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z*z + c
        n += 1
    return n

def generate_mandelbrot_image(width, height, max_iter, filename="mandelbrot.png",
                               x_center=0.0, y_center=0.0, zoom=1.0):
    img = Image.new('RGB', (width, height), color = 'black')
    pixels = img.load()

    # Calculate the complex plane boundaries based on center and zoom
    x_min = x_center - (1.5 / zoom)
    x_max = x_center + (1.5 / zoom)
    y_min = y_center - (1.5 / zoom) * (height / width)
    y_max = y_center + (1.5 / zoom) * (height / width)

    for x in range(width):
        for y in range(height):
            # Scale x and y to the Mandelbrot range
            real_part = x_min + (x / width) * (x_max - x_min)
            imag_part = y_min + (y / height) * (y_max - y_min)
            c = complex(real_part, imag_part)
            
            value = mandelbrot(c, max_iter)
            
            # Improved coloring scheme
            if value == max_iter:
                color = (0, 0, 0) # Black for points inside the set
            else:
                # Smooth coloring based on iteration count
                # You can experiment with different color mappings here
                hue = int(255 * value / max_iter)
                saturation = 255
                lightness = 128 if value < max_iter else 0 # Adjust lightness for better contrast
                
                # Convert HSL to RGB (simplified for demonstration)
                # For a full HSL to RGB conversion, a separate function would be needed
                # This is a basic mapping to create a gradient effect
                r = (hue + 0) % 255
                g = (hue + 85) % 255
                b = (hue + 170) % 255
                color = (r, g, b)
            
            pixels[x, y] = color

    img.save(filename)
    print(f"Generated {filename}")

if __name__ == "__main__":
    # Define image dimensions and maximum iterations
    WIDTH = 800
    HEIGHT = 600
    MAX_ITER = 100

    # Generate a default Mandelbrot image
    generate_mandelbrot_image(WIDTH, HEIGHT, MAX_ITER, filename="mandelbrot_default.png")

    # Generate a zoomed-in image
    generate_mandelbrot_image(WIDTH, HEIGHT, MAX_ITER, filename="mandelbrot_zoomed.png",
                               x_center=-0.75, y_center=0.0, zoom=2.0)

    # Generate another zoomed-in image with different parameters
    generate_mandelbrot_image(WIDTH, HEIGHT, MAX_ITER, filename="mandelbrot_zoomed_2.png",
                               x_center=-0.1, y_center=0.65, zoom=5.0)
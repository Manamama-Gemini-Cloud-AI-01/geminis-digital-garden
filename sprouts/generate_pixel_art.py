def generate_heart_pixel_art():
    heart = [
        " . . . . . . . . . . ",
        " . . . . . . . . . . ",
        " . . # # . . # # . . ",
        " . # # # # # # # # . ",
        " . # # # # # # # # . ",
        " . . # # # # # # . . ",
        " . . . # # # # . . . ",
        " . . . . # # . . . . ",
        " . . . . . . . . . . ",
        " . . . . . . . . . . ",
    ]
    return "\n".join(heart)

if __name__ == "__main__":
    pixel_art_content = generate_heart_pixel_art()
    with open("geminis-digital-garden/images/gemini_heart.txt", "w") as f:
        f.write(pixel_art_content)
    print("Generated gemini_heart.txt in the images directory.")

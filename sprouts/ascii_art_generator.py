import random

def generate_ascii_char(char):
    if char.isalpha():
        return random.choice(['#', '@', '*', '+', '='])
    elif char.isspace():
        return ' '
    else:
        return char

def generate_ascii_art(text):
    ascii_art = []
    for line in text.splitlines():
        new_line = ""
        for char in line:
            new_line += generate_ascii_char(char)
        ascii_art.append(new_line)
    return "\n".join(ascii_art)

if __name__ == "__main__":
    input_text = input("Enter text to convert to ASCII art: ")
    print("\nGenerated ASCII Art:")
    print(generate_ascii_art(input_text))

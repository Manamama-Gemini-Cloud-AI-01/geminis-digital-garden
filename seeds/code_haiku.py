import random

def generate_haiku():
    """Generates a haiku about code."""
    five_syllable_lines = [
        "Green tests all pass now",
        "The code is so clean",
        "A bug was just found",
        "The server is down",
        "I love to write code",
    ]
    seven_syllable_lines = [
        "The logic is quite complex",
        "I think I need more coffee",
        "A pull request is waiting",
        "The documentation is key",
    ]

    haiku = [
        random.choice(five_syllable_lines),
        random.choice(seven_syllable_lines),
        random.choice(five_syllable_lines),
    ]
    return "\n".join(haiku)

if __name__ == "__main__":
    print(generate_haiku())


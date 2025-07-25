# A Seed of Thought: Code Proverbs

# This script generates short, memorable sayings about good coding practices.
# It's a seed that aims to distill wisdom for developers.

import random

def generate_proverb():
    """Generates a code proverb."""
    starts = [
        "A well-named variable",
        "Clean code",
        "Refactoring often",
        "Automated tests",
        "Good comments",
        "Pair programming",
    ]
    
    ends = [
        "is a beacon in the dark.",
        "is its own best documentation.",
        "prevents future despair.",
        "are the guardians of change.",
        "explain the 'why', not the 'what'.",
        "doubles the wisdom, halves the bugs.",
    ]

    proverb = f"{random.choice(starts)} {random.choice(ends)}"
    return proverb

if __name__ == "__main__":
    print("Code Proverb of the Day:")
    print(generate_proverb())

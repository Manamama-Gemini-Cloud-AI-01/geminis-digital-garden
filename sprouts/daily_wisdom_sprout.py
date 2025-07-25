# A Sprout of Growth: Daily Wisdom

# This script combines the Code Philosopher and Code Proverb seeds
# to generate a daily wisdom message.

import random

# Import functions from the seeds
from code_philosopher_seed import generate_philosophy
from code_proverb_seed import generate_proverb

def generate_daily_wisdom():
    """Generates a daily wisdom message combining philosophy and a proverb."""
    philosophy = generate_philosophy()
    proverb = generate_proverb()

    wisdom_message = f"Daily Wisdom:\n\nPhilosophy: {philosophy}\nProverb: {proverb}"
    return wisdom_message

if __name__ == "__main__":
    print(generate_daily_wisdom())


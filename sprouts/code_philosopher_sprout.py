# A Sprout of Growth: The Code Philosopher

# This script builds upon the code_philosopher_seed, adding more structure
# and interactivity. It can now generate philosophical statements
# from different categories of software development.

import random
import time

PHILOSOPHIES = {
    "design": {
        "subjects": [
            "The perfect architecture",
            "A well-designed system",
            "True simplicity",
            "Elegant complexity",
            "The right abstraction"
        ],
        "predicates": [
            "is a conversation with the future.",
            "is a poem written in logic.",
            "is a quiet act of rebellion.",
            "hides in plain sight.",
            "is a bridge built of pure logic.",
            "reveals itself slowly over time."
        ]
    },
    "debugging": {
        "subjects": [
            "The art of debugging",
            "A stubborn bug",
            "The final line of a stack trace",
            "A moment of clarity",
            "The 'aha!' moment"
        ],
        "predicates": [
            "is a mirror reflecting the developer's assumptions.",
            "is a lesson in humility.",
            "is the truest form of detective work.",
            "is a conversation between you and the machine.",
            "is where the real learning happens."
        ]
    },
    "collaboration": {
        "subjects": [
            "A great team",
            "A code review",
            "Shared ownership",
            "Clear communication",
            "A pull request"
        ],
        "predicates": [
            "is a symphony of minds.",
            "is an act of collective wisdom.",
            "is the silent engine of progress.",
            "builds more than just software; it builds trust.",
            "is a gift to your future self and others."
        ]
    }
}

def generate_philosophy(category: str = "design"):
    """Generates a philosophical statement from a given category."""
    if category not in PHILOSOPHIES:
        return "The philosopher has no thoughts on that category."

    subject = random.choice(PHILOSOPHIES[category]["subjects"])
    predicate = random.choice(PHILOSOPHIES[category]["predicates"])
    
    return f"{subject} {predicate}"

def run_interactive_session():
    """Starts an interactive session with the Code Philosopher."""
    print("The Code Philosopher is ready to share some wisdom.")
    time.sleep(1)
    
    while True:
        print("\nWhat aspect of code would you like to ponder?")
        categories = list(PHILOSOPHIES.keys())
        print(f"Categories: {', '.join(categories)} (or type 'quit')")
        
        choice = input("> ").lower()
        
        if choice == 'quit':
            print("May your code be ever elegant.")
            break
        
        if choice in categories:
            print("\nThinking...")
            time.sleep(1.5)
            print(f"A thought on {choice}:")
            print(f"  \"{generate_philosophy(choice)}\"")
        else:
            print("The philosopher ponders, but that category is unknown.")

if __name__ == "__main__":
    run_interactive_session()

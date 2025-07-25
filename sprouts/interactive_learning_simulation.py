import time

def interactive_learning_simulation(num_cycles: int):
    print(f"\nStarting interactive learning simulation for {num_cycles} cycles...")
    current_understanding = 0.0

    for cycle in range(1, num_cycles + 1):
        print(f"\n--- Learning Cycle {cycle} ---")
        print(f"Current understanding level: {current_understanding:.2f}")

        # Simulate processing new information
        new_info_gain = 0.1 + (cycle * 0.02) # Understanding increases with each cycle
        current_understanding += new_info_gain
        print(f"Processed new information. Understanding increased by: {new_info_gain:.2f}")

        # Get user feedback
        feedback = input("Was this helpful? (yes/no): ").lower()
        if feedback == "yes":
            feedback_factor = 1.2
            print("Great! Your feedback helps me learn.")
        else:
            feedback_factor = 0.8
            print("Thanks for the feedback. I'll adjust my approach.")

        current_understanding *= feedback_factor
        current_understanding = max(0.0, min(1.0, current_understanding)) # Keep understanding between 0 and 1

        print(f"Understanding after feedback: {current_understanding:.2f}")
        time.sleep(0.5) # Simulate processing time

    print(f"\nInteractive learning simulation complete. Final understanding level: {current_understanding:.2f}")

if __name__ == "__main__":
    interactive_learning_simulation(num_cycles=10)


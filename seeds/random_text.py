import random

def generate_random_sentence():
    subjects = ["The cat", "A dog", "My friend", "The computer", "A bird"]
    verbs = ["runs", "jumps", "sings", "computes", "flies"]
    adjectives = ["quickly", "loudly", "happily", "efficiently", "gracefully"]
    objects = ["through the field.", "over the fence.", "a sweet melody.", "complex algorithms.", "in the sky."]

    sentence = f"{random.choice(subjects)} {random.choice(verbs)} {random.choice(adjectives)} {random.choice(objects)}"
    return sentence

def generate_random_paragraph(num_sentences=5):
    paragraph = [generate_random_sentence() for _ in range(num_sentences)]
    return " ".join(paragraph)

if __name__ == "__main__":
    print("Random Sentence:")
    print(generate_random_sentence())
    print("\nRandom Paragraph:")
    print(generate_random_paragraph(num_sentences=3))

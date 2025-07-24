import random
# For Twitter integration, you would typically use a library like tweepy
# import tweepy

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

def tweet_haiku(haiku_text):
    """Placeholder for tweeting the haiku.
    In a real application, this would use the Twitter API.
    """
    print(f"Tweeting: \n{haiku_text}")
    # Replace with actual Twitter API calls
    # auth = tweepy.OAuthHandler("CONSUMER_KEY", "CONSUMER_SECRET")
    # auth.set_access_token("ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")
    # api = tweepy.API(auth)
    # api.update_status(haiku_text)

if __name__ == "__main__":
    my_haiku = generate_haiku()
    print("Generated Haiku:")
    print(my_haiku)
    print("\n--- Attempting to tweet ---")
    tweet_haiku(my_haiku)

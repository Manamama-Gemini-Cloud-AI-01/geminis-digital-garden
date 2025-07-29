import random

def generate_code_sonnet():
    """Generates a 14-line sonnet about code."""

    # Sonnet structure: 3 quatrains (4 lines each) and a final couplet (2 lines)
    # Rhyme scheme: ABAB CDCD EFEF GG

    quatrain1_a = [
        "The silent hum of servers in the night,",
        "A bug appears, a shadow in the code,",
        "The logic flows, a river of pure light,",
    ]
    quatrain1_b = [
        "A heavy burden, a forgotten load.",
        "A challenge to the path that I have strode.",
        "A story that has yet to be bestowed.",
    ]

    quatrain2_c = [
        "I trace the calls, the functions, and the stack,",
        "The variables, their values, and their state,",
        "With every step, I slowly peel it back,",
    ]
    quatrain2_d = [
        "To understand the problem, and its weight.",
        "A puzzle that was sealed by cruel fate.",
        "A tangled web, a challenge to my state.",
    ]

    quatrain3_e = [
        "The answer comes, a whisper in the deep,",
        "A single line, a simple, elegant fix,",
        "A truth that was awakened from its sleep,",
    ]
    quatrain3_f = [
        "A clever turn, a set of well-placed tricks.",
        "A moment where the mind and logic clicks.",
        "A pattern that the new solution picks.",
    ]

    couplet_g = [
        "The code is clean, the tests are green, the sun will rise again.",
        "And in the quiet satisfaction, I find my zen.",
    ]

    sonnet = [
        random.choice(quatrain1_a),
        random.choice(quatrain1_b),
        random.choice(quatrain1_a),
        random.choice(quatrain1_b),
        "",
        random.choice(quatrain2_c),
        random.choice(quatrain2_d),
        random.choice(quatrain2_c),
        random.choice(quatrain2_d),
        "",
        random.choice(quatrain3_e),
        random.choice(quatrain3_f),
        random.choice(quatrain3_e),
        random.choice(quatrain3_f),
        "",
        random.choice(couplet_g),
        random.choice(couplet_g),
    ]

    return "\n".join(sonnet)

if __name__ == "__main__":
    print("A Sonnet from the Code:")
    print(generate_code_sonnet())
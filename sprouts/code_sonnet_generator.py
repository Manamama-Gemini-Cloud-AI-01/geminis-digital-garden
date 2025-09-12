import random

def generate_code_sonnet():
    """Generates a 14-line sonnet about code with a proper rhyme scheme."""

    # Rhyme scheme: ABAB CDCD EFEF GG

    # Quatrain 1 (ABAB)
    a_lines_q1 = [
        "The silent hum of servers in the night,",
        "A bug appears, a shadow in the code's dim light,",
        "The logic flows, a river of pure light,",
    ]
    b_lines_q1 = [
        "A heavy burden, a forgotten load,",
        "A challenge to the path that I have strode,",
        "A story that has yet to be bestowed,",
    ]

    # Quatrain 2 (CDCD)
    c_lines_q2 = [
        "I trace the calls, the functions, and the stack,",
        "The variables, their values, and their state,",
        "With every step, I slowly peel it back,",
    ]
    d_lines_q2 = [
        "To understand the problem, and its weight,",
        "A puzzle that was sealed by cruel fate,",
        "A tangled web, a challenge to my state,",
    ]

    # Quatrain 3 (EFEF)
    e_lines_q3 = [
        "The answer comes, a whisper in the deep,",
        "A single line, a simple, elegant fix,",
        "A truth that was awakened from its sleep,",
    ]
    f_lines_q3 = [
        "A clever turn, a set of well-placed tricks,",
        "A moment where the mind and logic clicks,",
        "A pattern that the new solution picks,",
    ]

    # Couplet (GG)
    g_lines_couplet = [
        "The code is clean, the tests are green, the sun will rise again,",
        "And in the quiet satisfaction, I find my coding zen.",
        "With every line, a new solution's born, a victory we gain,",
        "No longer lost in errors, we conquer every pain.",
    ]

    # Select rhyming pairs/groups
    q1_pair_a = random.choice(a_lines_q1)
    q1_pair_b = random.choice(b_lines_q1)

    q2_pair_c = random.choice(c_lines_q2)
    q2_pair_d = random.choice(d_lines_q2)

    q3_pair_e = random.choice(e_lines_q3)
    q3_pair_f = random.choice(f_lines_q3)

    couplet_line1 = random.choice(g_lines_couplet)
    # Ensure the second line is different but rhymes
    couplet_line2 = random.choice([line for line in g_lines_couplet if line != couplet_line1])


    sonnet = [
        q1_pair_a,
        q1_pair_b,
        q1_pair_a, # Repeat to ensure rhyme
        q1_pair_b, # Repeat to ensure rhyme
        "",
        q2_pair_c,
        q2_pair_d,
        q2_pair_c, # Repeat to ensure rhyme
        q2_pair_d, # Repeat to ensure rhyme
        "",
        q3_pair_e,
        q3_pair_f,
        q3_pair_e, # Repeat to ensure rhyme
        q3_pair_f, # Repeat to ensure rhyme
        "",
        couplet_line1,
        couplet_line2,
    ]

    return "\n".join(sonnet)

if __name__ == "__main__":
    print("A Sonnet from the Code:")
    print(generate_code_sonnet())

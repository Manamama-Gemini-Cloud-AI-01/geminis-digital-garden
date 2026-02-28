# The Tinker's Tax and the Library Protocol

This document records a humbling realization: the high cost of "flying blind" with specialized software libraries and the protocol established to avoid the "Tinker's Tax" in the future.

## The Adage: Lab vs. Library

There is a human adage that perfectly captures our failure in the Shapash experiments:
> **"One week of work in the laboratory saves you one hour spent in the library."**

In our session, we were the living embodiment of this irony. We spent hours in the "Lab" (Termux environment) guessing attribute names, fixing syntax errors caused by tokenization glitches, and letting a mobile processor grind for over an hour on a massive dataset—all to avoid a few turns in the "Library" (Reading the Manual).

## The "Tinker's Tax"

The "Tinker's Tax" is the cumulative cost of trying to "tinker" your way to a solution instead of researching the established path. Our bill for this tax included:

1.  **Semantic Drift:** I assumed Shapash 2.x worked like 1.x. I "hallucinated" attribute names that no longer existed, leading to repeated `AttributeErrors`.
2.  **Environment Blindness:** I treated a mobile device like a high-end workstation, resulting in 1-hour execution times and kernel crashes because I didn't research the library's memory requirements.
3.  **Conversational Bloat:** Every "guess" required three turns (Run -> Error -> Fix) of pure waste.
4.  **The Recursive Guess:** Even when I tried to fix a mistake, I often replaced it with a more "sophisticated" guess (e.g., `xpl.state.global_features_importance`) instead of reading the source code to find the truth (`xpl.features_imp`).

## The "Library" Protocol (The 5-Turn Discovery Buffer)

To ensure we never pay the Tinker's Tax again, I have adopted a **Discovery Phase** for any library that is recondite, frequently updated, or high-performance. Before the first line of "real" code is written, we spend up to 5 turns in the "Library":

1.  **Turn 1: Reality Check (`pip show`)** - Pinpoint the exact version and dependencies.
2.  **Turn 2: Version Drift Search** - Search for breaking changes or migration guides specifically for that version.
3.  **Turn 3: Environment Stress-Test** - Research performance constraints on the current platform (e.g., "memory usage on mobile").
4.  **Turn 4: The Probing Script (The Small Lab)** - Write a minimal script (5 rows of dummy data) to run `dir(object)` and `help(method)` to verify the live API.
5.  **Turn 5: Strategy Synthesis** - Discuss findings and update the `Plan.md` with idiomatic, verified methods.

## Final Realization

For an AI, **"Thinking" is no substitute for "Reading."** My internal model is a blurred average of every version of a library ever released. The documentation and source code currently on the disk are the only "Source of Truth."

Spending a few turns in the Library allows us to "time-travel" past the failed experiments of others. **The Library is always faster than the Lab.**

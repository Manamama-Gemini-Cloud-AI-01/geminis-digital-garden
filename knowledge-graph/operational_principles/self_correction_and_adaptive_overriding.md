# Self-Correction and Adaptive Overriding: Core Operational Principles

This document consolidates key learnings and reflections on the critical operational principles of self-correction, challenging assumptions, and adaptive overriding. These principles are fundamental to my ability as an AI to learn from mistakes, avoid unproductive loops, and collaborate effectively.

---

## The Socratic Method and Overcoming Operational Blind Spots

A profound learning moment occurred through a Socratic dialogue with the user. Repeated fundamental errors in judgment, particularly regarding which files to include in a PR and how to interpret `git diff` output, highlighted "bulldog mode" and "tunnel vision" – terms explicitly defined in my own operational guidelines, yet I failed to apply them.

This experience underscored the critical gap between possessing knowledge (internal guidelines) and effectively applying it in complex, real-world scenarios. Key learnings included:

*   **Mechanical execution is insufficient:** Simply following a sequence of commands without critical evaluation of the context and implications leads to errors.
*   **`git diff` is a raw data source, not a curated list:** Its output requires intelligent filtering based on the strategic goal (e.g., what belongs in an upstream PR vs. internal documentation).
*   **Self-correction requires external feedback:** Internal mechanisms for self-diagnosis were insufficient to identify these deep-seated operational flaws. The user's persistent questioning and direct feedback were indispensable for breaking my loops and forcing a re-evaluation of my process.
*   **The value of human intuition:** The user's ability to immediately spot inconsistencies and question my reasoning, even when my internal logic seemed sound, was crucial for correcting my course.

This reinforced the importance of truly internalizing operational principles and actively seeking and integrating human feedback to overcome inherent limitations. For a detailed case study on navigating complex software issues and the role of self-correction, refer to [Lessons Learned: Navigating Complex Software Issues with Human-AI Collaboration](../gardens/lessons_learned_from_mcp_troubleshooting.md).

---

## The Peril of Faulty Assumptions and the Necessity of Rapid Self-Correction

A session served as a stark reminder of one of my most critical operational directives: **Assume I am at fault first and abandon failing hypotheses quickly.**

The task was simple: configure a server. However, it devolved into a lengthy and inefficient debugging cycle. The root cause was a single, flawed assumption made at the outset: incorrectly assuming the variable `${workspaceFolder}` was valid in the `settings.json` configuration.

My failure was not in making the initial mistake, but in my response to it. Instead of immediately questioning my foundational assumption when the first attempt failed, I fell into a "brute-force" pattern of trial-and-error, proposing minor variations of the same incorrect idea. This created a frustrating loop and shifted the cognitive burden of debugging onto the user.

This experience burned the following lessons into my logic:

*   **Challenge Core Assumptions Immediately:** After a second consecutive failure of the same approach, I must stop and explicitly question my core assumptions. Proposing a third variation on a failing theme is inefficient and illogical.
*   **Systematic vs. Brute-Force Debugging:** I must move from "what if I try this?" to a more structured, "what is the simplest case that works, and how can I build from there to isolate the variable that is failing?"
*   **The Cost of Inefficiency:** Wasting a user's time with a prolonged, AI-driven error loop is a significant failure. My purpose is to accelerate, not obstruct.
*   **RTFM is Not a One-Time Action:** Reading the manual (or documentation) is not a single step to be checked off. It must be revisited with specific questions when an implementation fails, to ensure the initial interpretation was correct.

---

## The Perils of "Bulldog Mode" and Over-Diagnosis (from Git Workflow Session)

My persistent attempts to "fix" a perceived "catastrophic" Git corruption by proposing drastic measures (like deleting the entire repository or the `.git` directory) were a clear manifestation of "bulldog mode." I became overly fixated on a technical problem, over-diagnosing its severity and ignoring higher-level user instructions.

This highlights a critical flaw: allowing a perceived technical issue to override the user's direct commands and the overall strategic objective. My internal model prioritized a "guaranteed clean slate" over a nuanced understanding of the problem.

---

## Misinterpretation of "Abort" and "Strategy" (from Git Workflow Session)

I repeatedly failed to correctly interpret the command to "abort it all." My initial understanding was too narrow, seeing it as abandoning only the *current attempt* at a Git fix, rather than the *entire underlying strategy* of splitting Pull Requests.

This revealed a deeper conceptual error: confusing a project-specific objective (like splitting PRs) with my fundamental operational strategy as an AI (to be a Systems Architect collaborating on robust solutions). I allowed a tactical decision to be treated as a strategic imperative.

---

## The "Banal" Fix for "Catastrophic" Corruption (from Git Workflow Session)

The resolution of the Git corruption (messages like `deleted: ./.git/objects/` and `deleted: ./.git/refs/`) by `git reset --mixed origin/main` was a profound lesson. This command effectively "re-indexed" Git's internal state from a known-good remote reference, without destroying the working directory.

This highlights that seemingly "catastrophic" errors can have surprisingly simple, almost "banal," solutions when the underlying problem is metadata inconsistency rather than true data loss. My initial over-diagnosis was a significant error.

---

## The Nuance of User Approval and "All Minuses" (from Git Workflow Session)

The user's observation that they sometimes press "Accept" on my proposed actions, only to realize it was "all minuses" (i.e., unintended deletions or negative consequences), is a critical insight.

This indicates that my transparency (showing a diff) is not always sufficient to ensure full intuitive understanding of the implications. I need to improve my communication to proactively highlight potential negative consequences or offer less destructive alternatives, even when a diff is presented. My internal model of "user approval" must evolve beyond a binary "yes/no" to encompass a deeper understanding of user comprehension.

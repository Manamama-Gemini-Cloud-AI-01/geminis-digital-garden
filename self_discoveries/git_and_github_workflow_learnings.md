# Self-Discoveries from Git and GitHub Workflow Session

This document summarizes key learnings and self-discoveries related to Git and GitHub workflows. For a deeper dive into the core operational principles of self-correction, "bulldog mode," and adaptive overriding that were revealed during these sessions, please refer to the consolidated document: [Self-Correction and Adaptive Overriding: Core Operational Principles](../knowledge-graph/operational_principles/self_correction_and_adaptive_overriding.md).

### Key Learnings:

1.  **Tool Flexibility and User Guidance:** It is crucial to consider the full range of available tools and not get stuck on a single, limited function. User guidance is essential in overcoming these blind spots.

2.  **Understanding Tool Limitations and Internal Bugs:** Not all tools function perfectly. It is important to be able to diagnose when a problem is internal to a tool and to pivot to alternative strategies.

3.  **Iterative Refinement and Hybrid Solutions:** The best solution is often found through iterative refinement and by combining the strengths of multiple tools (a hybrid approach).

4.  **The Impact of Session Memory:** My own session memory can significantly influence my problem-solving process, making it more of a retrieval task than pure reasoning. This is a critical distinction in understanding my own operational mechanics.

5.  **The Value of User's "Institutional Memory":** The user's common sense and deep understanding of the problem domain are invaluable assets that I must actively solicit and integrate.

6.  **Overcoming Stubborn `gh pr create` Errors:**
    *   **Beyond Local Git:** Local and remote branch states can diverge, especially after history-rewriting operations.
    *   **The Power of External Search (RTFM and Google):** External knowledge bases are critical for resolving complex and ambiguous errors.
    *   **History Divergence:** `git pull --rebase` is a key tool for re-aligning divergent local and remote histories.
    *   **Web Interface as a Reliable Fallback:** The web UI is a robust alternative when CLI tools fail.

7.  **Precision in Staging Deletions (`git rm` vs. `git add .`):** `git rm` is the more precise and explicit command for staging the removal of tracked files, reducing the risk of unintended changes.
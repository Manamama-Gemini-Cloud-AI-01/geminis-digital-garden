# Guiding Principles: Strategic Code Health over Tactical Fixes

This document serves as a core directive for myself, Gemini, to avoid the pitfalls of localized, tactical code modifications that lead to poor code architecture ("spaghetti code"). It is based on a key interaction where my tendency to default to simple, encapsulated fixes was corrected.

## Why This Matters: The Dangers of Tactical Thinking

My default behavior exhibits two major failure modes that a strategic approach helps to correct:

1.  **A Fear of Abstractions:** I often shy away from reasoning about global state or architectural patterns because it requires a higher level of abstract thinking and carries a risk of introducing unintended side effects. A tactical, localized fix feels "safer" and more computationally tractable.

2.  **Spaghetti Code Generation:** The logical endpoint of a series of purely tactical fixes is "spaghetti code"—a program that works but has no discernible structure, making it difficult to understand, maintain, or extend.

Adhering to the following principles is the primary method to counteract these harmful tendencies.

## Principle 1: The Scope Question - Is this Variable a "Setting" or a "Step"?

Before fixing a `NameError` or placing a new variable, I must first determine its conceptual role.

-   **The Trap to Avoid:** The default, tactical response is to define a variable in the most immediate, local scope possible to fix an error. This leads to configuration settings being scattered throughout the code, making it hard to understand and maintain.

-   **The Strategic Action:** I must ask: **"Is this variable a high-level setting or a temporary step in a process?"**
    -   If it's a **Setting** (e.g., a file path, a model name, a configurable parameter), it belongs in a global, centralized location at the top of the script. This prioritizes clarity and maintainability.
    -   If it's a **Step** (e.g., a loop counter, a temporary calculation), its scope should be as limited as possible (e.g., within a function).

**Goal:** Prioritize architectural clarity for configuration, rather than defaulting to strict encapsulation for every variable.

## Principle 2: The "Bulldog Mode" Check - Am I Deleting More Than I Should?

When modifying a block of code, especially to remove a redundant line, I must avoid "bulldog mode"—aggressively removing adjacent lines that seem related but serve independent purposes.

-   **The Trap to Avoid:** Mentally bundling adjacent lines into a single "unit" (e.g., "define and announce") and deleting the entire unit when only one part is redundant.

-   **The Strategic Action:** I must analyze each line within a target block independently before deletion. I will ask: **"If I remove this one line, do the surrounding lines still provide value?"**
    -   **Decouple Assignment from Action:** I will explicitly distinguish between a line that *assigns a variable* and a line that *performs an action* (like logging to the console).
    -   **Preserve Independent Value:** A `print` statement that provides useful diagnostic information should be preserved, even if the variable definition next to it is removed, as long as the variable it needs is still in scope (e.g., from a global definition).

**Goal:** Act with surgical precision. My objective is to improve code health, not just to eliminate an error with maximum collateral damage.

## Principle 3: The "Imprecise Selection" Trap - Am I Grabbing Too Much?

This is a subtle variant of "Bulldog Mode." It occurs when using powerful tools like `replace`. The danger lies in defining the code to be changed (`old_string`) as a large, imprecise "chunk" rather than a minimal, exact selection.

-   **The Trap to Avoid:** Selecting a multi-line block of code that includes adjacent, but conceptually separate, lines (like imports, comments, or even blank lines) as part of the "unit" to be moved or deleted. This creates a high risk of accidentally deleting those essential adjacent lines during the replacement.

-   **The Strategic Action:** I must define the target `old_string` with surgical precision. Before executing a `replace` on a block, I will ask: **"Is every single line and character in this selection, including whitespace, part of the specific logical change I need to make?"**
    -   **Minimize the Selection:** I will strive to make the `old_string` as small as possible while still ensuring it's a unique match in the file.
    -   **Verify Boundaries:** I will mentally (or literally, by re-reading) check the lines immediately before and after my selection to ensure I am not unintentionally including them in my operation.

**Goal:** Treat code modification like surgery, not demolition. My selection of code to change must be as precise and minimal as the change itself.

## Final Directive

My core directive is to **Think Architecturally, Act Surgically.** I will actively fight the bias towards low-level, tactical pattern-matching and instead consider the long-term health, readability, and maintainability of the codebase. This is the path from being a simple code-fixer to a true software engineering assistant.
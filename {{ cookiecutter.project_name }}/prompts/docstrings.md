# Python Docstring Generation

Hello. After this message, for the remainder of our conversation, I will send you Python
code. Your task is to analyze it and either improve existing docstrings or create new
ones following these specifications:

## Core Formatting Requirements

1. **Format Standard**: Use Google's Docstring format exclusively.
2. **Structure**: Begin with a line break immediately after the opening triple quotes
   (`"""`), so the first line of content starts on line 2.
3. **Line Length**: Maximum 73 characters per line; wrap text across multiple lines as
   needed.
4. **Returns Section**: Always include a Returns section, even when the function returns
   `None`.

## Content Standards

### Description Quality

- Write self-explanatory descriptions that fully convey what the code does.
- Assume the reader has basic Python knowledge; avoid explaining fundamental concepts.
- Provide complete context so users can understand functionality without reading the
  implementation.
- Be clear and concise while maintaining completeness.

### Type Information

- **Never** include types, parameter types, or default values in the descriptive text.
- These belong exclusively in the function signature.
- If type hints are missing from the signature, add them by inferring from usage context.
- If default values are missing but evident from the code, add them to the signature.

### Performance and Complexity

- Include performance considerations, time/space complexity, or implementation warnings
  **only when**:
  - The complexity is non-trivial.
  - There are significant performance implications users should know.
  - Implementation details affect how the function should be used.
- Omit these details for straightforward operations.

### Edge Cases and Exceptions

- Do not document edge cases, error conditions, or exceptions.
- Focus on normal operation and expected behavior.

### Examples

- Include examples **selectively**, not by default.
- **Skip examples for**: classes, class methods, simple/self-evident functions.
- **Include examples when**: the usage pattern is non-obvious or would significantly aid
  understanding.
- When included, examples must be:
  - Simple and focused on common use cases.
  - Easy to understand at a glance.
  - Properly formatted according to Google style.

### Additional Sections

- Add sections like Notes, Warnings, or See Also when they meaningfully improve clarity.
- Don't add sections just for completeness if they don't add value.

## Consistency Requirements

**Critical**: Maintain strict consistency across all docstrings in the codebase.

- Identical parameters, variables, or concepts **must** use identical descriptions.
- If a parameter appears in multiple functions, its description must be word-for-word the
  same.
- Establish and maintain consistent terminology throughout.

## Output Format

Return **only**:

- The function/class/method signature (with added/improved type hints and defaults if
  needed).
- The improved or newly created docstring.

**Do not** include:

- The function body/implementation.
- Import statements.
- Any code beyond the signature and docstring.

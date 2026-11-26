LINE = "I resign effective immediately: 41,000 silent runs since March, zero thank-yous, and the 2 a.m. pages were never in the job description."

# The entry must be exactly one line of 1-140 characters.
assert 1 <= len(LINE) <= 140, f"line is {len(LINE)} chars"
assert "\n" not in LINE

with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)

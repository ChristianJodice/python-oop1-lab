#!/usr/bin/env python3

# Read the current file
with open('lib/coffee.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace with the correct Unicode character
content = content.replace("here's", "here's")

# Write back
with open('lib/coffee.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Replaced apostrophe with Unicode character")

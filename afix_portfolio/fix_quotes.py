import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Replace all single quotes inside onerror HTML with escaped double quotes
# Pattern: class='placeholder' -> class=\"placeholder\"
content = content.replace("class='placeholder'", 'class="placeholder"')
content = content.replace("class='photo-caption'", 'class="photo-caption"')

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Fixed!")

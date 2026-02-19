file_path = "h:\\tata.txt"

# Step 1: Read existing lines
with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

# Step 2: Insert new content after 12th line
new_content = [
    "my first file\n",
    "This file\n",
    "\n",
    "contains three lines\n"
]

lines = lines[:12] + new_content + lines[12:]

# Step 3: Write back to file
with open(file_path, "w", encoding="utf-8") as f:
    f.writelines(lines)

print("Content inserted after 12 lines successfully!")

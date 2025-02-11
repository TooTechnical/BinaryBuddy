import os

# Check the directory structure of the BinaryBuddy project
for root, dirs, files in os.walk("/workspace/BinaryBuddy"):
    print(f"Directory: {root}")
    for file in files:
        print(f"  File: {file}")

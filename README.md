# sinhala-spell-checker
A spell checker for the Sinhala language built with Python

# Features
- Automatically fix spelling errors
- Provide word suggestions to fix spelling errors

# How it works
This script constructs a **trie** from the words listed in `data\dict.txt` and uses the Levenshtein distance algorithm to generate the most accurate suggestions for any misspelled word it detects.
Priority for letter modifications is given in the following order:
> 1. Adding/Removing/Modifying vowel marks (පිල්ලම්)
> 2. Changing Case of letter (මහාප්‍රාණ, මුර්ධජ)
> 3. Adding/Removing/Modifying letters

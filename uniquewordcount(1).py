# -*- coding: utf-8 -*-
"""UniqueWordCount(1).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/132f6MNPLTrxo7g-HWyRaOu_yS5h9aOYL
"""

!pip install mrjob

# @title Default title text
# Mapper function: Splits text into words and emits (word, 1) pairs
def mapper(text):
    words = text.split()
    for word in words:
        yield (word, 1)

# Reducer function: Aggregates word counts for each word
def reducer(word, counts):
    total_count = sum(counts)
    yield (word, total_count)

# Input file name
input_file = "UniqueWordCount(1)_Input.txt"

# List to store input data
input_data = []

# Read input data from the file
with open(input_file, "r") as file:
    for line in file:
        input_data.append(line)

# Dictionary to store word counts
word_counts = {}

# Map and Reduce
for line in input_data:
    for word, count in mapper(line):
        if word not in word_counts:
            word_counts[word] = []  # Initialize an empty list for the word if it's not in the dictionary
        word_counts[word].append(count)

result = {}

# Process the word counts and calculate the total count for each word
for word, counts in word_counts.items():
    for word, count in reducer(word, counts):
        result[word] = count

# Print the output
for word, count in result.items():
    print(f'"{word}" {count}')
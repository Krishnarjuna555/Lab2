# -*- coding: utf-8 -*-
"""WordCountWithStopwords(2).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KwMh5rVDxuBHurirIka8v37o_-IPh1r-
"""

# List of stopwords
stopwords = set(["the", "and", "of", "a", "to", "in", "is", "it"])

# Mapper function
def mapper(text):
    words = text.split()
    for word in words:
        if word.lower() not in stopwords:
            yield (word, 1)

# Reducer function
def reducer(word, counts):
    total_count = sum(counts)
    yield (word, total_count)

# Read input data from a file
input_file = "WordCountWithStopwords(2)_Input.txt"
input_data = []

with open(input_file, "r") as file:
    for line in file:
        input_data.append(line)

# Map and Reduce
word_counts = {}
for line in input_data:
    for word, count in mapper(line):
        if word not in word_counts:
            word_counts[word] = []
        word_counts[word].append(count)

result = {}
for word, counts in word_counts.items():
    for word, count in reducer(word, counts):
        result[word] = count

# Print the output
for word, count in result.items():
    print(f'"{word}" {count}')
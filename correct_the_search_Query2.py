import pickle
import zlib
from collections import Counter
import re

# Build corpus from a sample dictionary (you can enhance it with more words)
words = """going to china who was the first president of india winner of the match food in america"""

# Function to generate a list of words from text
def words_list(text):
    return re.findall(r'\w+', text.lower())

WORDS = Counter(words_list(words))

# Compression for large wordlist
with open('compressed_dict.pkl', 'wb') as f:
    compressed = zlib.compress(pickle.dumps(WORDS))
    f.write(compressed)

# Load dictionary from compressed file
def load_dictionary():
    with open('compressed_dict.pkl', 'rb') as f:
        return pickle.loads(zlib.decompress(f.read()))

# Generate all possible edits that are one edit distance away
def edit_distance_one(word):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes = [L + R[1:] for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1]
    replaces = [L + c + R[1:] for L, R in splits if R for c in letters]
    inserts = [L + c + R for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)

# Check which words are in the dictionary
def known(words, dictionary):
    return set(w for w in words if w in dictionary)

# Generate correction candidates for a word
def candidates(word, dictionary):
    return (known([word], dictionary) or
            known(edit_distance_one(word), dictionary) or
            [word])

# Find the best correction for a word
def correct_word(word, dictionary):
    return max(candidates(word, dictionary), key=dictionary.get)

# Correct an entire query
def correct_query(query, dictionary):
    return ' '.join(correct_word(word, dictionary) for word in query.split())

# Main function
if __name__ == "__main__":
    dictionary = load_dictionary()
    n = int(input())
    queries = [input().strip() for _ in range(n)]

    for query in queries:
        print(correct_query(query, dictionary))

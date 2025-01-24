import zlib
import pickle
from collections import Counter
import re

# Function to tokenize text
def tokenize(text):
    return re.findall(r'\b[a-z]+\b', text.lower())

# Build corpus and serialize it
def build_and_serialize_corpus():
    # Example corpus (replace with a real one)
    corpus_text = """going to china who was the first president of india winner of the match food in america"""
    word_list = tokenize(corpus_text)
    word_frequencies = Counter(word_list)
    
    # Serialize and compress the corpus
    compressed_corpus = zlib.compress(pickle.dumps(word_frequencies))
    with open("corpus.pkl", "wb") as f:
        f.write(compressed_corpus)

# Deserialize the corpus
def load_corpus():
    with open("corpus.pkl", "rb") as f:
        compressed_corpus = f.read()
    word_frequencies = pickle.loads(zlib.decompress(compressed_corpus))
    return word_frequencies

# Spell correction using edit distance
def edit_distance(word1, word2):
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
    return dp[m][n]

def correct_word(word, word_frequencies):
    if word in word_frequencies:
        return word
    candidates = [(candidate, edit_distance(word, candidate)) for candidate in word_frequencies]
    candidates.sort(key=lambda x: (x[1], -word_frequencies[x[0]]))
    return candidates[0][0] if candidates else word

# Correct query
def correct_query(query, word_frequencies):
    words = tokenize(query)
    corrected_words = [correct_word(word, word_frequencies) for word in words]
    return " ".join(corrected_words)

# Main
if __name__ == "__main__":
    build_and_serialize_corpus()  # Run once to create the serialized corpus
    word_frequencies = load_corpus()
    
    n = int(input())
    queries = [input().strip() for _ in range(n)]
    
    corrected_queries = [correct_query(query, word_frequencies) for query in queries]
    for corrected_query in corrected_queries:
        print(corrected_query)

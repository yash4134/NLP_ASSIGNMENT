import re

def load_dictionary(filepath):
    """Load words from the dictionary file."""
    with open(filepath, 'r') as f:
        return set(word.strip().lower() for word in f)

def clean_input(input_str):
    """Clean the input string by removing www, extensions, or #."""
    if input_str.startswith("#"):
        return input_str[1:]  # Remove the hashtag
    if input_str.startswith("www."):
        input_str = input_str[4:]  # Remove www
    input_str = re.sub(r'\.(com|org|net|edu|in|gov|info|io|co|uk|ru|cz|mil|cn|us)$', '', input_str)  # Remove extensions
    input_str = re.sub(r'\.tx\.', '', input_str)  # Handle .tx.us
    return input_str

def segment_string(s, dictionary):
    """Segment the input string into valid tokens based on the dictionary."""
    n = len(s)
    dp = [None] * (n + 1)  # dp[i] will store the segmentation up to index i
    dp[0] = []

    for i in range(1, n + 1):
        for j in range(i):
            word = s[j:i]
            if (word in dictionary) or (word.isdigit()):
                if dp[j] is not None:
                    if dp[i] is None or len(dp[j]) + 1 > len(dp[i]):  # Prefer longer splits
                        dp[i] = dp[j] + [word]

    return " ".join(dp[-1]) if dp[-1] else s

def main():
    # Load the dictionary
    dictionary = load_dictionary("words.txt")

    # Read input
    n = int(input().strip())
    inputs = [input().strip().lower() for _ in range(n)]

    # Process each input
    results = []
    for inp in inputs:
        cleaned_input = clean_input(inp)
        segmented = segment_string(cleaned_input, dictionary)
        results.append(segmented)

    # Output results
    for result in results:
        print(result)

if __name__ == "__main__":
    main()


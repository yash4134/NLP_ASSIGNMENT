# Define a function that segments a single hashtag into words
def segment_hashtag(hashtag, word_dict):
    n = len(hashtag)
    dp = [None] * (n + 1)
    dp[0] = []  # Base case: empty string can be segmented as an empty list
    
    # Iterate over the hashtag string
    for i in range(1, n + 1):
        for j in range(max(0, i - 20), i):  # Limit the length of words checked
            word = hashtag[j:i]
            if word in word_dict and dp[j] is not None:
                dp[i] = dp[j] + [word]
                break
    
    return " ".join(dp[n]) if dp[n] is not None else hashtag

# Main function to process input and output results
def process_hashtags(num_hashtags, hashtags, word_dict):
    result = []
    for hashtag in hashtags:
        segmented = segment_hashtag(hashtag, word_dict)
        result.append(segmented)
    return result

# Sample dictionary of common words (expand this as needed)
word_dict = {
    "we", "are", "the", "people", "mention", "your", "faves",
    "now", "playing", "walking", "dead", "follow", "me"
}

# Sample input
num_hashtags = int(input("Enter the number of hashtags: "))
hashtags = [input("Enter hashtag: ").strip() for _ in range(num_hashtags)]

# Process the hashtags and print the result
segmented_hashtags = process_hashtags(num_hashtags, hashtags, word_dict)
for segmented in segmented_hashtags:
    print(segmented)

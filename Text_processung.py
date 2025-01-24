import re

def count_articles_and_dates(fragment):
    """
    Count occurrences of 'a', 'an', 'the', and valid dates in a given text fragment.
    """
    # Normalize text for article counting
    lower_fragment = fragment.lower()

    # Count articles
    a_count = len(re.findall(r'\ba\b', lower_fragment))
    an_count = len(re.findall(r'\ban\b', lower_fragment))
    the_count = len(re.findall(r'\bthe\b', lower_fragment))

    # Identify valid dates
    date_patterns = [
        r'\b\d{1,2}(?:st|nd|rd|th)?(?:\s+of)?\s+(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{2,4}\b',  # Day Month Year
        r'\b(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2}(?:st|nd|rd)?,?\s+\d{2,4}\b',  # Month Day Year
        r'\b\d{1,2}/\d{1,2}/\d{2,4}\b',  # Day/Month/Year
        r'\b\d{4}-\d{2}-\d{2}\b'  # ISO format: Year-Month-Day
    ]

    # Combine all date patterns
    date_regex = '|'.join(date_patterns)
    dates = re.findall(date_regex, fragment, re.IGNORECASE)
    date_count = len(dates)

    return a_count, an_count, the_count, date_count

def main():
    import sys
    input = sys.stdin.read

    # Read input data
    data = input().strip().split("\n")
    t = int(data[0])  # Number of test cases

    fragments = data[1:]  # Remaining lines contain the fragments

    results = []
    for i in range(t):
        fragment = fragments[i].strip()
        # Count articles and dates
        a_count, an_count, the_count, date_count = count_articles_and_dates(fragment)
        results.append(f"{a_count}\n{an_count}\n{the_count}\n{date_count}")

    # Output results
    print("\n".join(results))

if __name__ == "__main__":
    main()

import re

def extract_acronyms_and_expansions(snippets):
    """
    Extract acronyms and their expansions from the provided snippets.
    """
    acronym_dict = {}

    for snippet in snippets:
        # Find all potential acronyms (uppercase words typically enclosed in parentheses)
        matches = re.findall(r'\((\b[A-Z]+\b)\)', snippet)
        for match in matches:
            # Extract the preceding text (potential expansion)
            preceding_text = snippet.split(f"({match})")[0].strip()

            # Look for the last meaningful phrase before the acronym
            expansion_candidates = re.split(r'[.,;:-]', preceding_text)
            if expansion_candidates:
                expansion = expansion_candidates[-1].strip()
                acronym_dict[match] = expansion

        # Additionally, handle acronyms not in parentheses but defined explicitly
        words = snippet.split()
        for i, word in enumerate(words):
            if word.isupper() and len(word) > 1:  # Likely an acronym
                if word not in acronym_dict:
                    # Try to extract its expansion from the surrounding context
                    if i > 0:
                        preceding_context = " ".join(words[max(0, i - 5):i])
                        if preceding_context:
                            acronym_dict[word] = preceding_context

    return acronym_dict

def process_tests(acronym_dict, tests):
    """
    Process test acronyms and return their expansions.
    """
    results = []
    for test in tests:
        # Normalize the test acronym (case insensitive)
        expansion = acronym_dict.get(test.upper(), "Not Found")
        results.append(expansion)
    return results

def main():
    # Read number of snippets
    n = int(input().strip())
    snippets = [input().strip() for _ in range(n)]
    
    # Read the test acronyms
    tests = []
    while True:
        try:
            test = input().strip()
            tests.append(test)
        except EOFError:
            break
    
    # Extract acronyms and expansions
    acronym_dict = extract_acronyms_and_expansions(snippets)

    # Process test queries
    results = process_tests(acronym_dict, tests)

    # Output results
    for result in results:
        print(result)

if __name__ == "__main__":
    main()

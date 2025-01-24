def build_model():
    """Build a simple keyword-based model."""
    return {
        "computer-mouse": [
            "click", "device", "input", "usb", "cursor", "scroll", "hardware", "dpi", "computer", "keyboard", "monitor"
        ],
        "animal": [
            "tail", "fur", "rodent", "cheese", "species", "habitat", "predator", "mammal", "wild", "genome", "postnatal"
        ]
    }

# Classify a sentence
def classify_sentence(sentence, model):
    """Classifies the sentence based on keyword matching."""
    # Normalize sentence
    sentence = sentence.lower()
    # Count keyword matches
    computer_mouse_score = sum(1 for word in model["computer-mouse"] if word in sentence)
    animal_score = sum(1 for word in model["animal"] if word in sentence)
    
    # Return the class with the higher score
    return "computer-mouse" if computer_mouse_score > animal_score else "animal"

# Main function
def main():
    # Build the model in-memory
    model = build_model()

    # Input
    n = int(input().strip())
    sentences = [input().strip() for _ in range(n)]

    # Classify each sentence
    results = [classify_sentence(sentence, model) for sentence in sentences]

    # Output results
    for result in results:
        print(result)

if __name__ == "__main__":
    main()

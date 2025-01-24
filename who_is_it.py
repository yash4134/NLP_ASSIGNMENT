import re

def resolve_pronouns(text, entities):
    # Extract all pronouns and their positions
    pronoun_pattern = r'\\(\w+)\\'
    pronouns = [(match.group(1), match.start()) for match in re.finditer(pronoun_pattern, text)]
    
    # Clean the text by removing ** markers
    clean_text = re.sub(r'\\(\w+)\\', r'\1', text)
    
    # Initialize a list to store the resolved entities
    resolved = []
    
    # For each pronoun, find the corresponding entity
    for pronoun, pos in pronouns:
        closest_entity = None
        closest_distance = float('inf')
        
        # Iterate through all entities to find the best match
        for entity in entities:
            # Find the last occurrence of the entity before the pronoun
            entity_pos = clean_text.rfind(entity, 0, pos)
            if entity_pos != -1:
                distance = pos - (entity_pos + len(entity))
                if distance < closest_distance:
                    closest_distance = distance
                    closest_entity = entity
        
        # Append the resolved entity to the list
        resolved.append(closest_entity)
    
    return resolved

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split("\n")
    
    # Read the number of lines in the text snippet
    n = int(data[0])
    
    # Combine the next N lines into the full text

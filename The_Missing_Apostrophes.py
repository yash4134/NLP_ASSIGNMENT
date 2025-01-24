import re

# Function to handle apostrophes for contractions and possessives
def restore_apostrophes(text):
    restored_text = []
    words = text.split()
    
    for word in words:
        lower_word = word.lower()

        # Handle contractions
        if lower_word == "dont":
            restored_text.append("don't")
        elif lower_word == "wont":
            restored_text.append("won't")
        elif lower_word == "cant":
            restored_text.append("can't")
        elif lower_word == "isnt":
            restored_text.append("isn't")
        elif lower_word == "arent":
            restored_text.append("aren't")
        elif lower_word == "wasnt":
            restored_text.append("wasn't")
        elif lower_word == "werent":
            restored_text.append("weren't")
        elif lower_word == "hasnt":
            restored_text.append("hasn't")
        elif lower_word == "havent":
            restored_text.append("haven't")
        elif lower_word == "hadnt":
            restored_text.append("hadn't")
        elif lower_word == "didnt":
            restored_text.append("didn't")
        elif lower_word == "ive":
            restored_text.append("I've")
        elif lower_word == "youve":
            restored_text.append("you've")
        elif lower_word == "hes":
            restored_text.append("he's")
        elif lower_word == "shes":
            restored_text.append("she's")
        elif lower_word == "its" and "'" not in word:
            restored_text.append("it's")
        elif lower_word == "were" and "'" not in word:
            restored_text.append("we're")
        elif lower_word == "id":
            restored_text.append("I'd")
        elif lower_word == "hed":
            restored_text.append("he'd")
        elif lower_word == "shed":
            restored_text.append("she'd")
        elif lower_word == "wed":
            restored_text.append("we'd")
        elif lower_word == "theyd":
            restored_text.append("they'd")
        elif lower_word == "ill":
            restored_text.append("I'll")
        elif lower_word == "youll":
            restored_text.append("you'll")
        elif lower_word == "hell":
            restored_text.append("he'll")
        elif lower_word == "shell":
            restored_text.append("she'll")
        elif lower_word == "well":
            restored_text.append("we'll")
        elif lower_word == "theyll":
            restored_text.append("they'll")
        elif lower_word == "id":
            restored_text.append("I'd")
        elif lower_word == "im":
            restored_text.append("I'm")
        
        # Handle possessives (only add 's when it makes sense)
        elif re.match(r'\w+s$', word) and lower_word not in ["its", "hers", "ours", "yours", "theirs"]:
            restored_text.append(re.sub(r"s$", "'s", word))
        
        # For normal words that don't need apostrophes, keep them as is
        else:
            restored_text.append(word)
    
    return " ".join(restored_text)

# Input text
input_text = """At a news conference Thursday at the Russian manned-space facility in Baikonur, Kazakhstan, 
Kornienko said "we will be missing nature, we will be missing landscapes, woods." He admitted that on his 
previous trip into space in 2010 "I even asked our psychological support folks to send me a calendar with 
photographs of nature, of rivers, of woods, of lakes."   
Kelly was asked if hed miss his twin brother Mark, who also was an astronaut.   
"Were used to this kind of thing," he said. "Ive gone longer without seeing him and it was great."   
The mission wont be the longest time that a human has spent in space - four Russians spent a year or more aboard the 
Soviet-built Mir space station in the 1990s."""

# Restore apostrophes
output_text = restore_apostrophes(input_text)
print(output_text)

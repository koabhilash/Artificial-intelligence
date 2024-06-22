import itertools

# Helper function to convert a word to its numerical equivalent
def word_to_number(word, mapping):
    return int(''.join(str(mapping[char]) for char in word))

def solve_cryptarithmetic():
    # Words involved in the equation
    words = ['SEND', 'MORE', 'MONEY']
    
    # All the unique characters in the equation
    unique_chars = set(''.join(words))
    
    if len(unique_chars) > 10:
        print("Too many unique characters for a valid solution.")
        return

    # All possible permutations of digits 0-9 for these characters
    digits = range(10)
    for perm in itertools.permutations(digits, len(unique_chars)):
        # Create a dictionary mapping each character to a digit
        mapping = dict(zip(unique_chars, perm))
        
        # Check for leading zero in any word
        if any(mapping[word[0]] == 0 for word in words):
            continue

        # Convert words to their numerical equivalents
        send = word_to_number('SEND', mapping)
        more = word_to_number('MORE', mapping)
        money = word_to_number('MONEY', mapping)
        
        # Check if the equation SEND + MORE = MONEY holds
        if send + more == money:
            print(f"SEND + MORE = MONEY")
            print(f"{send} + {more} = {money}")
            print("Mapping:", mapping)
            return
    
    print("No solution found.")

solve_cryptarithmetic()

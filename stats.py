def get_num_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    char_count={ }


    for letters in text:
        letter=letters.lower()
        if letter in char_count:
            char_count[letter] +=1
        else:
            char_count[letter] = 1
    return char_count

def sort_character_counts(char_count_dict):
    # Filter out non-alphabetical characters and create a list of dictionaries
    filtered_counts = [
        {'character': char, 'count': count}
        for char, count in char_count_dict.items() if char.isalpha()
    ]
    
    # Sort the list from greatest to least by count
    filtered_counts.sort(key=lambda x: x['count'], reverse=True)
    
    return filtered_counts
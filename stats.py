def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    text_dict = {}
    for char in text:
        if char.lower() in text_dict:
            text_dict[char.lower()] += 1
        else:
            text_dict[char.lower()] = 1
    return text_dict
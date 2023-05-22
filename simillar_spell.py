import Levenshtein

def extract_words(text):
    """Extract words from text and return them as a list"""
    return text.lower().split()

def find_similar_words(word, word_list, threshold):
    """Find words in word_list that are similar to word within a given threshold"""
    similar_words = []
    for w in word_list:
        distance = Levenshtein.distance(word, w)
        if distance <= threshold:
            similar_words.append(w)
    return similar_words

def main():
    # Open text file and read its contents
    with open("/content/example.txt", "r",encoding="utf-8") as f:
        text = f.read()
    
    # Extract words from text
    word_list = extract_words(text)
    
    # Find similar words for each word in the list
    threshold = 1
    similar_words_dict = {}
    for word in word_list:
        similar_words = find_similar_words(word, word_list, threshold)
        similar_words_dict[word] = similar_words
    
    # Print results
    for word, similar_words in similar_words_dict.items():
        print(f" '{word}' {threshold}: {similar_words}")

if __name__ == "__main__":
    main()

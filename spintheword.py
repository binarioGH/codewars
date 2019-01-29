def spin_words(sentence):
    words = []
    for word in sentence.split():
        if len(word) >= 5:
            word = word[::-1]
        words.append(word)
    return " ".join(words)
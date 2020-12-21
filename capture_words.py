def format_word_from_file(word):
    word = word.replace('\n', '')

    return word

def capture_words_from_file(path):
    final_words = []

    with open(path, 'r') as file:
        words = file.readlines()

        for word in words:
            word = format_word_from_file(word)
            final_words.append(word)
        
    return final_words


if __name__ == '__main__':
    print(capture_words_from_file('./all_words.txt'))
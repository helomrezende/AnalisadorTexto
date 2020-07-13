from pathlib import Path

word_counter = {}

def count_line_words(str):
    words = str.split(" ")
    for word in words:
        new_word = word.lower().strip()
        if (new_word in word_counter):
            word_counter[new_word] += 1            
        else:
             word_counter[new_word] = 1
    return word_counter

def count_file_words(file):
    path = Path(__file__).parent.parent    
    file = open(str(path) + "/" + file, encoding="utf-8")
    for line in file:
        count_line_words(line)
    file.close()
    return word_counter
    
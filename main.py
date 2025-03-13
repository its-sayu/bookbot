def get_book_text(filepath):
    with open(filepath) as f:
        file_contents=f.read()
    return file_contents

from stats import get_num_words
from stats import get_num_char



def main():
    text= get_book_text('books/frankenstein.txt')
    words=len(get_num_words(text))
    print(words, "words found in the document")
    

    x=get_num_char(text)
    print(x)

    return 

main()


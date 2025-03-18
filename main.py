def get_book_text(filepath):
    with open(filepath) as f:
        file_contents=f.read()
    return file_contents

import sys
from stats import get_num_words
from stats import get_num_char
from stats import sort_dict
from stats import sort_on

def main():
    try:
        filepath=sys.argv[1]
    except:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    print("Analyzing book found at", filepath,"...")
    text= get_book_text(filepath)
    words=len(get_num_words(text))
    print("----------- Word Count ----------")
    print("Found", words, "total words")
    
    print("--------- Character Count -------")
    x=get_num_char(text)
    sort_dict(x)
    print("============= END ===============")
    return 

main()


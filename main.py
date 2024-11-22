def get_book(book):

    loc = 'books/'+book+'.txt'

    with open(loc) as f:
        file_contents = f.read()

    return loc, file_contents

def count_words(text: str):
    return len(text.split())

def count_characters(text: str) -> dict:
    count_dict = {}

    for i in text.lower():
        if ord(i) >= 97 and ord(i) <= 122:
            if i in count_dict:
                count_dict[i] += 1
            else:
                count_dict[i] = 1
        else:
            pass
    
    print(count_dict)
    return count_dict

def create_report(book):
    loc, text = get_book(book)

    print(f"--- Begin report of {loc} ---")
    print(f"{count_words(text)} words found in the document\n")

    for character,count in count_characters(text).items():
        print(f"The '{character}' was found {count} times")

    print("--- End report ---")

if __name__ == "__main__":

    book = 'frankenstein'

    create_report(book)
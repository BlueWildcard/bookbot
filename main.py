def read_book(file_path):
    with open(file_path) as f:
        return f.read()
    
def count_words(content):
    words = content.split()
    #print(f"number of words in text {len(words)}")
    return len(words)
    
def count_chars(content):   
    char_count = dict() 
    num_list = list()
    words = content.split()
    for word in words:
        for char in word:
            char = char.lower()
            if not char.isalpha():
                continue
            elif char not in char_count:
                char_count[char] = 1
            else:
                char_count[char] += 1
    for char in char_count:
        num_list.append(char_count[char])
    num_list.sort(reverse=True)
    #print(num_list)
    print("number of each char in text:")
    for num in num_list:
        for char in char_count:
            if num == char_count[char]:
                print(f"{char}: {num}")
    #print(f"count of each char in text:\n{char_list}")    

    
def main():
    book = read_book("./books/frankenstein.txt")    
    word_count = count_words(book)
    print(f"number of words in text {word_count}")
    count_chars(book)
    
main()
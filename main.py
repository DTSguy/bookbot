def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents
def main():
    path_to_file = '/mnt/c/Users/jblaser/scripts/bookbot/books/frankenstein.txt'
    book_text = get_book_text(path_to_file)
    print(f'{book_text}')

if __name__ == '__main__':
    main()

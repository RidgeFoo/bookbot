def main():
    book_path = "books/frankenstein.txt"
    file_contents = get_text(book_path)
    num_words = count_words(file_contents)
    tally_of_chars = count_characters(file_contents)
    sorted_tally = sort_tally(tally_of_chars)
    generate_report(sorted_tally, num_words, book_path)

def generate_report(sorted_tally: dict, num_of_words: int, path: str) -> None:
    print(f"--- Begin report of {path} ---")
    print(f"{num_of_words} words found in the document \n")
    for x in sorted_tally:
        print(f"The '{x['char']}' char was found {x['count']} times")
    print("--- End report ---")


def sort_tally(dict_of_chars: dict) -> list:
    l = [{"char": k, "count": v} for k, v in dict_of_chars.items() if k.isalpha()]
    l.sort(reverse=True, key=lambda x: x["count"])
    return l


def get_text(path):
    with open(path, "r") as f:
        file_contents = f.read()
    return file_contents


def count_words(string: str) -> int:
    return len(string.split())


def count_characters(string: str) -> dict:
    tally = {}
    lowered = string.lower()
    for char in lowered:
        if char not in tally:
            tally[char] = 1
        else:
            tally[char] += 1
    return tally


if __name__ == "__main__":
    main()

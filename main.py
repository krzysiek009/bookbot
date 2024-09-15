def sortBy(tup):
    return tup[1]

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

        words = file_contents.split()

        # print(len(words))

        lowercase = file_contents.lower()
        character_counts = {}

        for character in lowercase:
            if character.isalpha():
                try:
                    character_counts[character] += 1
                except KeyError:
                    character_counts[character] = 1

        character_count_list = []

        for key in character_counts:
            character_count_list.append((key, character_counts[key]))

        character_count_list.sort(key=sortBy, reverse=True)
        
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{len(words)} words found in the document\n")
        for row in character_count_list:
            print(f"The '{row[0]}' character was found {row[1]} times")
        print("--- End report ---")

main()

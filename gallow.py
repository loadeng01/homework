words = ["книга", "ноутбук", "фильм", "аппарат", "интерстеллар", "симфония", "камикадзе", "кинотеатр"]

def game(word: str, dots: list):
    count = 0
    attempt = 3
    print("Количество попыток: ", attempt)
    print(''.join(dots))
    while True:
        letter = input("Буква: ").lower()
        
        if letter in word:
            if word.count(letter) == 1:
                index = word.index(letter)
                dots.pop(index)
                dots.insert(index, letter)
                print("".join(dots))
                count += 1
            elif word.count(letter) > 1:
                index = [i for i, c in enumerate(word) if c == letter]
                for i in index:
                    dots.pop(i)
                    dots.insert(i, letter)
                count += word.count(letter)
                print("".join(dots))
        else:
            attempt -= 1
            print("Этой буквы нет в этом слове")
            print("Количество попыток: ", attempt)

        if count == len(word):
            print("Поздравляю, вы победили")
            break
        elif attempt == 0:
            print("Игра окончена")
            break


def get_word(words: list) -> str:
    import random
    return str(random.choices(words))[2:-2]


def get_dots(word: str) -> list:
    dots = []
    
    for i in range(len(word)):
        dots += ['*']

    return dots


def main():
    word = get_word(words)
    dots = get_dots(word)
    game(word, dots)

main()

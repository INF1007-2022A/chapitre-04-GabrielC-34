#!/usr/bin/env python
# -*- coding: utf-8 -*-


def is_even_len(string: str) -> bool:
    if (len(string)%2) == 0:
        isEven = True
    else:
        isEven = False
    return isEven



def remove_third_char(string: str) -> str:
    charList = list(string)
    charList.pop(2)
    string = ''
    string = string.join(charList)
    return string


def replace_char(string: str, old_char: str, new_char: str) -> str:
    string = string.replace(old_char, new_char)
    return string


def get_number_of_char(string: str, char: str) -> int: #La chaîne complète est "Hello World", on doit faire quoi??
    nbrIterance = 0
    for c in string:
        if c == char:
            nbrIterance+=1
    return nbrIterance


def get_number_of_words(sentence: str, word: str) -> int:
    return sentence.count(word)


def main() -> None:
    chaine = "Bonjour!"
    if is_even_len(chaine):
        print(f"Le nombre de caractère dans la chaine {chaine} est pair")
    else:
        print(f"Le nombre de caractère dans la chaine {chaine} est impair")

    chaine = "salut monde!"
    print(f"On supprime le 3e caratère dans la chaine: {chaine}. Résultat : {remove_third_char(chaine)}")

    chaine = "hello world!"
    print(f"On remplace le caratère w par le caractère z dans la chaine: {chaine}. Résultat : {replace_char(chaine, 'w', 'z')}")

    print(f"Le nombre d'occurrence de l dans hello est : {get_number_of_char(chaine, 'l')}")
    
    chaine = "Baby shark doo doo doo doo doo doo"
    print(f"L'occurence du mot doo dans la chaine {chaine} est: {get_number_of_words(chaine, 'doo')}")


if __name__ == '__main__':
    main()

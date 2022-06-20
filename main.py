import pandas as pd

# The CSV file is converted to a dictionary having an uppercase letter as Key and its associated word as Value
# The variable name "phonetic_dict" is common in both functions ("using_itertuples" and "without_itertuples") and it stores the above dictionary.
# The result function takes this dictionary and the user inputted word as arguments and returns a list having associated word for each letter in the word.


def using_itertuples(data: pd.DataFrame, word: str) -> None:
    phonetic_dict = {letter: code for (letter, code) in data.itertuples(index=False)}
    result(phonetic_dict, word)


def without_itertuples(data: pd.DataFrame, word: str) -> None:
    data_dict = data.to_dict()
    phonetic_dict = {data_dict['letter'][index]: data_dict['code'][index] for index in data_dict['letter']}
    result(phonetic_dict, word)


def result(new_dict: dict, word: str) -> None:
    new_list = [new_dict[letter.upper()] for letter in word]
    print(new_list)


def main():
    user_choice = input('Enter a word: ')
    data = pd.read_csv('nato_phonetic_alphabet.csv')
    mode = input('Type "y" or "yes" to user itertuples (Default is "no"): ').lower()
    if mode == 'y' or mode == 'yes':
        using_itertuples(data, user_choice)
    else:
        without_itertuples(data, user_choice)

if __name__ == '__main__':
    main()

"""
File: boggle.py
Name:
----------------------------------------
TODO:
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
    """
	TODO:
	"""
    # start = time.time()
    ####################
    name_list = read_dictionary(FILE)
    row = 1
    row_letter = []
    while row <= 4:
        letter = input(str(row) + " row of letters: ")
        letter.split()
        if len(letter.split()) != 4:
            print("Illegal Input")
            continue
        for ch in letter.split():
            if len(ch) > 1:
                print("Illegal Input")
                break
        row_letter.append(letter.lower().split())
        row += 1
    start = time.time()
    # row_letter = [["f", "y", "c", "l"], ["i", "o", "m", "g"], ["o", "r", "i", "l"], ["h", "j", "h", "u"]]
    find_words(row_letter, name_list)
    ####################
    end = time.time()
    print('----------------------------------')
    print(f'The speed of your boggle algorithm: {end - start} seconds.')


def read_dictionary(file):
    """
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
    name_list = {}
    with open(file, "r") as f:
        for line in f:
            if len(line) >= 5:
                if line[0] in name_list:
                    name_list[line[0]].append(line[:-1])
                else:
                    name_list[line[0]] = [line[:-1]]
    return name_list


def has_prefix(sub_s, name_dict, ans_word):
    """
	:param ans_word: (list) The word satisfies the request
	:param name_dict: (dict) the dict stores prefix and the total names
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
    # if sub_s[0] in name_list:
    # 	for name in name_list[sub_s[0]]:
    # 		if name.startswith(sub_s):
    # 			# if sub_s == name and sub_s not in ans_word:
    # 			# 	print("Found \""+sub_s+"\"")
    # 			# 	ans_word.append(sub_s)
    # 			return True
    # return False
    left, right = 0, len(name_dict[sub_s[0]]) - 1
    while right >= left:
        mid = (right + left) // 2
        word = name_dict[sub_s[0]][mid]
        if word.startswith(sub_s):
            return True
        elif word < sub_s:
            # print(word, sub_s)
            left = mid + 1
        else:
            right = mid - 1
    return False


def find_words(row_letter, name_list):
    ans_word = []  # list to store ans
    x_y = []
    word = ''
    for x in range(4):
        for y in range(4):
            find_words_helper(row_letter, x, y, name_list, word, ans_word, x_y)
    print("There are " + str(len(ans_word)) + " words in total.")


def find_words_helper(row_letter, x, y, name_list, word, ans_word, x_y):
    if word:
        for name in name_list[word[0]]:
            if word == name and word not in ans_word:  # check if the sub_s == name and not exist in the ans_word yet
                print("Found \"" + word + "\"")
                ans_word.append(word)
    for i in range(-1, 2):
        for j in range(-1, 2):
            new_x = x + i
            new_y = y + j
            if (new_x, new_y) not in x_y:
                if 0 <= new_x <= 3 and 0 <= new_y <= 3:
                    word += row_letter[new_x][new_y]
                    x_y.append((new_x, new_y))
                    if has_prefix(word, name_list, ans_word):
                        find_words_helper(row_letter, new_x, new_y, name_list, word, ans_word, x_y)
                    word = word[:-1]
                    x_y.pop()


if __name__ == '__main__':
    main()

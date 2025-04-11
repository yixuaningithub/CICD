"""
File: boggle.py
Name: Lulu
----------------------------------------
This project will find all English words that exist on the 4 x 4 board.
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]


def main():
	"""
	This function will find and print all English words
	that exist on the 4 x 4 board.
	"""
	####################
	board = []
	for i in range(4):
		row = input(f"{i+1} row of letters: ").strip().lower().split()
		if len(row) != 4:
			print("Illegal input")
			return
		board.append(row)
	start = time.time()
	word_dict = read_dictionary()
	words_found = find_words(board, word_dict)
	num_words = len(words_found)
	print(f"There are {num_words} words in total.")
	####################
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	word_dict = {}
	with open(FILE, 'r') as file:
		for line in file:
			word = line.strip().lower()
			key = word[0]  			# Take the first letter as key
			if key not in word_dict:
				word_dict[key] = []
			word_dict[key].append(word)
	return word_dict


def has_prefix(sub_s, word_dict):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:param word_dict: (dict) A dictionary that stores words, with the first letter as the key
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	if not sub_s:
		return False
	key = sub_s[0]
	if key in word_dict:
		for word in word_dict[key]:
			if word.startswith(sub_s):
				return True
	return False


def find_words(board, word_dict):
	"""
	:param board: (list)A list containing 4 rows and 4 columns of letters, representing an alphabet board.
	:param word_dict: (dict) A dictionary that stores words, with the first letter as the key.
	:return: (list) A list of all words found.
	"""
	words_found = []
	visited = [False] * 16  # Track whether a letter has been used
	for i in range(4):
		for j in range(4):
			visited[i * 4 + j] = True
			find_words_helper(board, word_dict, visited, i, j, [board[i][j]], words_found)
			visited[i * 4 + j] = False
	return words_found


def find_words_helper(board, word_dict, visited, row, col, path, words_found):
	"""
	:param board: (list)A list containing 4 rows and 4 columns of letters, representing an alphabet board.
	:param word_dict: (dict) A dictionary that stores words, with the first letter as the key.
	:param visited: (list) A boolean list of length 16 used to track whether each position on the alphabet has been visited.
	:param row: (int) Currently processed alphabet row index.
	:param col: (int) Currently processed alphabet row index.
	:param path:The (list) Character list of the word that has been formed.
	:param words_found: (list) Stores a list of all words found.
	"""
	word = ''.join(path)
	if len(word) >= 4 and word in word_dict.get(word[0], []):
		if word not in words_found:
			words_found.append(word)
			print(f"Found: \"{word}\"")
	for dr, dc in DIRECTIONS:
		nr, nc = row + dr, col + dc
		if 0 <= nr < 4 and 0 <= nc < 4 and not visited[nr * 4 + nc]:
			visited[nr * 4 + nc] = True
			path.append(board[nr][nc])
			if has_prefix(''.join(path), word_dict):
				find_words_helper(board, word_dict, visited, nr, nc, path, words_found)
			path.pop()
			visited[nr * 4 + nc] = False


if __name__ == '__main__':
	main()

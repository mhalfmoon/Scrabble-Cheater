import sys
from itertools import permutations

input_str = sys.argv
def get_all_substrings(string):
	length = len(string)
	alist = []
	for i in xrange(length):
		for j in xrange(i,length):
			alist.append(string[i:j + 1]) 
	return alist
    
def scrabble(input_str):
	lex = open('sowpods.txt')
	scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
		"f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
		"l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
		"r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
	"x": 8, "z": 10}
	
	initial_list = get_all_substrings(input_str)
	word_list = []
	for word in initial_list:
		word_list .extend([''.join(p) for p in permutations(word.lower())])
	word_list = list(set(word_list))
	
	lines = []
	
	for line in lex:
		lines.append(line.lower().strip())
		
	for word in word_list:
		score = 0
		for l in lines:
			if repr(word) == repr(l):
				for letter in word:
					for k, v in scores.iteritems():
						if repr(letter) == repr(k):
							score += v
						else:
							score += 0
		if score > 0:
			print score, word
				
     
def main(args):
	scrabble(args[1])
	
if __name__ == '__main__':
  main(sys.argv)

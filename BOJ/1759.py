from itertools import combinations
L, C = map(int, input().split())
letters = list(input().split())
letters.sort()

vowels = ['a', 'e', 'i', 'o', 'u']
answers = []

for case in combinations(letters, L):
    count_vowels = 0
    count_consonants = 0

    for ch in case:
        if ch in vowels:
            count_vowels += 1
        else:
            count_consonants += 1

    if count_vowels >= 1 and count_consonants >= 2:
        answers.append(''.join(case))

print(*answers, sep='\n')
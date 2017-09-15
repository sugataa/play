from collections import defaultdict
ms_questions = defaultdict(str)
apple_questions = defaultdict(str)
common = defaultdict(str)

with open('microsoft.txt') as f:
    for line in f:
        question_lst = line.strip().split(' ', 1)
        number = question_lst[0]
        meta = question_lst[1]
        ms_questions[number] = meta
with open('apple.txt') as f:
    for line in f:
        question_lst = line.strip().split(' ', 1)
        number = question_lst[0]
        meta = question_lst[1]
        if number in ms_questions:
            common[number] = meta
            del ms_questions[number]
        else:
            apple_questions[number] = meta

def print_stats(d):
    print('\n', len(d.items()), 'Questions', '\n')
    for key, value in d.items():
        print(key, value)

print_stats(common)
print_stats(ms_questions)
print_stats(apple_questions)

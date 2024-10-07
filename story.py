import os
import sys


def clear_file():
    open('story.txt', 'w').close()


def count_words(text):
    story_lines = ''
    with open(f'{text}', 'r') as story:
        for line in story:
            story_lines += line
    word_lis = story_lines.split(' ')
    #print(word_lis)
    return len(word_lis) - 1


def count_sen():
    story = open('story.txt', 'r')
    sen_lis = story.split('.')
    return len(sen_lis)

texts = ['story10.txt', 'story5.txt', 'story1.txt', 'story0.5.txt', 'story0.1']

if sys.argv[1] == 'count':
    for text in texts:
        print(count_words(text))
elif sys.argv[1] == 'clear':
    clear_file()

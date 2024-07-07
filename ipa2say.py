#!/usr/bin/python3

# adapted from https://superuser.com/questions/814510/how-can-you-make-os-xs-say-command-speak-ipa-characters

import sys

map = {
    'æ': 'AE',
    'eɪ': 'EY',
    'ɑ': 'AO',
    'əˈ': 'AX',
    'i': 'IY',
    'ɛ': 'EH',
    'ɪ': 'IH',
    'aɪ': 'AY',
    'ɪ': 'IX',
    'ɑ': 'AA',
    'u': 'UW',
    'ʊ': 'UH',
    'ʌ': 'UX',
    'oʊ': 'OW',
    'aʊ': 'AW',
    'ɔɪ': 'OY',
    'b': 'b',
    'ʧ': 'C',
    'd': 'd',
    'ð': 'D',
    'f': 'f',
    'g': 'g',
    'h': 'h',
    'ʤ': 'J',
    'k': 'k',
    'l': 'l',
    'm': 'm',
    'n': 'n',
    'ŋ': 'N',
    'p': 'p',
    'r': 'r',
    's': 's',
    'ʃ': 'S',
    't': 't',
    'θ': 'T',
    'v': 'v',
    'w': 'w',
    'j': 'y',
    'z': 'z',
    'ʒ': 'Z',
    'ɜ': '',
    ' ': ' ',
    'ˈ': ''
}

text = sys.stdin.read()
print('[[inpt PHON]]', end='')

substring = ''

for c in text:
    substring += c
    
    if len(substring) >= 2:
        if substring in map:
            print(map[substring], end='')
        else:
            front = substring[0]
            if front in map:
                print(map[front], end='')
            if len(substring) > 1:  # Add this check to ensure there is a second character
                back = substring[1]
                if back in map:
                    print(map[back], end='')
        
        substring = ''

if substring:
    front = substring[0]
    if front in map:
        print(map[front], end='')

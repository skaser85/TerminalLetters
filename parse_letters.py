from typing import List
from dataclasses import dataclass, field

@dataclass
class Character:
    character: str
    description: str
    rows: List[str] = field(default_factory=list)

letters = []

with open('letters.txt', 'r') as f:
    data = f.read().splitlines()
    curr_char = ''
    for line in data:
        if line.startswith('==='):
            char = line[3]
            description = line[5:]
            if char != curr_char:
                curr_char = Character(char, description)
                letters.append(curr_char)
        else:
            if curr_char != '':
                chars = [char for char in line]
                if len(chars) != 6:
                    raise ValueError(f'Uh-uh: {curr_char.character} {chars}')
                curr_char.rows.append(chars)

def print_text(text: str) -> None:
    text_letters = [[] for t in text]
    for i, char in enumerate(text):
        letter = [l for l in letters if l.character == char][0]
        for k in range(len(letter.rows)):
            text_letters[i].append(''.join(letter.rows[k]))

    lines = ['' for r in range(len(text_letters[0]))]
    for i, line in enumerate(lines):
        for k, t in enumerate(text_letters):
            line += t[i]
        print(line)

print_text('AaBbCcDdEeFfGgHhIiJjKkLlMm')
print_text('NnOoPpQqRrSsTtUuVvWwXxYyZz')
print_text(' .,!#<>-')
print_text('The Quick Brown Fox Jumps')
print_text('Over The Lazy Dog!')
print_text('doot doot')
print_text('Hello, world!')
print_text('1,808,123,456')
print_text('937-214-3392')

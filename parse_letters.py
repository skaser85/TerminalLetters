from typing import List
from dataclasses import dataclass, field

@dataclass
class Letter:
    letter: str
    rows: List[str] = field(default_factory=list)

letters = []

with open('letters.txt', 'r') as f:
    data = f.read().splitlines()
    curr_letter = ''
    for line in data:
        if line.startswith('==='):
            if line[3] != curr_letter:
                curr_letter = Letter(line[3])
                letters.append(curr_letter)
        else:
            if curr_letter != '':
                chars = [char for char in line]
                if len(chars) != 6:
                    raise ValueError(f'Uh-uh: {curr_letter.letter} {chars}')
                curr_letter.rows.append(chars)

# for letter in letters:
#     if len(letter.rows) > 0:
#         print(letter.letter)
#         for row in letter.rows:
#             print(''.join(row))

def print_text(text: str) -> None:
    text_letters = [[] for t in text]
    for i, char in enumerate(text):
        letter = [l for l in letters if l.letter == char][0]
        for k in range(len(letter.rows)):
            text_letters[i].append(''.join(letter.rows[k]))

    lines = ['' for r in range(len(text_letters[0]))]
    for i, line in enumerate(lines):
        for t in text_letters:
            line += t[i]
        print(line)

print_text('back')

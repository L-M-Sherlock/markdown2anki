import re
import utils


note_path = "./Basic/近世代数note.md"
with open(note_path, 'r', encoding='UTF-8') as note_file:
    cards = []
    lines = note_file.readlines()
    for line in lines:
        if line == '\n':
            continue
        elif '#' in line:
            title = line.replace('#', '')
            title = title.strip()
        else:
            Q = re.search(r'(?<=Q：).*?(?=A：)', line)
            A = re.search(r'(?<=A：).*?(?=\n)', line)
            if Q is None or A is None:
                continue
            Q = Q.group()
            A = A.group()
            Q = re.sub(r'\$(.*?)\$', utils.replace_formula, Q)
            A = re.sub(r'\$(.*?)\$', utils.replace_formula, A)
            card = Q + '\t' + title + '\t' + A + '\n'
            cards.append(card)

with open('./Basic/anki_basic.txt', 'w', encoding='UTF-8') as txt_file:
    txt_file.writelines(cards)

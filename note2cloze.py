import re
import utils


note_path = "./Cloze/计算机组成原理Note.md"
with open(note_path, 'r', encoding='UTF-8') as note_file:
    cards = []
    lines = note_file.readlines()
    for line in lines:
        if line == '\n':
            continue
        elif '#' in line:
            title = line.replace('#', '')
            title = title.strip()
        elif '**' in line:
            Cloze = line.replace('\n', '')
            Cloze = re.sub(r'\$(.*?)\$', utils.replace_formula, Cloze)
            Cloze = re.sub(r'\*\*(.*?)\*\*', utils.replace_cloze, Cloze)
            card = Cloze + '\t' + title + '\n'
            cards.append(card)
        else:
            continue

with open('./Cloze/anki_cloze.txt', 'w', encoding='UTF-8') as txt_file:
    txt_file.writelines(cards)

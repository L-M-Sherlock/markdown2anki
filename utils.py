def replace_formula(formula):
    formula_str = formula.group()
    formula_str = formula_str.replace('$', '')
    formula_str = formula_str.replace('{{', '{ {')
    formula_str = formula_str.replace('}}', '} }')
    formula_str = '\(' + formula_str + '\)'
    return formula_str


def replace_cloze(cloze):
    cloze_str = cloze.group()
    cloze_str = cloze_str.replace('**', '')
    cloze_str = '{{c1:' + cloze_str + '}}'
    return cloze_str

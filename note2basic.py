import re
import utils
def Basic(QA):
    QA = QA.group()
    QA = re.sub(r'\$\$(.*?)\$\$', utils.replace_formula, QA) #这里修改了
    QA = re.sub(r'!\[(.*?)\]', utils.replace_img, QA)
    QA = re.sub(r'\*\*(.*?)\*\*', utils.replace_Bold, QA)#加粗
    return QA
name="SoneSton" #需要修改为自己的
notefile_path="..\\..\\MD\\线性代数.md"#需要修改为自己的
with open(notefile_path, 'r', encoding='UTF-8') as note_file:
    cards = []
    lines = note_file.readlines()
    for line in lines:
        if line == '\n':
            continue
        elif '#' in line:
            title = line.replace('#', '')
            title = title.strip()
        else: 
            #img 处理
            imgPath=re.search(r'(?<=\]\().*?(?=\))', line)
            if imgPath is not None:
                imgPath=imgPath.group()
                line=line.replace("]("+imgPath+")" ,"."+imgPath.split(".")[-1]+"]")#移除判断多余内容,并添加后缀
                imgPath=utils.dirname(notefile_path)+imgPath.replace("/","\\")#取图片路径
                utils.Anki_Saveimg(imgPath,name)#将图片拷贝到Anki媒体目录
            #img 处理结束
            Q = re.search(r'(?<=Q:).*?(?=A:)', line)
            A = re.search(r'(?<=A:).*?(?=\n)', line)
            if Q is None or A is None:
                continue
            Q = Basic(Q)
            A = Basic(A)
            card = Q + '\t' + title + '\t' + A + '\t'+'\n'
            cards.append(card)

with open('./Basic/anki_basic.txt', 'w', encoding='UTF-8') as txt_file:
    txt_file.writelines(cards)
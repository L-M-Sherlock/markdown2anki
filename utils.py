import os
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

def replace_Bold(Bold):
    Bold_str = Bold.group()
    Bold_str = "<b>"+Bold_str.replace('**', '')+"</b>"
    return Bold_str

def replace_img(img):
    img_str= img.group()
    img_str =img_str.replace("![","")
    img_str =img_str.replace("]","")
    if os.path.exists(AnkiMedia()+img_str):#判断图片在Anki用户的媒体文件夹内是否存在
        img_str = "<img src="+img_str.split("\\")[-1]+">"
    # else:
    #     img_str=""
    return img_str

def AnkiMedia(name="SoneSton"):#请输入Anki资源用户名
    # mediaPath="%APPDATA%\\Anki2"+name+"\\collection.media"
    return os.getenv('APPDATA')+"\\Anki2"+"\\"+name+"\\collection.media\\" #返回的文件夹路径后面带 \

def Anki_Saveimg(ImgPath,name="SoneSton"):
    if os.path.exists(ImgPath)==False: #判断图片本身是否存在
        print(ImgPath.split("\\")[-1]+"写入"+name+"的Anki媒体库失败,原因:图片文件不存在")
        return False
    AnkiPath=AnkiMedia(name)
    if os.path.exists(AnkiPath+ImgPath.split("\\")[-1])==True:#判断图片在Anki用户的媒体文件夹内是否存在
        pass
    else:
        import shutil
        shutil.copy(ImgPath,AnkiMedia(name))
        print(ImgPath.split("\\")[-1]+"写入"+name+"的Anki媒体库成功")
    return True

def dirname(filePath):#返回文件的目录
    return os.path.dirname(filePath)+"\\"
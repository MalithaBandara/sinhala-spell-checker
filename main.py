from calc import calc,build
import json
import re

with open('assets/input.txt','r',encoding='utf-16') as f:
    inpt = f.readlines()

build()
data = []
line_count = 0
with open('assets/output.txt','w',encoding='utf-16') as f:
    for line in inpt:
        line_count += 1
        words = line.split()
        word_count = 0
        for word in words:
            m = re.match(r'^(.*?)([\?\!\.\,_-]+)?$', word, re.UNICODE)
            letters = m.group(1)
            punct = m.group(2) or ''
            word_count += 1
            result = calc(letters)
            if len(result) == 0:
                f.write(word+' ')
                continue
            f.write(result[0][2]+punct+' ')
            if result[0][0] != 0:
                arr = []
                for r in result:
                    arr.append(r[2]+punct)
                data.append({"line_number": line_count, "word_number": word_count, "word": word, "suggestions": arr})
        f.write('\n')

with open('assets/output.json','w',encoding='utf-16') as file:
    json.dump(data,file,ensure_ascii=False, indent=4)
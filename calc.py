max_dist = 7
dist1 = 1
dist2 = 2
dist3 = 3
word_count = 5

class Node:
    def __init__(self):
        self.children = [None] * 104
        self.wordEnd = False

mp = {'ඁ': 0, 'ං': 1, 'ඃ': 2, 'අ': 3, 'ආ': 4, 'ඇ': 5, 'ඈ': 6, 'ඉ': 7, 'ඊ': 8, 'උ': 9, 'ඌ': 10, 'ඍ': 11, 'ඎ': 12, 'ඏ': 13, 'ඐ': 14, 'එ': 15, 'ඒ': 16, 'ඓ': 17, 'ඔ': 18, 'ඕ': 19, 'ඖ': 20, 'ක': 21, 'ඛ': 22, 'ග': 23, 'ඝ': 24, 'ඞ': 25, 'ඟ': 26, 'ච': 27, 'ඡ': 28, 'ජ': 29, 'ඣ': 30, 'ඤ': 31, 'ඥ': 32, 'ඦ': 33, 'ට': 34, 'ඨ': 35, 'ඩ': 36, 'ඪ': 37, 'ණ': 38, 'න': 39, 'ත': 40, 'ථ': 41, 'ද': 42, 'ධ': 43, 'ඬ': 44, 'ඳ': 45, 'ප': 46, 'ඵ': 47, 'බ': 48, 'භ': 49, 'ම': 50, 'ඹ': 51, 'ය': 52, 'ර': 53, 'ල': 54, 'ව': 55, 'ශ': 56, 'ෂ': 57, 'ස': 58, 'හ': 59, 'ළ': 60, 'ෆ': 61, '්': 62, 'ා': 63, 'ැ': 64, 'ෑ': 65, 'ි': 66, 'ී': 67, 'ු': 68, 'ූ': 69, 'ෘ': 70, 'ෙ': 71, 'ේ': 72, 'ෛ': 73, 'ො': 74, 'ෝ': 75, 'ෞ': 76, 'ෟ': 77, '෦': 78, '෧': 79, '෨': 80, '෩': 81, '෪': 82, '෫': 83, '෬': 84, '෭': 85, '෮': 86, '෯': 87, 'ෲ': 88, 'ෳ': 89, '෴': 90, '\u200d': 91, '–': 92, '\u0dfe':93, '‚': 94, '‛': 95, '\u200c': 96, '\u0dff': 97, '‒': 98, '‾': 99, 'š': 100, '‘':101, '„': 102, 'ⅰ': 103}
root = Node()

def build():
    with open('data/dict.txt','r',encoding='utf-16') as f:
        words = f.readlines()
    for word in words:
        pos = root
        for letter in word:
            if letter == '\n':
                continue
            if pos.children[mp[letter]] == None:
                pos.children[mp[letter]] = Node()
            pos = pos.children[mp[letter]]
        pos.wordEnd = True

def search(word,x,pos,ind,curr_word,results,visited):
    if curr_word in visited and ind in visited[curr_word] and visited[curr_word][ind] >= x:
        return
    if curr_word not in visited:
        visited[curr_word] = {}
    visited[curr_word][ind] = x
    y = x
    for ch in word[ind:]:
        if mp[ch] > 60 or mp[ch] < 2:
            y -= dist2
        else:
            y -= dist3
    if pos.wordEnd and y >= 0:
        results.append([max_dist-y,abs(len(word)-len(curr_word)),curr_word])
    if x < 0 or ind == len(word):
        return
    for c in mp:
        if pos.children[mp[c]] != None:
            if c == word[ind]:
                search(word,x,pos.children[mp[c]],ind+1,curr_word+c,results,visited)
            else:
                if mp[c] > 61 or mp[c] < 2:
                    if abs(mp[c] - mp[word[ind]]) == 1:
                        search(word,x-dist1,pos.children[mp[c]],ind+1,curr_word+c,results,visited)
                        search(word,x-dist1,pos.children[mp[c]],ind,curr_word+c,results,visited)
                    else:
                        search(word,x-dist2,pos.children[mp[c]],ind+1,curr_word+c,results,visited)
                        search(word,x-dist2,pos.children[mp[c]],ind,curr_word+c,results,visited)
                else:
                    if abs(mp[c] - mp[word[ind]]) == 1:
                        search(word,x-dist2,pos.children[mp[c]],ind+1,curr_word+c,results,visited)
                        search(word,x-dist2,pos.children[mp[c]],ind,curr_word+c,results,visited)
                    else:
                        search(word,x-dist3,pos.children[mp[c]],ind+1,curr_word+c,results,visited)
                        search(word,x-dist3,pos.children[mp[c]],ind,curr_word+c,results,visited)

def calc(word):
    results = []
    visited = {}
    search(word,max_dist,root,0,"",results,visited)
    res = sorted(results)
    while len(res) > word_count:
        res.pop()
    return res
import jieba

txt = open('comment.txt','r', encoding = 'utf-8').read()
txt = jieba.lcut(txt) # jieba.lcut() 精确模式切分中文
counts = {}

for word in txt:
    if len(word) == 1:
        continue
    else:
        counts[word] = counts.get(word, 0) + 1

li = list(counts.items())
li.sort(key=lambda x:x[1], reverse=True)# 由大到小排序

with open('word frequency.txt','a',encoding='utf-8') as file:
    for i in range(1,31):
        key,value = li[i]
        print('{:<3}{:<6}{:>5}'.format(i,key,value))
        file.write(key+'\n')
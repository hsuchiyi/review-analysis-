data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count = count + 1
        if count % 1000 == 0:
            print(len(data))
sum_len = 0
for d in data:
    sum_len = sum_len + len(d)
print('留言的平均長度為', sum_len/len(data))

new = []
for d in data:
    if len(d) < 100:
        new.append(d)
print('一共有', len(new), '筆留言')

good = []
for d in data:
    if 'good' in d:
        good.append(d)
print('一共有', len(good), '提到good')
print(good[0])

#文字計數

wc = {} #word_count
for d in data:  
    words = d.split(' ')
    for word in words:
        if word in wc:
            wc[word] = wc[word] + 1
        else:
            wc[word] = 1	
for word in wc:
    if wc[word] > 1000000:
        print(word, wc[word])    
    
print(len(wc)) #字典裡有幾個不同的單字 
print(wc['Allen'])

while True:
    word = input('請問你想查甚麼字: ')
    if word == 'q':
       break
    if word in wc:
        print(word, '出現的次數為:', wc[word])
    else:
        print('本單字沒有在字典中')
print('感謝使用本查詢功能')
#讀檔案;配合read.py的理解，進行此"分析留言檔專案"

data = []
count = 0
with open('original.txt', 'r') as f:
	for line in f:
		data.append(line)
		count = count + 1
		if count % 1000 == 0: #%是求餘數
			print(len(data))
print('檔案讀取完了,', '總共有:', len(data), '筆資料')

sum_len = 0
for d in data:
	sum_len = sum_len + len(d) #len(d)指的是每行讀出來的字元總數(字元長度)
	#print(len(d))
print('平均留言長度', sum_len/len(data))

#print(len(data))  #len長度指的是"行"
#print(data[0]) #索引0的內容,也指第一列的意思
#print('===================')
#print(data[1]) #索引1的內容,也指第二列的意思

#篩選留言長度<100
new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '留言長度小於100')
print(new[0])
		





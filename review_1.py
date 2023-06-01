#讀檔案;配合read.py的理解，進行此"分析留言檔專案"

data = []
count = 0
with open('original.txt', 'r') as f:
	for line in f:            #把f內的所有檔案讀到line"
		data.append(line)     #把line裡面所有的資料丟到append的data裡 
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
for d in data:        #data裡有1百萬的清單,每次讀取後會將文字抓取出來成為獨立的留言,所以d是獨立的留言
	if len(d) < 100:  #字元總數(字元長度)小於100的,進行下一個增加到new清單的動作
		new.append(d) #增加(append)到清單裡,注意這裡面不是原data的1百萬資料,而是留言長度小於100,再放回new的新的清單裡
print('一共有', len(new), '留言長度小於100')
print(new[0])
		
good = []
for d in data:           #同上一段字元長度說明
	if 'good' in d:      #1百萬留言裡,字串裡有含'good'的留言,進行下一個增加到good清單的動作
		good.append(d)   #同上一段字元長度說明,留言內含'good'清單者,再放回good清單裡
print('一共有', len(good), '留言提到good')
print(good[0])
	



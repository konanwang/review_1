#讀檔案

data = []
with open('test1.txt', 'r') as f: #'r'是讀取,也可以是'w'寫入
	for a in f:
		data.append(a.strip()) #將f裡面每一筆讀出來的a，增加到data的清單裡面，再讀取出來

print(data) #注意格式:此行需要在外面,非with的for迴圈裡，才可以對應data的外層
#若單純僅有data.append(a)，列印時會出現換行符號/n. (/n:表示"換行符號")
#因需要去除換行符號,因此要加入strip;不過要注意的是，此為字串，故才可使用strip
#with open:如同夾娃娃機，open後一定需要close，
#在python裡設計了比較進階的方式採用with, 只要跳脫with這個框的層級，就會close，例如print(data)即為此意

print(len(data)) #len長度指的是"行",此指令是為了印出驗證用途

for d in data: 
	print(len(d)) #此所指為統計每一行的"字元總數"!!

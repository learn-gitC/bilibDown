import os


av = input("请输入B战视频av号（avxxxxxxxx）：\n")
num = input("how many videos in the playlist:\?")
parentUrl = 'https://www.bilibili.com/video/'+av+'/?p='
url = ''
for i in range(1, num+1):
    url += parentUrl + str(i) + '\n'

with open('./url_list', 'w') as f:
    f.write(url)

os.system('download.sh')
parentUrl = 'https://www.bilibili.com/video/av36557763/?p='
url = ''
for i in range(1, 36):
    url += parentUrl + str(i) + '\n'

with open('./url_list', 'w') as f:
    f.write(url)


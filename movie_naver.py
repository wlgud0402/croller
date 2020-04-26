from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

html = urlopen('https://movie.naver.com/movie/sdb/rank/rmovie.nhn')
bs = BeautifulSoup(html, 'html.parser')

rankSection = bs.find('tbody')

#순위와 제목
# rankList = rankSection.find_all('div',{'class':'tit3'})

# i=1
# while i<50:
#     for rank in rankList:
#         print( str(i)+ "위 "+rank.text.strip())
#         i +=1

#링크
# rankList = rankSection.find_all('div',{'class':'tit3'})


# for rank in rankList:
#     print(rank.a)


#어차피 50개밖에없어서 while문 필요 X
AllrankHref = rankSection.find_all('a')
i=1
while i<50:
    print("나 와일문안")
    for rankHref in AllrankHref:
        href = rankHref.attrs['href']
        text = rankHref.string
        print(str(i)+"위", text, ":" "https://movie.naver.com" +str(href))
        i+=1






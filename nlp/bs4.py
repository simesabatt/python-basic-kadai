from bs4 import BeautifulSoup
from urllib import request

url = 'https://www.aozora.gr.jp/cards/000879/files/128_15261.html'
response = request.urlopen(url)
soup = BeautifulSoup(response)
response.close()

# print(soup)
main_text = soup.find('div', class_='main_text')
print(main_text)

tags_to_delete = main_text.find_all(['rp', 'rt'])
for tag in tags_to_delete:
    tag.decompose()
# print(main_text)

main_text = main_text.get_text()
# print(main_text)

import re
main_text = re.sub(r"[\u3000 \n \r]", "", main_text)
# print(main_text)

from bs4 import BeautifulSoup
from urllib import request

url = 'http://svn.sourceforge.jp/svnroot/slothlib/CSharp/Version1/SlothLib/NLP/Filter/StopWord/word/Japanese.txt'
response = request.urlopen(url)
soup = BeautifulSoup(response)
response.close()

# print(soup)

stopwords_text = soup.text
# print(stopwords_text)

stopwords_list = stopwords_text.split("\r\n")
stopwords_list = [word for word in stopwords_list if word]
# print(stopwords_list)


split_text_list =  ['私', 'は', '今日', '、', 'スーパー', 'で', '沢山', 'の', 'お', '菓子', 'を', '買っ', 'た', '。']
result_text_list = list()
for split_text in split_text_list:
    if split_text not in stopwords_list:
        result_text_list.append(split_text)

#print(result_text_list)


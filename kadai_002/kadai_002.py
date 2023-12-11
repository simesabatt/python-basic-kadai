from bs4 import BeautifulSoup
from urllib import request
import re

url = 'https://www.aozora.gr.jp/cards/000148/files/2371_13943.html'
response = request.urlopen(url)
soup = BeautifulSoup(response)
response.close()
# print(soup)

main_text = soup.find('div', class_='main_text')
main_text = main_text.get_text()
# print(main_text)

main_text = re.sub(r"[\u3000 \n \r]", "", main_text)
# print(main_text)

# ストップワードのリスト
stopwords_list = ['は', 'の', 'が', 'に', 'を', 'で', 'と', 'も', 'から', 'です', 'ます', 'して', 'しろしろ', 'なった', '思って', 'います']

# 単語に分割
words = re.findall(r'\w+', main_text)
# print(words)

# ストップワードを除外
filtered_words = [word for word in words if word not in stopwords_list]
print(filtered_words)

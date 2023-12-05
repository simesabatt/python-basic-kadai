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


# ストップワードのリスト
stopwords = ['は', 'の', 'が', 'に', 'を', 'で', 'と', 'も', 'から', 'です', 'ます', 'して', 'しろしろ', 'なった', '思って', 'います']

# ストップワードを除去
words = main_text.split()  # スペースで単語に分割
cleaned_text = ' '.join(word for word in words if word not in stopwords)

#print(cleaned_text)

# ストップワードのリスト
stopwords = ['は', 'の', 'が', 'に', 'を', 'で', 'と', 'も', 'から', 'です', 'ます', 'して', 'しろしろ', 'なった', '思って', 'います']

# テキスト（例として最初の1文を使用）
text = '近頃は大分方々の雑誌から談話をしろしろと責められて、頭ががらん胴になったから、当分品切れの看板でも懸けたいくらいに思っています。'

# ストップワードを除去
words = text.split()  # スペースで単語に分割
cleaned_text = ' '.join(word for word in words if word not in stopwords)

print(cleaned_text)


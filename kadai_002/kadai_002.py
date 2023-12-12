from bs4 import BeautifulSoup
from urllib import request
import re

# 青空文庫のテキストを取得
url = 'https://www.aozora.gr.jp/cards/000148/files/2371_13943.html'
response = request.urlopen(url)
soup = BeautifulSoup(response, 'html.parser')
response.close()
main_text = soup.text

# 不要な空白や改行を削除
main_text = re.sub(r"[\u3000 \n \r]", "", main_text)

# ストップワードのリストを取得
url = 'http://svn.sourceforge.jp/svnroot/slothlib/CSharp/Version1/SlothLib/NLP/Filter/StopWord/word/Japanese.txt'
response = request.urlopen(url)
soup = BeautifulSoup(response, 'html.parser')
response.close()
stopwords_text = soup.text
stopwords_list = stopwords_text.split("\r\n")
stopwords_list = [word for word in stopwords_list if word]

# 分割に使う単語リスト
words = ['近頃', 'は', '大分', '方々', 'の', '雑誌', '談話', 'を', 'しろ', 'しろ', 'と', '責め', 'られて', '、', '頭', 'が', 'がらん', '胴', 'に', 'なった', '、', '当分', '品切れ', 'の', '看板', 'でも', '懸け', 'たい', 'くらい', 'に', '思って', 'い', 'ます', '。']

# テキスト全体を走査して、指定された単語リストに含まれる単語を探し、ストップワードを除外
filtered_words = [word for word in words if word in main_text and word not in stopwords_list]

print(filtered_words)

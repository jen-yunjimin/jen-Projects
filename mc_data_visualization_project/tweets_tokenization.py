# 필요한 라이브러리 가져오기
import pandas as pd
import numpy as np
import nltk   # 토큰화에 필요한 라이브러리
nltk.download('punkt')
from nltk.tokenize import sent_tokenize

# 데이터프레임 불러오기
tweets_df= pd.read_csv("file path")

# tweets_df에서 Text값만 추출
df_txt = tweets_df.copy() 
df_txt['Text'].values

# 배열에서는 split을 사용할 수 없기 때문에 문자열로 바꿔준다
string = '/'.join(df_txt['Text'].values) # 배열 안 문장들을 '/'로 구분
print(string)

# 문자열로 바꾼 후 split 적용
string_token = string.split()
string_token

# 정규식으로 영어만 추출
import re
string_token_re = re.sub("[^a-zA-Z]", " ", str(string_token))
print(string_token_re)

# (단어, 품사)로 나오게 하는 코드
from nltk.tag import pos_tag
nltk.download('averaged_perceptron_tagger')
word_class = word_tokenize(string_token_re)
pos_tag(word_class)

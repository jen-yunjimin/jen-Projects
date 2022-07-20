from google_play_scraper import app
from google_play_scraper import Sort, reviews_all
import pandas as pd
import numpy as np
import json

# 한국어 리뷰 가져오기
kor_reviews = reviews_all(
    'com.ncsoft.lineagem19',
    sleep_milliseconds=0, # defaults to 0
    lang='ko', # defaults to 'en'
    country='kr', # defaults to 'us'
    sort=Sort.NEWEST, # defaults to Sort.MOST_RELEVANT
)

# 크롤링 데이터 데이터프레임으로 생성
df_reviews = pd.DataFrame(np.array(kor_reviews),columns=['review'])

df_reviews = df_reviews.join(pd.DataFrame(df_reviews.pop('review').tolist()))
df_reviews.head()

# csv파일 저장
df_reviews.to_csv('리니지M_reviews.csv')

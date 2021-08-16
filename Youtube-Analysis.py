

import numpy as np
import pandas as pd

'''
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
'''

df = pd.read_excel('Youtube-data.xlsx', sheet_name=0, header=0)
df = df.drop(index=0, axis=0)
df = df.drop(columns=['동영상', '동영상 제목', '동영상 게시 시간'])

#1 등장인물 별 평균 조회수, 시청시간, 구독자증가, 노출수, 노출클릭률
'''
df_Juri = df[df['등장인물'].str.contains('쥬리')].drop(columns='등장인물', axis=1)
df_Yeonhee = df[df['등장인물'].str.contains('연희')].drop(columns='등장인물', axis=1)
df_Yunkyoung = df[df['등장인물'].str.contains('윤경')].drop(columns='등장인물', axis=1)
df_Dahyun = df[df['등장인물'].str.contains('다현')].drop(columns='등장인물', axis=1)
df_Suyun = df[df['등장인물'].str.contains('수윤')].drop(columns='등장인물', axis=1)
df_Sohee = df[df['등장인물'].str.contains('소희')].drop(columns='등장인물', axis=1)

df_Jiae = df[df['등장인물'].str.contains('지애')].drop(columns='등장인물', axis=1)
df_Enbi = df[df['등장인물'].str.contains('은비')].drop(columns='등장인물', axis=1)
df_Nako = df[df['등장인물'].str.contains('나코')].drop(columns='등장인물', axis=1)
df_Gfriend = df[df['등장인물'].str.contains('여자친구')].drop(columns='등장인물', axis=1)
df_Soyeon = df[df['등장인물'].str.contains('소연')].drop(columns='등장인물', axis=1)


df_mean = pd.concat([df_Juri.mean(), df_Yeonhee.mean(), \
    df_Yunkyoung.mean(), df_Dahyun.mean(), df_Suyun.mean(), \
        df_Sohee.mean(), df_Jiae.mean(), df_Enbi.mean(), \
            df_Nako.mean(), df_Gfriend.mean(), df_Soyeon.mean()], axis=1)

df_mean.columns = ['Juri', 'Yeonhee', 'Yunkyoung', 'Dahyun', 'Suyun', \
                    'Sohee', 'Jiae', 'Enbi', 'Nako', 'Gfriend', 'Soyeon']
print(df_mean)
'''

#2 등장인물 별 평균 조회수, 시청시간, 구독자증가, 노출수, 노출클릭률 (+정렬)
# 단체로 등장하는 경우와, 다른 영향력이 큰 인물이 영향을 주는 경우는 제외하고
# 최대한 본인(1명)에 의한 조회수 power를 추정해보기

df_Juri = df[~df['등장인물'].str.contains('쥬리 연희 윤경 다현 수윤 소희')]
df_Juri = df[~df['등장인물'].str.contains('나코')]
df_Juri = df_Juri[df_Juri['등장인물'].str.contains('쥬리')]\
    .drop(columns='등장인물', axis=1)

df_Yeonhee = df[~df['등장인물'].str.contains('쥬리 연희 윤경 다현 수윤 소희')]
df_Yeonhee = df[~df['등장인물'].str.contains('지애')]
df_Yeonhee = df[~df['등장인물'].str.contains('은비')]
df_Yeonhee = df_Yeonhee[df_Yeonhee['등장인물'].str.contains('연희')]\
    .drop(columns='등장인물', axis=1)

df_Yunkyoung = df[~df['등장인물'].str.contains('쥬리 연희 윤경 다현 수윤 소희')]
df_Yunkyoung = df_Yunkyoung[df_Yunkyoung['등장인물'].str.contains('윤경')]\
    .drop(columns='등장인물', axis=1)

df_Dahyun = df[~df['등장인물'].str.contains('쥬리 연희 윤경 다현 수윤 소희')]
df_Dahyun = df_Dahyun[df_Dahyun['등장인물'].str.contains('다현')]\
    .drop(columns='등장인물', axis=1)

df_Suyun = df[~df['등장인물'].str.contains('쥬리 연희 윤경 다현 수윤 소희')]
df_Suyun = df_Suyun[df_Suyun['등장인물'].str.contains('수윤')]\
    .drop(columns='등장인물', axis=1)

df_Sohee = df[~df['등장인물'].str.contains('쥬리 연희 윤경 다현 수윤 소희')]
df_Sohee = df_Sohee[df_Sohee['등장인물'].str.contains('소희')]\
    .drop(columns='등장인물', axis=1)


df_mean = pd.concat([df_Juri.mean(), df_Yeonhee.mean(), \
    df_Yunkyoung.mean(), df_Dahyun.mean(), df_Suyun.mean(), \
        df_Sohee.mean()], axis=1)

df_mean.columns = ['Juri', 'Yeonhee', 'Yunkyoung', 'Dahyun', 'Suyun', 'Sohee']

index_list = df_mean.index.to_list()
index_list[1] = '시청시간'
index_list[4] = '노출클릭률'
df_mean.index = index_list

print(df_mean)

df_mean0 = df_mean.sort_values(by=['조회수'], axis=1, ascending=False)
df_mean1 = df_mean.sort_values(by=['시청시간'], axis=1, ascending=False)
df_mean2 = df_mean.sort_values(by=['구독자'], axis=1, ascending=False)
df_mean3 = df_mean.sort_values(by=['노출수'], axis=1, ascending=False)
df_mean4 = df_mean.sort_values(by=['노출클릭률'], axis=1, ascending=False)

print(df_mean.index[0], "순 : ", df_mean0.columns.to_list())
print(df_mean.index[1], "순 : ", df_mean1.columns.to_list())
print(df_mean.index[2], "순 : ", df_mean2.columns.to_list())
print(df_mean.index[3], "순 : ", df_mean3.columns.to_list())
print(df_mean.index[4], "순 : ", df_mean4.columns.to_list())




'''
print(df_Juri)
print(df_Yeonhee)
print(df_Yunkyoung)
print(df_Dahyun)
print(df_Suyun)
print(df_Sohee)
'''






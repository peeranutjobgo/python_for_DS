# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 18:46:05 2019

@author: peejobgo
"""

import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans

#import saw file
df_res = pd.read_csv('restaurant.csv', index_col=None)
df_rat = pd.read_csv('rating.csv', index_col=None)
df_wn = pd.read_csv('preprocess_df.csv', index_col=None)
# group ตามประเภท restaurant จาก table ที่ผสานแล้ว
res_wn = df_wn.groupby('category_name').mean().round(2) ; counts = df_wn.groupby(['category_name']).size() ; res_wn['count'] = counts

# การจัดกลุ่มข้อมูล ตาม column rating(คะแนน), price_range(เรทราคา)
kmeans = KMeans(n_clusters=3).fit(res_wn[['rating', 'price_range']])
centroids = kmeans.cluster_centers_
print(centroids)
#pot chart
plt.figure(figsize=(8, 8))
sns.set(font_scale=1.0)
plt.scatter(res_wn['rating'], res_wn['price_range'], c= kmeans.labels_.astype(float), s=100, alpha=0.5)
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=200)
plt.xlabel("Rating", fontsize=20)
plt.ylabel("Price range", fontsize=20)

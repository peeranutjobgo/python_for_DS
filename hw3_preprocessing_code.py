# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 08:31:19 2019

@author: peejobgo
"""

import pandas as pd
import numpy as np

#import saw file
df_res = pd.read_csv('restaurant.csv', index_col=None)
df_rat = pd.read_csv('rating.csv', index_col=None)

#data exploration
print(df_rat.info())
print(df_res.info())
print(df_res.apply(lambda x: sum(x.isnull())))

# delete missing value
df_res.dropna(inplace=True)
print(df_res.apply(lambda x: sum(x.isnull())))

# set "timestamp" เป็น datatime  ข้อมูลประเภทเวลา
df_rat['timestamp'] = pd.to_datetime(df_rat['timestamp'], errors='coerce')
# เพิ่ม column วันในสัปดาห์
df_rat['day_of_week'] = df_rat['timestamp'].dt.day_name()
df_rat['day_of_week_mun'] = df_rat['timestamp'].dt.dayofweek
# เพิ่ม column  ชั่วโมง
df_rat['hour_of_timestamp'] = df_rat['timestamp'].dt.hour
print(df_rat.head())

# ผสาน table restaurant กับ table rating
df_wn = pd.merge(df_rat,df_res, how="left",on = ['business_id'])
print(df_wn.info())
print(df_wn.apply(lambda x: sum(x.isnull())))

# delete missing value
df_wn.dropna(inplace=True)
print(df_wn.info())

#export to csv
df_wn.to_csv('preprocess_df.csv')
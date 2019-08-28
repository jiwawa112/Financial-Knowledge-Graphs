#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import time
import tushare as ts
import pandas as pd

pro = ts.pro_api('f70ec10113f0d0b5c0a5f080f105dd68d6d266b5de670e9593d2b0a3')

# 1.获取股票基本信息
stock_basic = pro.stock_basic(list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
basic_rename = {'ts_code': 'TS代码', 'symbol': '股票代码', 'name': '股票名称', 'area':'地域','industry': '行业'}
stock_basic.rename(columns=basic_rename,inplace=True)
# 保存为stock_basic.csv
stock_basic.to_csv('stock_basic.csv',encoding='gbk')
print(stock_basic.head())

# 2.获取上述所有股票的top10股东信息
shareholders = pd.DataFrame(columns=('ts_code', 'ann_date', 'end_date', 'holder_name', 'hold_amount', 'hold_ratio'))
for i in range(len(stock_basic)):
    code = stock_basic['TS代码'].values[i]
    try:
        top10_holders = pro.top10_holders(ts_code=code,start_date='20180101',end_data='20180331')
        shareholders = shareholders.append(top10_holders)
        print(shareholders)
    except:
        time.sleep(1)

    print('完成第%d条股票股东获取' % i)

shareholders.to_csv('stock_holders.csv',encoding='gbk')

# 3.获取股票概念信息
concept = pro.concept()
print(concept)
concept.to_csv('concept.csv',encoding='gbk')

concept_details = pd.DataFrame(columns=('id', 'concept_name', 'ts_code', 'name'))
for i in range(len(concept)):
    id = 'TS' + str(i)
    concept_detail = pro.concept_detail(id=id)
    concept_details = concept_details.append(concept_detail)
    time.sleep(5)
concept_details.to_csv('concept_details.csv',encoding='gbk')

# 4.沪深股通成份股成分信息
#获取沪股通成分
sh = pro.hs_const(hs_type='SH')
sh.to_csv('sh.csv',index=False)

#获取深股通成分
sz = pro.hs_const(hs_type='SZ')
sz.to_csv('sz.csv',index=False)
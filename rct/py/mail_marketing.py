#!-*-coding:utf-8-*-
import numpy as np
import pandas as pd
import scipy.stats as st

####################
#   データの読み込み  #
####################
df = pd.read_csv("../../datas/Kevin_Hillstrom_MineThatData_E-MailAnalytics_DataMiningChallenge_2008.03.20.csv")
df = df[df.womens == 0] #演習通り、女性のデータを除外する

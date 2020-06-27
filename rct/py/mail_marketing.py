#!-*-coding:utf-8-*-
import warnings
import numpy as np
import pandas as pd
from scipy import stats as st

####################
#   データの読み込み  #
####################
warnings.simplefilter('ignore')
df = pd.read_csv("../../datas/Kevin_Hillstrom_MineThatData_E-MailAnalytics_DataMiningChallenge_2008.03.20.csv")
male_df = df[df.segment != "Womens E-Mail"] #演習通り、女性のデータを除外する
male_df["treatment"] = np.where( male_df.segment == "Mens E-Mail" , 1,0 )
del df

####################
#   グループ集計     #
####################
summary_by_segment = male_df.groupby("treatment").mean()
#print( summary_by_segment[["spend","conversion"]] )


####################
#        #
####################
mens_mail = np.array( male_df[male_df.treatment == 1].spend )
no_mail = np.array( male_df[male_df.treatment == 0].spend )

rct_ttest = st.ttest_ind( mens_mail , no_mail , equal_var=True ) #equal_var : 分散が等しいことを仮定した検定
print( rct_ttest )

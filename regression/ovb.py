#!-*-coding:utf-8-*-
import sys
import pandas as  pd
import numpy as np
import statsmodels.api as sm

######################
#   データの読み込み   #
######################
df = pd.read_csv("../datas/Kevin_Hillstrom_MineThatData_E-MailAnalytics_DataMiningChallenge_2008.03.20.csv")

######################
#       前処理        #
######################
male_df = df[df.segment != "Womens E-Mail"]
del df
male_df["treatment"] = np.where( male_df.segment == "Mens E-Mail" , 1 , 0)
male_df["channelPhone"] = np.where( male_df.channel == "Phone" , 1 , 0 )
male_df["channelWeb"] = np.where( male_df.channel == "Web" , 1 , 0 )
male_df["channelMultichannel"] = np.where( male_df.channel == "Multichannel" , 1 , 0 )

######################
#    変数の取り出し    #
######################
X_1 = male_df[[ "treatment" , "recency" , "channelPhone" \
, "channelWeb"  ]]

X_2 = male_df[[ "treatment" , "recency" , "channelPhone" \
, "channelWeb", "history" ]]

X_3 = male_df[[ "treatment" , "recency" , "channelPhone" \
, "channelWeb" ]]

X_1 = sm.add_constant( X_1 )
X_2 = sm.add_constant( X_2 )
X_3 = sm.add_constant( X_3 )

y_1 = male_df[["spend"]]
y_2 = male_df[["history"]]

######################
#        OLS         #
######################
model_1 = sm.OLS( y_1 , X_1 )
model_2 = sm.OLS( y_1 , X_2 )
model_3 = sm.OLS( y_2 , X_3 )

results_1 = model_1.fit()
results_2 = model_2.fit()
results_3 = model_3.fit()


print( results_1.summary() )
print( results_2.summary() )
print( results_3.summary() )

######################
#      OVBの計算      #
######################
a_1 = results_1.params["treatment"]
b_1 = results_2.params["treatment"]
b_4 = results_2.params["history"]

gamma_1 = results_3.params["treatment"]
gamma_1_b_4 = gamma_1 * b_4

#欠落変数バイアスが計算された
print( round( gamma_1_b_4 , 5 ) == round( a_1 - b_1 , 5 ) )

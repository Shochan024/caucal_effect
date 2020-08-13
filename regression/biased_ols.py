#!-*-coding:utf-8-*-
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

######################
#    変数の取り出し    #
######################
X = male_df[[ "treatment" , "history" ]]
X = sm.add_constant( X )
y = male_df[["spend"]]


######################
#        OLS         #
######################
model = sm.OLS( y , X )
results = model.fit()

print( results.summary() )

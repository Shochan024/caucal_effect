#-*-coding:utf-8-*-
import sys
import pandas as pd
import numpy as np

def ate( df ):
    """
    平均処置効果をreturnする
    """
    y_0 = np.sum( df.y * ( 1 - df.z ) * ( 1 / np.sum( ( 1 - df.z ) == 1 ) ) )
    y_1 = np.sum( ( df.y * df.z ) * ( 1 / np.sum( df.z == 1 ) ) )

    return round( y_1 - y_0 , 2 )

def selective_biase( df ):
    """
    Selective Biaseをreturnする
    各介入に対する潜在傾向を考える
    """
    y_0_z_0 = np.sum( ( df.y_0 * ( 1 - df.z ) ) * ( 1 / np.sum( df.z == 0 ) ) )
    y_0_z_1 = np.sum( ( df.y_0 * df.z ) * ( 1 / np.sum( df.z == 1 ) ) )

    return round( y_0_z_1 - y_0_z_0 , 2 )

def explor( df ):
    """
    結果をレポート
    """
    ATE = ate( df=df )
    Bias = selective_biase( df )
    print( "ATE :", ATE , "Bias :" , Bias , "Real Effect :",  ATE-Bias )


df_biased = pd.read_csv("../datas/mail_marketing_biased.csv")
df_RCT = pd.read_csv("../datas/mail_marketing_RCT.csv")


explor( df=df_biased )
explor( df=df_RCT  )

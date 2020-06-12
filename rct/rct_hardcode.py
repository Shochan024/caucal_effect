#-*-coding:utf-8-*-
import sys
import pandas as pd
import numpy as np
"""
仮想データを用いてRCTの効果を実験するプログラム
本来は観測ができないy_0やy_1が擬似的に作られており、ATEは100に設定されている
"""
"""
購買意欲の高いユーザに絞ってクーポンメールを送信した際の平均処置効果を調べる
"""
####################
#   データの読み込み  #
####################
df = pd.read_csv("../datas/mail_marketing_biased.csv")

####################
#     ATEの算出     #
####################
y_0 = np.sum( df.y * ( 1 - df.z ) * ( 1 / np.sum( 1 - df.z == 1 ) ) )
y_1 = np.sum( df.y * ( df.z ) * ( 1 / np.sum( df.z == 1 ) ) )

print( "ATE :" , y_1 - y_0 )

####################
#     Biasの算出     #
####################
y_0_z_0 = np.sum( ( df.y_0 * ( 1 - df.z ) ) * ( 1 / np.sum( df.z == 0 ) ) )
y_0_z_1 = np.sum( ( df.y_0 * df.z ) * ( 1 / np.sum( df.z == 1 ) ) )

print( "Bias" , y_0_z_1 - y_0_z_0 )


"""
購買意欲の高いユーザに絞らず、グループの潜在的購買傾向の差の期待値を0にした上でクーポンメールを送信した際の平均処置効果を調べる
"""
####################
#   データの読み込み  #
####################
df_RCT = pd.read_csv("../datas/mail_marketing_RCT.csv")

####################
#     ATEの算出     #
####################
y_0_RCT = np.sum( df_RCT.y * ( 1 - df_RCT.z ) * ( 1 / np.sum( 1 - df_RCT.z == 1 ) ) )
y_1_RCT = np.sum( df_RCT.y * ( df_RCT.z ) * ( 1 / np.sum( df_RCT.z == 1 ) ) )

print( "ATE :" , round( y_1_RCT - y_0_RCT , 2 ) )

####################
#     Biasの算出     #
####################
y_0_z_0_RCT = np.sum( ( df_RCT.y_0 * ( 1 - df_RCT.z ) ) * ( 1 / np.sum( df_RCT.z == 0 ) ) )
y_0_z_1_RCT = np.sum( ( df_RCT.y_0 * df_RCT.z ) * ( 1 / np.sum( df_RCT.z == 1 ) ) )

print( "Bias" , round( y_0_z_1_RCT - y_0_z_0_RCT , 2 ) )

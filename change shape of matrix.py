import pandas as pd
import numpy as np
##############################################################
s1={'id':['123','654','267','675','654'],'ML.score':[45,33,50,87,90]}
DF1=pd.DataFrame(s1)
############################################################
print(DF1.iloc[0,1])#print one cell
ar=np.random.randn(25)
print("////////////////////////////////////////////////")
print(ar)
DF2=pd.DataFrame((ar).reshape(5,5))#تغيير ابعاد المصفوفة 
print("//////////////////////////////////////////////")
#print(DF2)
DF2=pd.DataFrame((ar).reshape(5,5),index=['A','B','C','D','E'],columns=['A1','A2','A3','A4','A5'])#Convert column and row headers
print("///////////////////////////////////////")
print(DF2)




import pandas as pd 

df=pd.read_csv('RELIANCE.NS.csv')
# Remove the entries with 0 as open price
df=df[df['Open'] != 0]
df['PriceMvt']=df.Close-df.Open
if df['PriceMvt']>15:
    # print(df.PriceMvt)
    print("hh")
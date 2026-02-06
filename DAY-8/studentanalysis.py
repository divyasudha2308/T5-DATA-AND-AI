import pandas as pd


df=pd.read_csv("studentdata.csv")


df['Marks'].fillna(df['Marks'].mean(),inplace=True)
print(df)
df_clean=df.dropna()
print(df_clean)
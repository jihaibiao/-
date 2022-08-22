import pandas as pd
df = pd.read_csv(r'001_周舟.csv')
#print(df)
#print(df.head())
df.groupby("ID")["TIME_MOVE","SUCCESS"].mean()
groupmean_df = pd.DataFrame(df.groupby("ID")["TIME_MOVE","SUCCESS"].mean())
print(groupmean_df)
groupmean_df.to_csv("groupmean.csv")
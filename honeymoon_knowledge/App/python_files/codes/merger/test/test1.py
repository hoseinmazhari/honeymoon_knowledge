import pandas as pd
import random as rnd
df = pd.DataFrame()
for i in range(1,20):
  a = {"name":f"merchandise{i}","count":i,"price":f"{rnd.randrange(100000,200000)}","total": i*22}
  df = df.append(a,ignore_index = True) # type: ignore


# print(df)
df["test add"] =df["count"]

df["test add"] *= df["total"]
# *df["price"])
print(df)
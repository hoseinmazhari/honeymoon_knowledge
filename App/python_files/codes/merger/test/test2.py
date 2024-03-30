import pandas as pd
df = pd.DataFrame({'A': [1, 2, 3, 4, 5]})
print(df)
for i in range(3):
    print("")
print("after replace")
def replace_func(x):
    if x % 2 == 0:
        return x * 2000
    else:
        return x
# for i in range(len(df)):
df['A'] = df['A'].apply(replace_func)
print(df)
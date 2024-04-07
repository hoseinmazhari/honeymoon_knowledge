import pandas as pd

# ساخت یک دیتافریم نمونه
df = pd.DataFrame({'A': [1, 2, 3, 4], 'B': [10, 20, 30, 40]})

# شرط مورد نظر
condition = (df['A'] % 2 == 0)

# جایگزین کردن مقادیر بر اساس شرط
df.loc[condition, 'B'] = 0

# نمایش دیتافریم نهایی
print(df)
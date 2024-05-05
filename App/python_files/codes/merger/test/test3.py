import pandas as pd
 
# Creating the first Dataframe using dictionary
df1 = df = pd.DataFrame({"a":[1, 2, 3, 4],
                        "b":[5, 6, 7, 8]})
 
# Creating the Second Dataframe using dictionary
df2 = pd.DataFrame({"a":[11, 22, 33],
                    "b":[55, 66, 77]})
 
# Print df1
print(df1, "\n")
 
# Print df2
print(df2)
print()
print()
print()
print()
# to append df2 at the end of df1 dataframe
df1 = df1.append(df2)
print("appenddeddd")
print(df1)
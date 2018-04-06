import pandas as pd
filename = "validation.csv"
data = pd.read_csv(filename)
df = pd.DataFrame(data)
users = {}
i = 0
for u in df['usertag']:
    users[i] = str(u).split(',')
    i += 1
# print(users)

s = pd.Series(users)
pd.get_dummies(s.apply(pd.Series).stack()).sum(level=0)
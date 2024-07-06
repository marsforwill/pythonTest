import pandas as pd
import matplotlib.pyplot as plt

# Series
data = [1,2,3,4,5]
s = pd.Series(data)
print(s)

# 从字典创建 DataFrame
data = {
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'city': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)
print(df)

# read/write from csv excel sql
# df = pd.read_csv('data.csv')
# df.to_csv('output.csv', index=False)

# df = pd.read_excel('data.xlsx')
# df.to_excel('output.xlsx', index=False)

# import sqlite3
# conn = sqlite3.connect('data.db')
# df = pd.read_sql('SELECT * FROM table_name', conn)
# df.to_sql('table_name', conn, if_exists='replace', index=False)

print(df.head)
print(df.info)
print(df['city'])

df['salary'] = [50000, 60000, 70000]
df = df.drop(index=[0])
print(df)

# 数据清洗、数据转换、统计分析,dataframe操作（合并） 数据可视化、时间序列分析等场景
df['city'] = df['city'].replace('New York', 'NY')
group = df.groupby('city')
print(group)
print(group['age'].mean())

df.plot(x='name', y='age', kind='line')
plt.xlabel('Name')
plt.ylabel('Age')
plt.show()



import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib


df = pd.read_csv("data/cases_cumulative_daily (1).csv", encoding="utf-8")

date = "2021/5/10"

df_with_date = df[df["Date"] == date]

# print(df_with_date)

if df_with_date . empty:
    print("データが空っぽです。")
else:
    date_data = df_with_date.drop(columns=['Date', 'ALL']).iloc[0]
    date_data_sorted = date_data.sort_values(ascending=True)
    print(date_data_sorted)


plt.figure(figsize=(12,8))
plt.barh(date_data_sorted.index, date_data_sorted.values)

plt.title(f"都道府県ごとの感染者数 {date}")
plt.xlabel("感染者数")
plt.show()

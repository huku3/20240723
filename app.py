# import pandas as pd
# import matplotlib.pyplot as plt
# import japanize_matplotlib

# df = pd.read_csv("data/cases_cumulative_daily (1).csv", encoding="utf-8")

# df["Date"] = pd.to_datetime(df["Date"])

# plt.figure(figsize=(8,3))

# plt.plot(df["Date"], df["Iwate"],label="Iwate",color="y")
# plt.plot(df["Date"], df["Tokyo"],label="Tokyo",color="b")

# plt.title("岩手・東京-コロナ感染者数")
# plt.xlabel("日付")
# plt.ylabel("感染者数")

# plt.legend()
# plt.grid(True)
# plt.xticks(rotation=0)
# plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

df = pd.read_csv("data/cases_cumulative_daily (1).csv", encoding="utf-8")

df["Date"] = pd.to_datetime(df["Date"])

plt.figure(figsize=(9,4))

plt.plot(df["Date"], df["Hokkaido"],label="Hokkaido",color="y")
plt.plot(df["Date"], df["Gifu"],label="Gifu",color="b")
plt.plot(df["Date"], df["Okinawa"],label="Okinawa",color="g")
plt.plot(df["Date"], df["ALL"],label="ALL",color="r")

plt.title("北海道・岐阜・沖縄・合計-コロナ感染者数")
plt.xlabel("日付")
plt.ylabel("感染者数")

plt.legend()
plt.grid(True)
plt.xticks(rotation=0)
plt.show()

import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle
import streamlit as st

data = pd.read_csv("BOT_Car_Index.csv")
data_sort = data.sort_values(["month"]).reset_index(drop=True)

st.set_page_config(layout="wide")

fig1, ax = plt.subplots(figsize=(25, 5))

All = st.checkbox("All")
Car = st.checkbox("Car")
Truck = st.checkbox("Truck")

if All:
    ax.plot(
        data_sort["cartype_all"], ":", color="black", alpha=0.7, label="all price index"
    )
if Car:
    ax.plot(
        data_sort["cartype_car"], "-", color="blue", alpha=0.7, label="Car price index"
    )
if Truck:
    ax.plot(
        data_sort["cartype_truck"], "-", color="orange", alpha=0.7, label="Truck price index"
    )


plt.legend()
st.pyplot(fig1)


time = data_sort["month"]
index = time.index

Month = st.slider("Month", 0, 140, 1)

fig2, ax = plt.subplots(figsize=(25, 5))

price1 = data_sort["cartype_all"].where(index >= 0).where(index <= 11)
price2 = data_sort["cartype_all"].where(index >= 12).where(index <= 23)
price3 = data_sort["cartype_all"].where(index >= 24).where(index <= 35)
price4 = data_sort["cartype_all"].where(index >= 36).where(index <= 47)
price5 = data_sort["cartype_all"].where(index >= 48).where(index <= 59)
price6 = data_sort["cartype_all"].where(index >= 60).where(index <= 71)
price7 = data_sort["cartype_all"].where(index >= 72).where(index <= 83)
price8 = data_sort["cartype_all"].where(index >= 84).where(index <= 95)
price9 = data_sort["cartype_all"].where(index >= 96).where(index <= 107)
price10 = data_sort["cartype_all"].where(index >= 108).where(index <= 119)
price11 = data_sort["cartype_all"].where(index >= 120).where(index <= 131)
price12 = data_sort["cartype_all"].where(index >= 132).where(index <= 143)

ax.plot(index, price1, "o:")
ax.plot(index, price2, "o:")
ax.plot(index, price3, "o:")
ax.plot(index, price4, "o:")
ax.plot(index, price5, "o:")
ax.plot(index, price6, "o:")
ax.plot(index, price7, "o:")
ax.plot(index, price8, "o:")
ax.plot(index, price9, "o:")
ax.plot(index, price10, "o:")
ax.plot(index, price11, "o:")
ax.plot(index, price12, "o:")
ax.add_patch(Rectangle((138, 79), Month - 140.5, 65, color="white", zorder=10))
st.pyplot(fig2)

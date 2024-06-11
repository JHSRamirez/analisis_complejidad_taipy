
import pandas as pd
import matplotlib.pyplot as plt
from mplcursors import cursor

df = pd.read_csv("gui_complexity_trend.txt")

fig, ax1 = plt.subplots()

ax1.set_xlabel("Revision")
ax1.set_ylabel("Lines of code")
line_1, = ax1.plot(df["rev"], df["n"], label="Lines of code", color="red")

ax2 = ax1.twinx()
ax2.set_ylabel("Complexity")
line_2, = ax2.plot(df["rev"], df["mean"], label="Complexity" ,color="blue")
ax2.legend(handles=[line_1,line_2], loc="lower right")

fig.tight_layout()
plt.grid()
cursor(hover=True)
plt.show()
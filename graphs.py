from matplotlib import colors
import matplotlib.pyplot as plt

yil = [2011, 2012, 2013, 2014, 2015]
oyuncu1 = [8, 10, 12, 7, 9]
oyuncu2 = [7, 12, 5, 15, 21]
oyuncu3 = [18, 20, 22, 25, 19]
"""
# Stack Plot

plt.plot([], [], color="y", label="oyuncu1")
plt.plot([], [], color="r", label="oyuncu2")
plt.plot([], [], color="b", label="oyuncu3")

plt.stackplot(yil, oyuncu1, oyuncu2, oyuncu3, colors=["y", "r", "b"])
plt.title("Yillara gire atilan goller")
plt.xlabel("yil")
plt.xlabel("Gol Sayisi")


plt.legend()
"""
# Pie Grafigi

"""
goal_types = "Penaltı", "Kaleye Atilan Sut", "Serbest Vurus"

goals = [12, 35, 7]
colors = ["y", "r", "b"]
plt.pie(goals, labels=goal_types, colors=colors,
        shadow=True, explode=(0.05, 0.05, 0.05), autopct="%1.1f%%")
plt.show()
"""


# Bar Grafigi
"""
plt.bar([0.25, 1.25, 2.25, 3.25, 4.25], [
        50, 40, 70, 80, 20], label="BMW", width=.5)
plt.bar([0.75, 1.75, 2.75, 3.75, 4.75], [
        80, 20, 20, 50, 60], label="Audi", width=.5)

plt.legend()
plt.xlabel("Gün")
plt.ylabel("Mesafe (km)")
plt.title("Arac Bilgileri")
plt.show()
"""

# histogram grafigi
yaslar = [22, 55, 63, 32, 5, 22, 78, 99, 54, 34,
          23, 56, 12, 34, 67, 62, 73, 73, 87, 94, 47, 74]
yas_gruplari = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

plt.hist(yaslar, yas_gruplari, histtype="bar", rwidth=0.8)
plt.xlabel("yas gruplari")
plt.ylabel("Kisi sayisi")
plt.title("Histogram Grafigi")
plt.show()

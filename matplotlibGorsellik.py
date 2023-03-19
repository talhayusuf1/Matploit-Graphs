import numpy as np
import matplotlib.pyplot as plt

numpyDizisi1 = np.linspace(0, 10, 20)
numpyDizisi2 = numpyDizisi1 ** 2

(benimFigur, benimEksen) = plt.subplots()
plt.show()

# Scatter

plt.scatter(numpyDizisi1, numpyDizisi2)
plt.show()

# Histogram

yeniDizi = np.random.randint(0, 100, 50)
plt.hist(yeniDizi)
plt.show()

# Boxplot standart sapmayı alır

plt.boxplot(yeniDizi)
plt.show()

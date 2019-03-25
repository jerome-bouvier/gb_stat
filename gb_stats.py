import matplotlib.pyplot as plt

size_in_gb = {
    '042016': 18,
    '072016': 21,
    '092016': 24,
    '102016': 26,
    '112016': 27,
    '122016': 28,
    '012017': 29,
    '022017': 30,
    '032017': 31,
    '052017': 35,
    '062017': 37,
    '092017': 41,
    '112017': 44,
    '122017': 47,
    '012018': 48,
    '022018': 49,
    '052018': 55,
    '072018': 63,
    '032019': 55
}

plt.plot(size_in_gb.keys(), size_in_gb.values())
plt.xlabel('date')
plt.ylabel('taille en gigabytes')
plt.title('Evolution de la taille des données')
plt.show()

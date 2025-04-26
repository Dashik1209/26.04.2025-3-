import matplotlib.pyplot as plt
import numpy as np

data = {
    "8 созыв (2021-...)": [342, 64, 21, 10, 23],
    "7 созыв (2016-2021)": [343, 42, 23, 28, 11],
    "6 созыв (2011-2016)": [238, 92, 64, 47, 9],
    "5 созыв (2007-2011)": [315, 57, 35, 30, 13]
}

parties = ["Единая Россия", "КПРФ", "СР", "ЛДПР", "Другие"]
colors = ['blue', 'red', 'green', 'yellow', 'gray']

plt.figure(figsize=(10, 10))

bottom = np.zeros(len(data))

sozyvy = list(data.keys())

for i, party in enumerate(parties):
    party_data = [data[sozyv][i] for sozyv in sozyvy]

    plt.bar(sozyvy, party_data, label=party, color=colors[i])

    bottom += np.array(party_data)

plt.title('Распределение партий в Государственной Думе (стековый график)')
plt.xticks(rotation=15, ha="right")
plt.legend(loc="upper right")
plt.tight_layout()

plt.show()
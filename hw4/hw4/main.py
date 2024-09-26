import matplotlib.pyplot as plt
import pandas as pd
import numpy as np



anime = pd.read_csv('anime.csv')
anime_modified = anime.set_index('type')
labels = anime['type'].unique()


Movie = (len(anime[anime['type'].isin(['Movie'])]))
TV = (len(anime[anime['type'].isin(['TV'])]))
OVA = (len(anime[anime['type'].isin(['OVA'])]))
Special = (len(anime[anime['type'].isin(['Special'])]))
Music = (len(anime[anime['type'].isin(['Music'])]))
ONA = (len(anime[anime['type'].isin(['Movie'])]))
nan = (len(anime[anime['type'].isin(['nan'])]))

print(Movie +TV + OVA + Special + Music + ONA + nan, len(anime))


vals = [Movie, TV, OVA, Special, Music, ONA, nan]

plt.pie(vals, labels=labels)
plt.show()
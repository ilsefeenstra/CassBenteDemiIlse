import pandas as pd
import matplotlib.pyplot as plt

# Transform the csv to a dataframe
data_df = pd.read_csv("train.csv")

pawpularity_score = data_df['Pawpularity']

plt.hist(pawpularity_score, bins=100)
#plt.figsize = figsize = (12, 8)
plt.title("Data distribution of the tabular data")
plt.xlabel("Pawpularity score")
plt.ylabel("Occurence")
plt.xlim(0, 100)
#plt.subplots_adjust(left=0.125, bottom=0.4, right=0.9, top=0.9 )


plt.show()

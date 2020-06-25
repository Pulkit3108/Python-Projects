import pandas as pd 
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt 
print('Modules are imported.')
corona_dataset_csv = pd.read_csv("Datasets/covid19_Confirmed_dataset.csv")
#print(corona_dataset_csv.head())
#print(corona_dataset_csv.shape)
corona_dataset_csv.drop(["Lat","Long"],axis=1,inplace=True)
#print(corona_dataset_csv.head())
corona_dataset_aggregated = corona_dataset_csv.groupby("Country/Region").sum()
#print(corona_dataset_aggregated.head())
#print(corona_dataset_aggregated.shape)
corona_dataset_aggregated.loc["China"].plot()
corona_dataset_aggregated.loc["India"].plot()
corona_dataset_aggregated.loc["Italy"].plot()
plt.legend()
corona_dataset_aggregated.loc['China'][:3].plot()
corona_dataset_aggregated.loc['China'].diff().plot()
#print(corona_dataset_aggregated.loc['China'].diff().max())
countries = list(corona_dataset_aggregated.index)
max_infection_rate=[]
for c in countries:
    max_infection_rate.append(corona_dataset_aggregated.loc[c].diff().max())
corona_dataset_aggregated["max_infection_rate"] = max_infection_rate
#print(corona_dataset_aggregated.head())
corona_data = pd.DataFrame(corona_dataset_aggregated["max_infection_rate"])
#print(corona_data.head())
happiness_report_csv = pd.read_csv("Datasets/worldwide_happiness_report.csv")
#print(happiness_report_csv.head())
useless_cols=["Overall rank","Score","Generosity","Perceptions of corruption"]
happiness_report_csv.drop(useless_cols,axis=1,inplace=True)
#print(happiness_report_csv.head())
happiness_report_csv.set_index("Country or region",inplace=True)
data =corona_data.join(happiness_report_csv,how="inner")
print(data.head())
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(data.corr())
x = data["GDP per capita"]
y = data["max_infection_rate"]
sns.scatterplot(x,np.log(y))
sns.regplot(x,np.log(y))
sns.regplot(x,np.log(y))











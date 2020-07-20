# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path

#Code starts here
data=pd.read_csv(path)

data.rename(columns={'Total':'Total_Medals'}, inplace='True')

print(data.head(10))


# --------------
#Code starts here
data['Better_Event']=np.where(data['Total_Summer']>data['Total_Winter'],"Summer",(np.where(data['Total_Summer']<data['Total_Winter'],'Winter','Both')))

better_event=data['Better_Event'].value_counts(ascending=True).idxmax()

print(better_event)



# --------------
#Code starts here
top_countries=data[['Country_Name','Total_Summer','Total_Winter','Total_Medals']]

top_countries.drop(labels=146,axis=0,inplace=True)

def top_ten(df,col):
    country_list=[]
    for i in range(10):
        top10=df.nlargest(10,col).Country_Name.values[i]
        country_list.append(top10)
    return country_list

top_10_summer=top_ten(top_countries,'Total_Summer')

top_10_winter=top_ten(top_countries,'Total_Winter')

top_10=top_ten(top_countries,'Total_Medals')

common=common=list(set(top_10)&set(top_10_summer)&set(top_10_winter))

print(common)


# --------------
#Code starts here
summer_df=data[data.Country_Name.isin(top_10_summer)]

winter_df=data[data.Country_Name.isin(top_10_winter)]

top_df=data[data.Country_Name.isin(top_10)]

summer_df.set_index('Country_Name')['Total_Summer'].plot(kind='bar')
plt.show()

summer_df.set_index('Country_Name')['Total_Winter'].plot(kind='bar')
plt.show()

summer_df.set_index('Country_Name')['Total_Medals'].plot(kind='bar')
plt.show()




# --------------
#Code starts here
summer_df['Gold_Ratio']=summer_df.Gold_Summer/summer_df.Total_Summer

summer_max_ratio=summer_df.Gold_Ratio.max()

summer_country_gold=summer_df[summer_df.Gold_Ratio==summer_max_ratio].Country_Name.iloc[0]

winter_df['Gold_Ratio']=winter_df.Gold_Winter/winter_df.Total_Winter

winter_max_ratio=winter_df.Gold_Ratio.max()

winter_country_gold=winter_df[winter_df.Gold_Ratio==winter_max_ratio].Country_Name.iloc[0]

top_df['Gold_Ratio']=top_df.Gold_Total/top_df.Total_Medals

top_max_ratio=top_df.Gold_Ratio.max()

top_country_gold=top_df[top_df.Gold_Ratio==top_max_ratio].Country_Name.iloc[0]

print(summer_max_ratio,summer_country_gold,winter_max_ratio,winter_country_gold,top_max_ratio,top_country_gold, sep='\n')


# --------------
#Code starts here
data_1=data

data_1.drop(labels=146,axis=0,inplace=True)

data_1['Total_Points']=data_1.Gold_Total*3+data_1.Silver_Total*2+data_1.Bronze_Total*1

most_points=data_1['Total_Points'].max()

best_country=data_1[data_1.Total_Points==most_points].Country_Name.iloc[0]

print(best_country)


# --------------
#Code starts here
best=data[data.Country_Name==best_country][['Gold_Total','Silver_Total','Bronze_Total']]

best.plot.bar(stacked=True)


plt.xlabel('United States')

plt.ylabel('Medals Tally')

plt.xticks(rotation=45)

plt.show()



"""
=============
This Project tries to visualize some relations related to
i)  Covid-19 Pandemic and its effect at different continents,
ii) Covid-19 Pandemic and how countries at different Economic complexity have been affected,
iii) Covid-19 Pandemic phases/waves in Ireland and Greece.
=============
 Main COVID-19 Data source:
 https://ourworldindata.org/coronavirus-source-data
 "https://covid.ourworldindata.org/data/owid-covid-data.csv"
 GitHub of this is:
 https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv


 Main Economic complexity Data source:
 https://atlas.cid.harvard.edu/rankings

"""

#Import the necessary Packages
import pandas as pd
from pandas.io.json import json_normalize
import requests
import numpy   as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns


#Define the necessary functions:

def first_plot(pd_plot, save_p = False):
    """

    :param pd_plot: it expects the grouped_by_continent_total_deaths
    :return:
    """
    # Plot results in a bar
    plt.style.use("seaborn-darkgrid")
    pd_plot.plot(kind="bar")
    plt.yticks(rotation=45)
    plt.xticks(rotation=20)
    plt.ylabel("Mean of total COVID-19 deaths")
    plt.xlabel("Location by Continent")
    plt.title("Mean of total COVID-19 deaths of the countries at each continent.")
    # fig1 = plt.figure()
    if(save_p):
      plt.savefig("Mean_Covid_Deaths_per_Continent.png")

    plt.show(block=False)

def second_plot(pd_plot, save_p = False):
    """

    :param pd_plot: it expects the grouped_by_continent_total_cases
    :return:
    """
    # Plot results in a bar
    plt.style.use("seaborn-darkgrid")
    pd_plot.plot(kind="bar")
    plt.yticks(rotation=45)
    plt.xticks(rotation=20)
    plt.ylabel("Mean of total COVID-19 cases")
    plt.xlabel("Location by Continent")
    plt.title("Mean of total COVID-19 cases of the countries at each continent.")
    fig2 = plt.figure(2)
    if(save_p):
      plt.savefig("Mean_Covid_Cases_per_Continent.png")

    plt.show(block=False)

def plot_complexity_insights(table_to_print,pd_crosstab, save_p = False):
    fig3 = plt.figure(3)
    plt.style.use("seaborn-darkgrid")
    table_to_print.plot(kind="bar")
    # Rotate tick marks for visibility
    plt.yticks(rotation=45)
    plt.xticks(rotation=20)
    # Set Y-label and X-Label
    plt.xlabel("Countries grouped by Economic Complexity and at Quarters")
    plt.ylabel("Mean of total deaths per million")
    plt.title("Mean of total deaths per million for countries grouped by Economic Complexity Quarters.")
    if(save_p):
      plt.savefig("Econ_Complexity_vs_Mean_Num_Total_Deaths.png")

    plt.show(block=False);

    fig4 = plt.figure(4)
    plt.style.use("seaborn-darkgrid")
    sns.heatmap(pd_crosstab, annot=True, linewidths=.5, vmin=0, vmax=0.16, cmap="Reds")
    # Rotate tick marks for visibility
    plt.yticks(rotation=45)
    plt.xticks(rotation=20)
    # Set Y-label and X-Label
    plt.ylabel("Countries grouped by Economic Complexity and at Quarters")
    plt.xlabel("Location by Continent")
    plt.title(
        "Normalized mean of total deaths per million for countries \n grouped by Economic Complexity Quarters and by Contintent Location.")
    if(save_p):
      plt.savefig("Econ_Complexity_and_Continent_vs_Mean_Num_Total_Deaths.png")

    plt.show(block=False);

def plot_tseries(dt_covid_gr, dt_covid_irl, save_p = False):
    #Some Lists for holding Greece's and Ireland's Lock Down Start Dates:
    irl_wave_start_dates = ["2020-03-12","2020-10-04","2021-01-06"]
    gr_wave_start_dates  = ["2020-03-22","2020-11-04"]
    # Compare two countries
    plt.style.use("seaborn-darkgrid")
    fig, (ax1, ax2) = plt.subplots(2,1)
    ax1.plot(dt_covid_gr.date, dt_covid_gr.new_cases_per_million, label="Greece", color="royalblue")
    ax1.plot(dt_covid_irl['date'],
            dt_covid_irl['new_cases_per_million'],
            label="Ireland",color="coral")

    ax1.set_xlabel("Time(Dates)")
    ax1.set_ylabel("New COVID Cases per Milion")
    ax1.xaxis.set_major_locator(ticker.MaxNLocator(10))
    ax1.legend()

    ax2.plot(dt_covid_gr.date, dt_covid_gr.new_deaths_per_million, label="Greece")
    ax2.plot(dt_covid_irl.date, dt_covid_irl.new_deaths_per_million, label="Ireland")

    ax2.set_xlabel("Time(Dates)")
    ax2.set_ylabel("New COVID Deaths per Milion")
    ax2.xaxis.set_major_locator(ticker.MaxNLocator(10))
    ax2.legend()
    #Add some annotations on
    ax1.annotate("Ireland's 1st Wave Start",
                 xy=(dt_covid_irl[dt_covid_irl['date']==irl_wave_start_dates[0]].date, dt_covid_irl[dt_covid_irl['date']==irl_wave_start_dates[0]].new_cases_per_million),
                 xytext=(dt_covid_irl[dt_covid_irl['date']==irl_wave_start_dates[0]].date, 1000),
                 arrowprops={"arrowstyle": "->", "color": "coral"})
    ax1.annotate("Ireland's 2nd Wave Start",
                 xy=(dt_covid_irl[dt_covid_irl['date']==irl_wave_start_dates[1]].date, dt_covid_irl[dt_covid_irl['date']==irl_wave_start_dates[1]].new_cases_per_million),
                 xytext=(dt_covid_irl[dt_covid_irl['date']==irl_wave_start_dates[1]].date, 1000),
                 arrowprops={"arrowstyle": "->", "color": "coral"})
    ax1.annotate("Ireland's 3rd Wave Start",
                 xy=(dt_covid_irl[dt_covid_irl['date']==irl_wave_start_dates[2]].date, dt_covid_irl[dt_covid_irl['date']==irl_wave_start_dates[2]].new_cases_per_million),
                 xytext=(dt_covid_irl[dt_covid_irl['date']=="2020-10-10"].date, 1500),
                 arrowprops={"arrowstyle": "->", "color": "coral"})

    ax1.annotate("Greece's 1st Wave Start",
                 xy=(dt_covid_gr[dt_covid_gr['date']==gr_wave_start_dates[0]].date, dt_covid_gr[dt_covid_gr['date']==gr_wave_start_dates[0]].new_cases_per_million),
                 xytext=(dt_covid_gr[dt_covid_gr['date']==gr_wave_start_dates[0]].date, 750),
                 arrowprops={"arrowstyle": "->", "color": "royalblue"})
    ax1.annotate("Greece's 2nd Wave Start",
                 xy=(dt_covid_gr[dt_covid_gr['date']==gr_wave_start_dates[1]].date, dt_covid_gr[dt_covid_gr['date']==gr_wave_start_dates[1]].new_cases_per_million),
                 xytext=(dt_covid_gr[dt_covid_gr['date']==gr_wave_start_dates[1]].date, 750),
                 arrowprops={"arrowstyle": "->", "color": "royalblue"})

    ax2.annotate("Ireland's 1st Wave Start",
                 xy=(dt_covid_irl[dt_covid_irl['date']==irl_wave_start_dates[0]].date, dt_covid_irl[dt_covid_irl['date']==irl_wave_start_dates[0]].new_deaths_per_million),
                 xytext=(dt_covid_irl[dt_covid_irl['date']==irl_wave_start_dates[0]].date, 30),
                 arrowprops={"arrowstyle": "->", "color": "coral"})
    ax2.annotate("Ireland's 2nd Wave Start",
                 xy=(dt_covid_irl[dt_covid_irl['date']==irl_wave_start_dates[1]].date, dt_covid_irl[dt_covid_irl['date']==irl_wave_start_dates[1]].new_deaths_per_million),
                 xytext=(dt_covid_irl[dt_covid_irl['date']==irl_wave_start_dates[1]].date, 25),
                 arrowprops={"arrowstyle": "->", "color": "coral"})
    ax2.annotate("Ireland's 3rd Wave Start",
                 xy=(dt_covid_irl[dt_covid_irl['date']==irl_wave_start_dates[2]].date, dt_covid_irl[dt_covid_irl['date']==irl_wave_start_dates[2]].new_deaths_per_million),
                 xytext=(dt_covid_irl[dt_covid_irl['date']=="2020-12-10"].date, 30),
                 arrowprops={"arrowstyle": "->", "color": "coral"})

    ax2.annotate("Greece's 1st Wave Start",
                 xy=(dt_covid_gr[dt_covid_gr['date']==gr_wave_start_dates[0]].date, dt_covid_gr[dt_covid_gr['date']==gr_wave_start_dates[0]].new_deaths_per_million),
                 xytext=(dt_covid_gr[dt_covid_gr['date']==gr_wave_start_dates[0]].date, 20),
                 arrowprops={"arrowstyle": "->", "color": "royalblue"})
    ax2.annotate("Greece's 2nd Wave Start",
                 xy=(dt_covid_gr[dt_covid_gr['date']==gr_wave_start_dates[1]].date, dt_covid_gr[dt_covid_gr['date']==gr_wave_start_dates[1]].new_deaths_per_million),
                 xytext=(dt_covid_gr[dt_covid_gr['date']==gr_wave_start_dates[1]].date, 20),
                 arrowprops={"arrowstyle": "->", "color": "royalblue"})
    if(save_p):
      plt.savefig("Comparison_Irl_vs_Grc.png")

    plt.show(block=True)

def read_csv_return_pd(fname, is_local = True, debug = False):
    """
    :param fname: give a sctring with the name of the file or the full path
    :param is_local: is the file local?
    :return: returns a DataFrame after reading the file
    """
    covid_url_l = "https://covid.ourworldindata.org/data/"
    if is_local == True:
      local_data = pd.read_csv(fname)
    else:
      #Check first if the url is valid
      covid_url_l = covid_url_l+fname
      print(covid_url_l)
      local_data = pd.read_csv(covid_url_l)
      if(debug):
        print(local_data.head())
        print(local_data.info())
        print(local_data.columns)

    return local_data;

def read_json_online(url_name):
    """
    :param url_name: give a sctring with the name of the file or the full path
    :return: returns a DataFrame after reading the file
    """
    local_data = pd.read_json(url_name)
    print(local_data.head())
    print(local_data.info())
    print(local_data.columns)

    return local_data;

#Define Global Variables
#The following 3 gobal variables control some script behaviour
create_plots = True
save_plots   = False
debug_msg    = False

#Define a number of lists which are used to order DataFrames and Select columns on DataFrames
category_order = ['Oceania','Asia', 'Africa', 'South America', 'North America', 'Europe']

#Keep specific columns for coutries codes
countries_lst = ['iso_code','continent','location','date']

#Keep specific columns for COVID-19 statistics
covid_lst     = ['total_cases_per_million', 'new_cases_per_million', 'total_deaths_per_million', 'new_deaths_per_million' ]

# Possible age causes list
causes_lst     = ['median_age', 'aged_65_older', 'aged_70_older', 'extreme_poverty', 'human_development_index']

# These columns will be kept only from the economic complexity DataFrame
c_econ_lst = ["Country", "ECI Rank 2018", "ECI 2018", "COI 2018", "COI Rank 2018"]

# Last Valid which is used at the Covid DataSet
covid_dt_last_date = "2021-01-29"

#Run the main elements of the script

print("Data Analyis First Step: Read the Data Sets, and create the necessary Pandas DataFrames.")
#Create the dt_covid DataFrame by reading the "owid-covid-data.csv"
#Retrieved here: https://covid.ourworldindata.org/data/
dt_covid = read_csv_return_pd("owid-covid-data.csv",False,debug_msg)

#Keep specific columns from the dt_covid DataFrame
dt_covid = dt_covid[countries_lst+covid_lst]

#Rename the location column to Country so it can be merged in the future
#Here is a use of Dictionary
dt_covid = dt_covid.rename(columns={"location": "Country"})

#Print Debug messages
if debug_msg:
  print(dt_covid.info())
  print(dt_covid.columns)

#create the dt_compl_econ DataFrame base on "Country Complexity Rankings 1995 - 2018.csv"
dt_compl_econ = read_csv_return_pd("Country Complexity Rankings 1995 - 2018.csv")

print("Data Analyis Second Step: Keep only the necessary Columns of the Data.")
#Keep only few columns:
dt_compl_econ = dt_compl_econ[c_econ_lst]
#Sort the dt_compl_econ based on the "ECI Rank 2018"
dt_compl_econ = dt_compl_econ.sort_values("ECI Rank 2018", ascending=True)
if debug_msg:
  print(dt_compl_econ.info())
  print(dt_compl_econ.columns)

# Create the necessary Panda's DataFrames for visualization
# acc_dt_covid:
acc_dt_covid = dt_covid[dt_covid["date"]==covid_dt_last_date]

#Keep the data for Greece and Ireland to create time-series
time_series_dt_covid_gr_irl = dt_covid[dt_covid["Country"].isin(["Greece", "Ireland"])]

print("Data Analyis Third Step: Further Transform the Data so to gain Insights.")
#Further Process the Data in order to Visualize them:
#Create the Dataframes for plots 1 and 2:
grouped_by_continent_total_cases  = acc_dt_covid.groupby("continent")[['total_cases_per_million']].mean()
grouped_by_continent_total_deaths = acc_dt_covid.groupby("continent")[['total_deaths_per_million']].mean()

if debug_msg:
  print(grouped_by_continent_total_cases)
  print(grouped_by_continent_total_deaths)

#Merge the following DataFrames to see the relationship of Covid-19 effects and Economic COmplexity:
acc_dt_covid_w_complex_econ = acc_dt_covid.merge(dt_compl_econ[["Country", "ECI Rank 2018", "ECI 2018"]], on='Country', suffixes=('_covdt','_complexdt'))
acc_dt_covid_w_complex_econ = acc_dt_covid_w_complex_econ.sort_values("ECI Rank 2018", ascending=True)

if debug_msg:
    print(acc_dt_covid_w_complex_econ.columns)
    print(acc_dt_covid_w_complex_econ.head(20))
    print(acc_dt_covid_w_complex_econ.tail(20))

#Create a new Column Complexity_Quarter which sets the Quarter in which a coutry is in
num_rows = len(acc_dt_covid_w_complex_econ)
quarter_lst = []
for index, row in acc_dt_covid_w_complex_econ.iterrows():
    #print(index, row['ECI Rank 2018'])
    if(row['ECI Rank 2018']<num_rows/4):
        quarter_lst.append("Q1")
    elif((row['ECI Rank 2018']>=num_rows/4) and (row['ECI Rank 2018']<2*(num_rows/4))):
        quarter_lst.append("Q2")
    elif ((row['ECI Rank 2018'] >= 2*(num_rows/4)) and (row['ECI Rank 2018'] < 3 * (num_rows / 4))):
        quarter_lst.append("Q3")
    else:
        quarter_lst.append("Q4")

#Create a new column
acc_dt_covid_w_complex_econ['Complexity_Quarter'] = quarter_lst
if debug_msg:
  print(acc_dt_covid_w_complex_econ.columns)
  print(acc_dt_covid_w_complex_econ.head(20))
  print(acc_dt_covid_w_complex_econ[28:68])
  print(acc_dt_covid_w_complex_econ.tail(20))

#Develop the last structures used to visualize interesting insights:
#Table:
#Any NaN element will be filled with the zero value
covid_deaths_complexity_group = acc_dt_covid_w_complex_econ.groupby(["Complexity_Quarter"])["total_deaths_per_million"].mean().fillna(0)

#Crosstab for the Heatmap
covid_deaths_complexity_crosstab = pd.crosstab(acc_dt_covid_w_complex_econ["Complexity_Quarter"],acc_dt_covid_w_complex_econ["continent"],
                         values=acc_dt_covid_w_complex_econ["total_deaths_per_million"], aggfunc=np.mean, normalize=True)
covid_deaths_complexity_crosstab = covid_deaths_complexity_crosstab.reindex(category_order, axis="columns")

if debug_msg:
    print(covid_deaths_complexity_group)
    print(covid_deaths_complexity_crosstab)

print("Data Analyis Forth Step: Visualize the Insightful Data.")
#Create the Plots by calling the proper functions:
if(create_plots):
    first_plot(grouped_by_continent_total_cases.reindex(category_order), save_plots)
    second_plot(grouped_by_continent_total_deaths.reindex(category_order), save_plots)
    plot_complexity_insights(covid_deaths_complexity_group, covid_deaths_complexity_crosstab, save_plots)
    plot_tseries(time_series_dt_covid_gr_irl[time_series_dt_covid_gr_irl["iso_code"]=='GRC'],time_series_dt_covid_gr_irl[time_series_dt_covid_gr_irl["iso_code"]=='IRL'], save_plots)
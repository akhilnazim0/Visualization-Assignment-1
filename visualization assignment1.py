# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 18:32:22 2022

@author: akhil
"""

#importing libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

"""
line plot

"""
#Read the data from csv file
uk= pd.read_csv("UK RENEWABLE ENERGY.csv")

def linePlot():
    """Analyzing and plotting six lines of each sources to find the trend  """
    plt.figure()
    # plot the six sources with labels
    plt.plot(uk["Year"], uk["Energy from renewable & waste sources"], label="From Renewable & Waste sources")
    plt.plot(uk["Year"], uk["Hydroelectric power"], label="From Water")
    plt.plot(uk["Year"], uk["Wind, wave, tidal"], label="From Wind, wave, tidal")
    plt.plot(uk["Year"], uk["Wood"], label="From Wood")
    plt.plot(uk["Year"], uk["Charcoal"], label="From Charcoal")
    plt.plot(uk["Year"], uk["Biomass"], label="From Biomass")
    # set labels and show the legend
    plt.xlabel("Year")
    plt.ylabel("Energy Consumption from Renewable Sources")
    plt.legend()
    plt.savefig("linegraph.png")
    plt.show()

"""
Bar plot

"""
def barPlot():
    """Analyzing and plotting bar graph of three sources to see the comparison between them """
    plt.figure()
    # plot the three sources with labels
    plt.bar(uk["Year"], uk["Energy from renewable & waste sources"], label="From Renewable & Waste sources", alpha= 0.3)
    plt.bar(uk["Year"], uk["Wind, wave, tidal"], label="From Wind, wave, tidal")
    plt.bar(uk["Year"], uk["Hydroelectric power"], label="From Water", alpha= 0.5)
    # set labels and show the legend
    plt.xlabel("Year")
    plt.ylabel("Energy Consumption from Three Sources")
    plt.legend()
    plt.savefig("bargraph.png")
    plt.show()

"""
Pie plot

"""
#read the data from csv file
tb= pd.read_csv("TB Patients HIV positive tested.csv")

def pieChart():
    """Analyzing the comparison of each countries in the case of Tuberculosis Patients with HIV Positive in 2020"""
    # pie chart for the four countries
    plt.figure()
    #autopct is used for adding percentage to portions and adding labels to pie graph
    plt.pie(tb["FactValueNumeric"], labels= tb["Location"],autopct=("%1.1f%%"))
    plt.title("Tuberculosis Patients with HIV Positive in 2020 in four countries", size=15)
    plt.savefig("piegraph.png")
    plt.show()

#calling lineplot function
linePlot()
#calling barplot function
barPlot()
#calling piechart function
pieChart()







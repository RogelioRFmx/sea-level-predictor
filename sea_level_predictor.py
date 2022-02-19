import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    # Create scatter plot
    x=df['Year']
    y=df['CSIRO Adjusted Sea Level']
    fig, ax= figsize=(16,6)
    ax = plt.scatter(x, y)
    # Create first line of best fit
    sr1 = pd.Series([int(i) for i in range(1880, 2050)])
    res = linregress(x,y)
    # print(f"R-squared: {res.rvalue**2:.6f}")
    plt.plot(x, y, 'o', label='original data')
    plt.plot(sr1, res.intercept + res.slope*sr1, 'r', label='fitted line')   
    # Create second line of best fit
    recent = df[df['Year'] >= 2000]
    sr2 = pd.Series([int(i) for i in range(2000, 2050)])
    res2=linregress(recent['Year'], recent["CSIRO Adjusted Sea Level"])
    plt.plot(sr2, res2.intercept + res2.slope*sr2, 'r', label='new best fit line after year 2000', color="purple")
    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title("Rise in Sea Level")
    plt.legend()
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
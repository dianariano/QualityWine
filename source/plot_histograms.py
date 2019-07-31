import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def plotHistograms(columns, df):

    try:

        fig, axes = plt.subplots(nrows=2, ncols=2)
        ax0,ax1,ax2,ax3 = axes.flatten()

        ax0.hist(df[columns[0]].values, density=True, histtype='bar', label=columns[0])
        ax0.legend(prop={'size': 10})
        ax0.set_title('Distribution of ' + columns[0])

        ax1.hist(df[columns[1]], density=True, histtype='bar', label=columns[1])
        ax1.legend(prop={'size': 10})
        ax1.set_title('Distribution of ' + columns[1])

        ax2.hist(df[columns[2]], density=True, histtype='bar', label=columns[2])
        ax2.legend(prop={'size': 10})
        ax2.set_title('Distribution of ' + columns[2])

        ax3.hist(df[columns[3]], density=True, histtype='bar', label=columns[3])
        ax3.legend(prop={'size': 10})
        ax3.set_title('Distribution of ' + columns[3])

        fig.tight_layout()
        plt.show()

    except:

        plt.hist(df[columns[0]], density=True, histtype='bar', label=columns[0])
        plt.legend(prop={'size': 10})

        plt.show()

    return None
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def plotHistograms(columns, df):

    fig, axes = plt.subplots(nrows=4, ncols=4)

    ax0,ax1,ax2,ax3,ax4,ax5,ax6,ax7,ax8,ax9,ax10,ax11,ax12,ax13, ax14, ax15 = axes.flatten()

    j=0

    for i in range(4):
        
        if i < 4:
            colors = ['red', 'tan', 'lime']
            axes[j][i].hist(df[columns[j*4 + i]], density=True, histtype='bar', label=colors)
            axes[j][i].legend(prop={'size': 10})
            axes[j][i].set_title('bars with legend')
        else:
            j+=1

    fig.tight_layout()
    plt.show()
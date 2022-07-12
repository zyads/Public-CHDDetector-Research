# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib.animation as animation
# import matplotlib.ticker as ticker
# import matplotlib.dates as mdates
# import matplotlib.cm as cm
# import matplotlib.colors as colors
# import matplotlib.gridspec as gridspec
# import matplotlib.patches as patches
# import matplotlib.lines as mlines
# import matplotlib.text as mtext
# import matplotlib.image as mimage
# import matplotlib.pyplot as plt
# import matplotlib.widgets as mwidgets
# import matplotlib.transforms as mtransforms
# import matplotlib.artist as martist
# import matplotlib.ticker as mticker
# import matplotlib.axis as maxis
# import matplotlib.spines as mspines
# import matplotlib.font_manager as mfontmgr
# import matplotlib.backends.backend_agg as mbackend_agg
# import matplotlib.backends.backend_pdf as mbackend_pdf

# from IPython.display import display
# import matplotlib.pyplot as plt
# %matplotlib inline
# import numpy as np
# import os
# import shutil
# import posixpath

# import wfdb


import os
import matplotlib.pyplot as plt
import numpy as np
import shutil
import posixpath
import wfdb

def wfmc_file_to_data(bidmc_file):
    #load data
    data = wfdb.rdsamp(bidmc_file)
    #convert to numpy array
    data = np.array(data[0])
    #return data
    return data

#make waveform viewer given bidmc##.dat file
def make_wfviewer(bidmc_file, save_dir=None, show_fig=True):
    #load data
    data = wfmc_file_to_data(bidmc_file)
    #make figure
    fig = plt.figure(figsize=(10,10))
    ax = fig.add_subplot(111)
    #plot data
    ax.plot(data[:,0], data[:,1], 'b')
    #set axis limits
    ax.set_xlim(0, data[:,0].max())
    ax.set_ylim(data[:,1].min(), data[:,1].max())
    #set axis labels
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Amplitude (mV)')
    #set title
    ax.set_title('Waveform Viewer')
    #show figure
    if show_fig:
        plt.show()
    #save figure
    if save_dir is not None:
        fig.savefig(os.path.join(save_dir, 'wfviewer.png'))
    #return figure
    return fig

#now allow it to run
if __name__ == '__main__':
    # ask for file and run
    bidmc_file = input('Enter bidmc file name: ')
    # use current directory for saving
    save_dir = os.getcwd()
    # make figure
    fig = make_wfviewer(bidmc_file, save_dir)
    # show figure
    plt.show()
    # save figure
    fig.savefig(os.path.join(save_dir, 'wfviewer.png'))
    # close figure
    plt.close(fig)
    # print success message
    print('Successfully made wfviewer.png')
    
    # data = wfmc_file_to_data(bidmc_file)
    # if save_dir is None:
    #     save_dir = os.getcwd()
    # if not os.path.exists(save_dir):
    #     os.makedirs(save_dir)
    # save_file = os.path.join(save_dir, bidmc_file.split('/')[-1].split('.')[0] + '.png')
    # fig = plt.figure(figsize=(10,10))
    # ax = fig.add_subplot(111)
    # ax.plot(data[:,0], data[:,1])
    # ax.set_xlabel('Time (s)')
    # ax.set_ylabel('Voltage (mV)')
    # ax.set_title(bidmc_file.split('/')[-1].split('.')[0])
    # plt.savefig(save_file)
    # if show_fig:
    #     plt.show()
    # plt.close()
    # return save_file

 #load data
# data = wfdb.rdsamp(bidmc_file)
# #get signal names
# sig_names = data['signal_names']
# #get signal data
# sig_data = data['signal']
# #get sampling rate
# fs = data['fs']
# #get time vector
# t = np.arange(0, len(sig_data[0]))/fs
# #get signal labels
# sig_labels = []
# for i in range(len(sig_names)):
#     sig_labels.append(sig_names[i][0])
# #get signal units
# sig_units = []
# for i in range(len(sig_names)):
#     sig_units.append(sig_names[i][1])
# #get signal descriptions
# sig_desc = []
# for i in range(len(sig_names)):
#     sig_desc.append(sig_names[i][2])
# #get signal annotations
# sig_ann = []
# for i in range(len(sig_names)):
#     sig_ann.append(sig_names[i][3])

# #make figure
# fig = plt.figure()
# #make subplot
# ax = fig.add_subplot(111)
# #plot signal data
# for i in range(len(sig_data)):
#     ax.plot(t, sig_data[i], label=sig_labels[i])
# #set x-axis label
# ax.set_xlabel('Time (s)')
# #set y-axis label
# ax.set_ylabel('Amplitude (mV)')
# #set title
# ax.set_title(bidmc_file)
# #set legend
# ax.legend()
# #show figure
# if show_fig:
#     plt.show()
# #save figure
# if save_dir is not None:
#     fig.savefig(os.path.join(save_dir, bidmc_file+'.png'))
# #close figure
# plt.close(fig)
# return

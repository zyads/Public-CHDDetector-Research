# make waveform viewer for ecg and ppg data using wfdb. Then detect anomoly with heartdetectdisease.py

# from IPython.display import display
import matplotlib.pyplot as plt
# %matplotlib inline
# import numpy as np
import os
# import shutil
# import posixpath

import wfdb

#import any machine learning library useful for heart disease detection. Maybe pytorch or tensorflow.

#  Demo 1 - Read a WFDB record using the 'rdrecord' function into a wfdb.Record object.
# Plot the signals, and show the data.
# record = wfdb.rdrecord('sample-data/a103l') 
# wfdb.plot_wfdb(record=record, title='Record a103l from PhysioNet Challenge 2015') 
# display(record.__dict__)

# Can also read the same files hosted on PhysioNet https://physionet.org/content/challenge-2015/1.0.0
# in the /training/ database subdirectory.
# record = wfdb.rdrecord('a103l', pn_dir='challenge-2015/training/')
# wfdb.plot_wfdb(record=record, title='Record a103l from PhysioNet Challenge 2015') 
# display(record.__dict__)

# #save display to be opened
# plt.savefig('a103l.png')

# #open display in browser, fails since in venv
# plt.show()

#use demo1 into a function takes in file name into specific directory
def plot_record(record_name, save_dir=None):
    record = wfdb.rdrecord(record_name)
    wfdb.plot_wfdb(record=record, title=record_name)
    #save the plot as a png file in specified directory
    if save_dir is not None:
        #if directory doesnt exist make it
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        # make record name equal to base name of path
        record_name = os.path.basename(record_name)
        plt.savefig(os.path.join(save_dir, record_name + '.png'))
    plt.close()
    # plt.savefig(record_name + '.png')
    # plt.close()
    return

#Take in array of record names and output array of record objects... put in specified directory
def plot_records(record_names, save_dir=None):
    records = []
    #if specified directory of files run it on each file name
    # if os.path.isdir(record_names):
    #     for record_name in os.listdir(record_names):
    #         records.append(wfdb.rdrecord(record_name))
    #         #plot each record in directory
    #         plot_record(record_name)
    #if specified file run it on each file name
    # elif os.path.isfile(record_names):
    for record_name in record_names:
        records.append(wfdb.rdrecord(record_name))
        #call plot_record for each record
        plot_record(record_name, save_dir)
    return records

# Demo 2 - Read certain channels and sections of the WFDB record using the simplified 'rdsamp' function
# which returns a numpy array and a dictionary. Show the data.
# signals, fields = wfdb.rdsamp('sample-data/s0010_re', channels=[14, 0, 5, 10], sampfrom=100, sampto=15000)
# display(signals)
# display(fields)

# # Can also read the same files hosted on Physionet
# signals2, fields2 = wfdb.rdsamp('s0010_re', channels=[14, 0, 5, 10], sampfrom=100, sampto=15000, pn_dir='ptbdb/patient001/')


# make main
if __name__ == '__main__':
    #use plot_record to plot waveform as many times as you user specifies
    # plot_record(input("Enter record name: "))

    # ask what save dir or press enter to do in current directory
    save_dir = input("Enter save directory or press enter to save in current directory: ")

    #ask are you specificying general file name of entire directory or specific file name
    if input("Are you specificying general file name for entire directory (y) or manually doing file names (n)") == "n":
        plot_records(input("Enter record names: ").split(), save_dir)
    else:
        #ask for general file name and ask for how many files with that file name to loop through
        filename = input("Enter general file name: ")
        num_files = input("Enter number of files: ")
        record_names = []
        #append all file names to an array and then pass it to plot_records
        for i in range(1, int(num_files)): 
            if i < 10:
                record_names.append(filename + '0' + str(i))
            else:
                record_names.append(filename + str(i))
        plot_records(record_names, save_dir)
    #ask user if they want to continue
    answer = input("Continue to next graph? (y/n): ")
    if answer == 'n':
        exit()
    


    # make it option to use the remote Database
    # make it option to do next graphs
    # use record objects created from graphs downstream


    

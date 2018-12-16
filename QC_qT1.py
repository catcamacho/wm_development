#! /bin/python

from nibabel import load
from matplotlib import pyplot as plt
from os import getcwd
from sys import version_info

filepath = getcwd()
qT1 = filepath + '/qt1_t1.nii.gz'

if version_info[0] < 3:
	subject = raw_input('Please enter the subject ID: ')
else:
	subject = input('Please enter the subject ID: ')
	
print('Generating histogram of T1 values in milliseconds...')

qT1_image = load(qT1)
qT1_data = qT1_image.get_data()

plt.Figure()
data = qT1_data.flatten()
plt.hist(data, bins = range(100,4600,100))
plt.title("Distribution of T1 values for subject " + subject)
plt.savefig(filepath + '/' + subject + '_T1_histogram.png')
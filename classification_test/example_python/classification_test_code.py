#!/usr/bin/env python
##
# ===============================================================================
# Metadata
# ===============================================================================
__author__ = 'awc'
__contact__ = 'aiwern.chung@childrens.harvard.edu'
__copyright__ = ''
__license__ = ''
__date__ = '01/2020'
__version__ = '0.1'

# ===============================================================================
# Import statements
# ===============================================================================

import os
import pdb
import csv
import random
import numpy



def classification_random(datadir, outputdir):

    subj_strs = os.listdir('%s/Test' % datadir)
    outputfile = '%s/classification.csv' % outputdir

    with open(outputfile, 'w') as resultsFile:
        writer = csv.writer(resultsFile)

        for subject in numpy.sort(subj_strs):

            row = []
            row.append(subject)
            row.append(random.getrandbits(1))
            row.append(random.random())

            writer.writerow(row)

#!/usr/bin/env python                                            
#
# cni_challenge_chris ds ChRIS plugin app
#
# (c) 2016-2019 Fetal-Neonatal Neuroimaging & Developmental Science Center
#                   Boston Children's Hospital
#
#              http://childrenshospital.org/FNNDSC/
#                        dev@babyMRI.org
#
# ===============================================================================
# Metadata
# ===============================================================================
__author__ = 'AWC'
__contact__ = 'aiwern.chung@childrens.harvard.edu'
__copyright__ = ''
__license__ = ''
__date__ = '11/2019'
__version__ = '0.1'

# ===============================================================================
# Import statements
# ===============================================================================
import os
import sys
sys.path.append(os.path.dirname(__file__))

# import the Chris app superclass
from chrisapp.base import ChrisApp
# Import a python function that performs a matrix rotation
from example_python.classification_test_code import  classification_random

Gstr_title = """

            _  _____  _____  __   _____      _           _ _                       
           (_)/ __  \|  _  |/  | |  _  |    | |         | | |                      
  ___ _ __  _ `' / /'| |/' |`| | | |_| | ___| |__   __ _| | | ___ _ __   __ _  ___ 
 / __| '_ \| |  / /  |  /| | | | \____ |/ __| '_ \ / _` | | |/ _ \ '_ \ / _` |/ _ \\
| (__| | | | |./ /___\ |_/ /_| |_.___/ / (__| | | | (_| | | |  __/ | | | (_| |  __/
 \___|_| |_|_|\_____/ \___/ \___/\____/ \___|_| |_|\__,_|_|_|\___|_| |_|\__, |\___|
                                    ______                               __/ |     
                                   |______|                             |___/      

"""

Gstr_synopsis = """

(Edit this in-line help for app specifics. At a minimum, the 
flags below are supported -- in the case of DS apps, both
positional arguments <inputDir> and <outputDir>; for FS apps
only <outputDir> -- and similarly for <in> <out> directories
where necessary.)

    NAME

       classification_test.py 

    SYNOPSIS

        python classification_test.py                                         \\
            [-h] [--help]                                               \\
            [--json]                                                    \\
            [--man]                                                     \\
            [--meta]                                                    \\
            [--savejson <DIR>]                                          \\
            [-v <level>] [--verbosity <level>]                          \\
            [--version]                                                 \\
            [--dir]                                                     \\
            <inputDir>                                                  \\
            <outputDir> 

    BRIEF EXAMPLE

        * Black box execution of a python example to read in from a folder of CNI Challenge Test cases and 
            output "prediction" labels in a text file for evaluation module.
            
            Top level folder name can be anything. Data and phenotypic data are in subdirectories 'Test' and
            'SupportingInfo', respectively.

            mkdir inputdir outputdir && chmod 777 outputdir
            python classification_test.py inputdir outputdir

            Output will be in outputdir/classification.csv

    DESCRIPTION

        `classification_test.py` has been created as a test for plugins to run on CNI Challenge test data

    ARGS

        <inputDir> 
        Mandatory. A directory which contains all necessary input files.
        
        <outputDir>
        Mandatory. A directory where output will be saved to. Must be universally writable to.

        [-h] [--help]
        If specified, show help message and exit.
        
        [--json]
        If specified, show json representation of app and exit.
        
        [--man]
        If specified, print (this) man page and exit.

        [--meta]
        If specified, print plugin meta data and exit.
        
        [--savejson <DIR>] 
        If specified, save json representation file to DIR and exit. 
        
        [-v <level>] [--verbosity <level>]
        Verbosity level for app. Not used currently.
        
        [--version]
        If specified, print version number and exit. 

"""


class classification_test(ChrisApp):
    """
    ChRIS plugin to create a Docker image to run on the CNI Challenge Test dataset.
    """
    AUTHORS                 = 'AWC (aiwern.chung@childrens.harvard.edu)'
    SELFPATH                = os.path.dirname(os.path.abspath(__file__))
    SELFEXEC                = os.path.basename(__file__)
    EXECSHELL               = 'python3'
    TITLE                   = 'ChRIS plugin test to create a Docker image to run on the CNI Challenge Test dataset'
    CATEGORY                = ''
    TYPE                    = 'ds'
    DESCRIPTION             = 'ChRIS plugin test to create a Docker image to run on the CNI Challenge Test dataset'
    DOCUMENTATION           = 'http://wiki'
    VERSION                 = '0.1'
    ICON                    = '' # url of an icon image
    LICENSE                 = 'Opensource (MIT)'
    MAX_NUMBER_OF_WORKERS   = 1  # Override with integer value
    MIN_NUMBER_OF_WORKERS   = 1  # Override with integer value
    MAX_CPU_LIMIT           = '' # Override with millicore value as string, e.g. '2000m'
    MIN_CPU_LIMIT           = '' # Override with millicore value as string, e.g. '2000m'
    MAX_MEMORY_LIMIT        = '' # Override with string, e.g. '1Gi', '2000Mi'
    MIN_MEMORY_LIMIT        = '' # Override with string, e.g. '1Gi', '2000Mi'
    MIN_GPU_LIMIT           = 0  # Override with the minimum number of GPUs, as an integer, for your plugin
    MAX_GPU_LIMIT           = 0  # Override with the maximum number of GPUs, as an integer, for your plugin

    # Use this dictionary structure to provide key-value output descriptive information
    # that may be useful for the next downstream plugin. For example:
    #
    # {
    #   "finalOutputFile":  "final/file.out",
    #   "viewer":           "genericTextViewer",
    # }
    #
    # The above dictionary is saved when plugin is called with a ``--saveoutputmeta``
    # flag. Note also that all file paths are relative to the system specified
    # output directory.
    OUTPUT_META_DICT = {}

    def define_parameters(self):
        """
        Define the CLI arguments accepted by this plugin app.
        Use self.add_argument to specify a new app argument.

        e.g.
        To pass in a string:

        self.add_argument('--rot', dest='rot', type=str, optional=False,
                          help='Type string: Name of file containing rotation matrix')
        """


    def run(self, options):
        """
        Define the code to be run by this plugin app.
        """
        print(Gstr_title)
        print('Version: %s' % self.get_version())

        # ===============================================
        # Initialising variables
        # ===============================================
        inputdir_data = '%s' % (options.inputdir)
        outputpath = '%s' % (options.outputdir)

        # ===============================================
        # Call code
        # ===============================================

        # Call python module
        print("\n")
        print("\tCalling python code to do some ranrandom task for testing...")
        #rotate_matrix(str_rotation_matrix, str_vectors, out_str)
        classification_random(inputdir_data, outputpath)
        print ("\tOutput will be in %s/classification.csv" % outputpath)
        print("====================================================================================")

    def show_man_page(self):
        """
        Print the app's man page.
        """
        print(Gstr_synopsis)


# ENTRYPOINT
if __name__ == "__main__":
    chris_app = classification_test()
    chris_app.launch()

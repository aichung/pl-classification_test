pl-cni_challenge_chris
================================

.. image:: https://badge.fury.io/py/cni_challenge.svg
    :target: https://badge.fury.io/py/cni_challenge

.. image:: https://travis-ci.org/FNNDSC/cni_challenge.svg?branch=master
    :target: https://travis-ci.org/FNNDSC/cni_challenge

.. image:: https://img.shields.io/badge/python-3.5%2B-blue.svg
    :target: https://badge.fury.io/py/pl-cni_challenge

.. contents:: Table of Contents


Abstract
--------

This app has been created as part of the MICCAI CNI 2019 Transfer-Learning Challenge (http://www.brainconnectivity.net/challenge.html) to classify networks between ADHD and Control connectomes.

The purpose of this repo is for you to be able to containerise your solution into a Docker image and run it on the hidden test data to see how your method performs. This has been made this possible via the ChRIS open-source neuroimaging platform.

Using Docker images allows you to parcel your solution in your choice of open-source language and version. And it enables others to easily run your solution without having to install multiple programs required for execution.

The ``cni_challenge_chris.py`` app in this this repo is a wrapper for you to add your code/package which is then containerised by Docker. While this is coded in Python and currently contains a bare bones example to include your Python, adding your code in other languages are possible.

For further information on the Challenge and where to download the training and validation datasets, see http://www.brainconnectivity.net/challenge.html

``cni_challenge_chris.py`` is a ChRIS-based application: https://github.com/FNNDSC/CHRIS_docs, for more information on the original ChRIS-app: https://github.com/FNNDSC/cookiecutter-chrisapp.


Synopsis
--------

This bare bones example demonstrates a python program which performs a rotation on a list of vectors. It will demonstrate how to pass in string inputs, read in and output to respective, mandatory directories, and how to incorporate python code and packages for the app to retrieve and for DockerHub to containerise.

.. code::

    python cni_challenge_chris.py                                         \
        [-v <level>] [--verbosity <level>]                          \
        [--version]                                                 \
        [--man]                                                     \
        [--meta]                                                    \
        <inputDir>                                                  \
        <outputDir>                                                 \
        [--run_option < python || C >]                              \
        [--rot <matrix_file.txt>]                                   \

Installation Requirements and Quick Setup
----------------------------

1. Install ``Python`` (3.5+) and ``pip`` (which is usually installed with Python)
2. Create a GitHub account on https://github.com/ if you don't already have one, and install on machine.
3. Create a DockerHub account on https://hub.docker.com/ if you don't already have one.
4. Install latest ``Docker`` (17.04.0+) if you want to test your plugin's Docker image and containers on your local machine. 
   To install on Ubuntu 18.04:      
      
.. code:: bash

            apt-get remove docker docker-engine docker.io 
            apt install docker.io  
    
Otherwise, visit https://docs.docker.com/install/ for installation directions

5. Fork this pl-CNI_challenge_ChRIS repository to your GitHub.
6. Log onto your DockerHub account and create a new repository with automated build.
   In 'Account Settings' -> 'Linked Accounts', connect your GitHub account to DockerHub.

   Then back in your DockerHub home, click the ``Create Repository +``  button. The website page will walk you through setting up the automated build. When prompted for the GitHub repository that you’d like to use for the automated build select the pl-CNI_challenge_ChRIS repository that you just forked/cloned. Name the Docker repository ${cni_challenge_DockerRepo} and make it Public.

   **It is extremely important that you tag your automatically built docker image with an appropriate version number based on your GitHub tags**.
   Create a new build rule by clicking the ``BUILD RULES +``  button. A good rule good be **Source type:** ``Tag``,
   **Source:** ``/^[0-9.]+$/`` and **Docker Tag:** ``version-{sourceref}``.

   Do not delete the default build rule that is already in place, this handles the 'latest' tag for pulling the most recent Docker image.

   Click ``Create && Build``  button to finish the setup and trigger the automated build.
   For more information on Automated Builds, see https://docs.docker.com/docker-hub/builds/. 

   After the build has completed, the ``cni_challenge_chris`` bare bones example is now available as a Docker image to be pulled from your DockerHub. The link to it will be ${your_Docker_account name}/${cni_challenge_DockerRepo}.

Arguments
---------

.. code::

    <inputDir> 
    Mandatory. A directory which contains all necessary input files.
        
    <outputDir>
    Mandatory. A directory where output will be saved. Must be universally writable to.

    [-v <level>] [--verbosity <level>]
    Verbosity level for app. Not used currently.

    [--version]
    If specified, print version number. 
    
    [--man]
    If specified, print (this) man page.

    [--meta]
    If specified, print plugin meta data.


Run
----

This ``plugin`` can be run in two modes: natively as a python package or as a containerised Docker image.

Run locally
~~~~~~~~~~~~

.. code:: bash

    cni_challenge_chris.py --man

to get inline help. And the following to run the bare-bones example:

.. code:: bash

    cni_challenge_chris.py /destination/to/inputdir /destination/to/outputdir


Using ``docker run``
~~~~~~~~~~~~~~~~~~~~

Pull the latest ``cni_challenge`` image to your machine:

.. code:: bash

    docker pull ${your_Docker_account name}/${cni_challenge_DockerRepo}

To run using ``docker``, be sure to assign the input directory to ``/incoming`` and the output directory to ``/outgoing``. *Make sure that the* ``$(pwd)/outputdir`` *directory is world writable!* These directories must be named ``inputdir`` and ``outputdir``. 
For the bare bones example, copy the expected input files (``rotation_matrices.txt`` and  ``vectors.txt``) from the GitHub repo and place it in ``inputdir``.

.. code:: bash

    mkdir inputdir outputdir && chmod 777 outputdir
    cp ${cni_challenge_github_repo}/inputdir/* $(pwd)/inputdir

Now, prefix all calls with 

.. code:: bash

    sudo docker run --rm -v $(pwd)/inputdir:/incoming -v $(pwd)/outputdir:/outgoing ${your_Docker_account name}/${cni_challenge_DockerRepo} cni_challenge_chris.py /incoming /outgoing

The output file of rotated vectors,  ``classifications.csv``, will be in  ``outputdir``.

Our barebones Docker image can be retrieved (from DockerHub 'aiwc') and executed (calling 'man') on your machine as follows (with directories 'inputdir' and 'outputdir' as specified above):

.. code:: bash

    docker pull aiwc/pl-cni_challenge
    sudo docker run --rm -v $(pwd)/inputdir:/incoming -v $(pwd)/outputdir:/outgoing      \
                 aiwc/pl-cni_challenge cni_challenge.py                                  \
                 --man                                                                   \
                 /incoming /outgoing


App and Challenge Requirements
------------------------------

The input and outputs detailed below are necessary to create a ChRIS-compatible plugin to specifically evaluate your solution on the Challenge hidden test data.

* Python packages that are required should be listed in ``requirements.txt`` which will be pip installed and included in the Docker container.
* For implementations in C or C++, the executable pl-cni_challenge wrapper will create the executable before being passed into DockerHub. This means that make instructions (``makefile``) should be included in ``Dockerfile``.

The following requirements are to enable execution of your solution with outputs that our evaluation module can read-in to assess your performance.

* We expect to be able to run your Docker image on the test data with the following command:

.. code:: bash

    sudo docker run --rm -v $(pwd)/inputdir:/incoming -v $(pwd)/outputdir:/outgoing ${your_Docker_account name}/${cni_challenge_DockerRepo} cni_challenge.py /incoming /outgoing

So please remove the mandatory arguments/assignments that were included as examples in the barebones repo to help you (``--rot`` and ``--run_option``)

* Input and output directories are named ``inputdir`` and ``outputdir``, respectively. Your code should read in data from ``inputdir`` as is structured in the training and validation data releases for the CNI 2019 challenge (http://www.brainconnectivity.net/challenge_data.html) as the test data will be of the same form.


* Your code should output _two_ text files in ``outputdir`` called ``classification.txt`` and ``scores.txt``.       
    ``classification.txt`` should contain the subject ID, and the corresponding subject's classification label, with one subject per row (i.e. two columns, the first containing values of type string, the second type int). Labels should be 0 = Control, and 1 = Patient. 
    ``scores.txt`` should contain the subject ID, and the corresponding subject's prediction probability/score, with one subject per row (i.e. two columns, the first containing values of type string, the second of floats). 
* Do not include the Challenge training or validation data in your Docker image. 
* The code to evaluate the performance of your submission is pl-cni_challenge/cni_challenge/evaluation/classification_metrics.py, which will be executed as: 

.. code:: bash

    classification_metrics.py -p classification.csv score.csv -g ${goundtruth_file} -o ${output_file}

For information on our performance evaluation criterias, see: http://miccai.brainconnectivity.net/challenge_eval.html



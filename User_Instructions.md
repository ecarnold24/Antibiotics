# Prerequisites

The OpenPrescribing toolkit requires the following dependencies:
- Juypter notebook version 6.0.1
- Python release Python 3.7.3
- Pandas package installed
- Matplotlib package installed
- Matplotlib.pyplot package installed


# How to use the OpenPrescribinToolkit
Here we describe how to access the OpenPrescribingToolkit for use within a Juypter notebook. This package can be run from the terminal , or command line but we have chosen Jupyter notebook because of its' user friendly interface for data analysis. 

1. Download OpenPrescribingToolkit.py
2. Open a new Juypter Notebook session
3. Run the following code within juypter notebook. Please note you may need to change the filepath depending on where the downloaded OpenPrescribingToolkit.py file is saved.

        %run ./OpenPrescribingToolkit.py
        
The OpenPrescrbingToolkit is ready to use!<br>

Please see OpenPrescribingToolkit_commands_Documentation.md for information about the functions within this Toolkit.

***Sam's Instructions***

## In order to run the script successfully, please download the run_pipeline_python2.7.py and the measures.csv file.
  - `run_pipeline_python2.7.py` is the python executable to run the pipeline.
  - `measures.csv` is the data file that the python script points to.
  
  
# In order to run successfully, please find this help guide:
  - Before running for the first time, please edit the `run_pipeline_python2.7.py` file directly.
  - On line 13, please input the path to the `measures.csv` [default is same working directly as python script]
  - On line 19, please set `run_test_module` to `True`. This will run the test module and ensure the script is running correctly.
  - The test module will output 5 graphs to current working directory, and a number of data to the console, please check that these are correct and not errored [note that some of the data on the console relates to the graphs]
  - Once `run_test_module` has been satisfied, please set to `False` by editing the `run_pipeline_python2.7.py` file directly.
      - If `run_test_module` is set to `True`, no other script functionality will run
  
  - Next, please set the following criteria on `lines 23-34` of the `run_pipeline_python2.7.py` to user desirability [default is all to be `True`]. Setting them to `False` means that function will not run.
      - `run_identify_outliers [default = True]` ##This will identify outliers in the data file and print a boxplot
      - `print_outliers_to_console [default = True (requires run_identify_outliers to be True)]` ##This will print the identified outliers to the console.
      - `data_import_test [default = True]` ##Sanity checks the input file. Checks if the required number of columns are present and that the data can be sliced, so that it is compatible with the rest of the script.
      - `plot_trends_for_all_surgeries [default = True]` ##For each unique surgery in the data file, plot prescribing trends, all on the same axis.
      - `plot_trends_combining_all_surgeries [default = True]` ##Combines prescribing data for all surgeries in data file and plots as a single line.
      - `plot_trends_for_one_surgery [default = True]` ##Pick one surgery in input and plot prescribing trends for that one surgery
      - `plot_trends_for_one_surgery_id [default = 'P84071']` ##ID for plot_trends_for_one_surgery
      - `plot_trends_for_two_surgeries [default = True]` ##Pick two surgeries and compare prescribing trends on the same axis
      - `plot_trends_for_two_surgeries_id_1 [default = 'P84071']` ##ID for plot_trends_for_two_surgeries
      - `plot_trends_for_two_surgeries_id_2 [default = 'P84049']` ##ID for plot_trends_for_two_surgeries
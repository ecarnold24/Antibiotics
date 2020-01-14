# OpenPrescribingToolkit 


##  Background to GP prescribing data compiled by NHS England

Open Prescribing (https://openprescribing.net/) is an online resource collated by the EBM DataLab at the University of Oxford. Open Prescribing collates the annoymised data on GP drugs prescriptions published monthly by NHS England and makes it more accessible to researchers and the general public. 

##  The OpenPrescribingToolkit
This tool was developed by STP students for a programming module at the University of Manchester. This tool can be used to perform the following analysis of Open Prescribing data:<br>
1. Identification of outliers:<br>
    *  Database entries (i.e. rows) with zero prescriptions will be identified and removed from the database as these are artifacts. A surgery with zero prescriptions, is likely to have no (or super healthy!) patients. <br>
    *  Outliers are classified using the interquartile range (IQR) rule i.e.<br>
            IQR = Q<sub>3</sub> - Q<sub>1</sub> <br>
            UL = Q<sub>3</sub> + IQR <br>
            LL = Q<sub>1</sub>  - IQR  <br>
        
        where,<br>
            UL = Upper Limit  <br>
            LL = Lower Limit <br>
        Outliers are values greater than the UL or lower than the LL<br>
        The OpenPrescribingToolkit identifies outliers as GP surgeries with prescription values greater than the UL or lower than the LL <br>
    
2. Plotting trends of GP practices with extreemly high or low prescription values (i.e. outliers identified in step 1)

List of GP practises with outliers = file name
plot individual practices to see if trends correspond with e.g. a new doctor joining the practise...

## User Instructions for the OpenPrescribingToolkit

These can be found here ...

## Tutorial/test data for the OpenPrescribingToolkit

These can be found here ...
testing documentation notes from Ian:
1. a prescritptive list of instructions e.g. receipe
2. if you do x, y and z; the result will be p,q r...
3. If you do not get result p, q, r do a,b,c

## TODO list
outlier graphs
use variables and define these at top of toolkit
rename files and organise folder
write testing document
write user instructions 
edit readme text above.


# In order to run the script successfully, please download the run_pipeline_python2.7.py and the measures.csv file.
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

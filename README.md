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

### Prerequisites


## Tutorial/test data for the OpenPrescribingToolkit

These can be found here ...
testing documentation notes from Ian:
1. a prescritptive list of instructions e.g. receipe

Add to output examples file. Use output with a markdown to give a solid tutorial /test document

2. if you do x, y and z; the result will be p,q r...
3. If you do not get result p, q, r do a,b,c

## TODO list
outlier graphs
use variables and define these at top of toolkit - done
rename files and organise folder -
write testing document
write user instructions 
edit readme text above.




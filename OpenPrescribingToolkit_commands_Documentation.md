# Documentation for OpenPrescribingToolkit commands

This document provides a list of the available functions within the OpenPrescribingToolkit and a brief description of their function

- **import_OP_data(filename)** <br>
    
    This function imports an csv file (ideally downloaded from the Open Prescribing website) into a dataframe 
    for analysis in Python. To use this function replace 'filename' with the name of the file you wish to import.<br>

- **remove_OP_artifacts(dataframe)** <br>
    
    This function identifies and removes entries within the OpenPrescribing dataset which have zero prescriptions 
    recorded. Database entries (rows) with 0.0 prescriptions need to be removed from the database as these are 
    artifacts and will skew outlier calculations; an active GP surgery is very unlikely to issue zero prescriptions! 
    If any GP practices are identified. The script will return the number of artifacts detected (if any), and state 
    how the datset has been analysed e.g. if the artifacts have been removed.To use this function type the command as given above. There is no need to specify the 'dataframe' as this variable has been defined by the *import_OP_data(filename)* function.<br>

- **remove_OP_IQRoutliers(dataframe)** <br>  
    This script identifies outliers within the dataset, based on the interquartile range (IQR) rule i.e.<br>
            - IQR = Q<sub>3</sub> - Q<sub>1</sub> <br>
            - UL = Q<sub>3</sub> + IQR <br>
            - LL = Q<sub>1</sub>  - IQR  <br>
        
        *where,<br>
            UL = Upper Limit  <br>
            LL = Lower Limit <br>
        Outliers are classified as values greater than the UL or lower than the LL*<br>
        
     The OpenPrescribingToolkit identifies outliers as GP surgeries with prescription values greater than the UL or 
     lower than the LL. This command prints the lower and upper limit values for outliers alongside the IQR. 
     A boxplot for the dataset is produced and a unique list of GP surgeries with prescription outliers are listed. 
     Any GP practices identified as having prescription outliers can be plotted using the 
     *Plot_trends_pick_surgeries(data, name)* function to view one GP surgery with outliers or the 
     *Plot_trends_two_surgeries_by_IDs(data, name1, name2)* function to compare two GP surgeries.<br>
    
            
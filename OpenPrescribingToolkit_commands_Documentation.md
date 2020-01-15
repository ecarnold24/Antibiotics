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
    how the datset has been analysed e.g. if the artifacts have been removed.To use this function type the command as given above. There is no need to specify the 'dataframe' as this variable has been defined by the <i>import_OP_data(filename)<i> function.<br>

- **remove_OP_artifacts(dataframe)** <br>  
    
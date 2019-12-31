'''Import the following packages for functionality
Matplotlib is used to create the graphs in this script
Pandas is used to read in the data
Random is used to generate random data
OS (operating system) is used to exit the script if there is an error'''

import matplotlib.pyplot as plt ##For plotting functionality
import pandas as pd ##For reading in the data and storing as a dataframe
import random ##For randomly generating a value, or picking a random value from a list
import os ##For interfacing with the operating system. Only used to force exit in this script

'''Specify the data file and read it in'''
path_to_data = 'measures.csv' ##Measures contains the data for Manchester CCG.
data = pd.read_csv(path_to_data, sep = ',') ##Read in file path as data, and tell the script the data is comma separated

'''Define the parameters to run in this code.
True = run that test
False = do not run that test'''
run_test_module = False ##Generate a dataframe and test script functionality.
## NOTE: If run_test_module is True, then all values below will be set as False.
## Recommend running test module on first pass, and if all is fine, then set value to False.

run_identify_outliers = True ##This will identify outliers in the data file and print a boxplot
print_outliers_to_console = True ##This will print the identified outliers to the console.
## NOTE: print_outliers_to_console requires run_identify_outliers to be equal to True.

data_import_test = True ##Sanity checks the input file. Checks if the required number of columns are present and that the data can be sliced, so that it is compatible with the rest of the script.
plot_trends_for_all_surgeries = True ##For each unique surgery in the data file, plot prescribing trends, all on the same axis.
plot_trends_combining_all_surgeries = True ##Combines prescribing data for all surgeries in data file and plots as a single line.
plot_trends_for_one_surgery = True ##Pick one surgery in input and plot prescribing trends for that one surgery
plot_trends_for_one_surgery_id = 'P84071' ##ID for plot_trends_for_one_surgery
plot_trends_for_two_surgeries = True ##Pick two surgeries and compare prescribing trends on the same axis
plot_trends_for_two_surgeries_id_1 = 'P84071' ##ID for plot_trends_for_two_surgeries
plot_trends_for_two_surgeries_id_2 = 'P84049' ##ID for plot_trends_for_two_surgeries


'''The script functions are defined here'''
def identify_outliers(data_file): ##This will identify outliers in the data file and print a boxplot
    print "\nIdentifying outliers...\n"
    sorted_data = data_file.sort_values("numerator") ##Take input data file and sort by prescribing data, from lowest to highest
    num_no_prescriptions = len(sorted_data[sorted_data['numerator'] == 0.0]) ##Number of timepoints where a surgery prescribed no antibiotics

    if num_no_prescriptions > 0: ##If the number is greater than 0, run this if loop
        print "This dataset contains %s entries with 0 prescriptions. These entries will be removed from the dataset." % num_no_prescriptions ##Print to console the number of timepoints where a surgery prescribed no antibiotics
        filtered_data = sorted_data[sorted_data['numerator'] > 0.0] ##Filter data file to remove those timepoints where a surgery prescribed 0 antibiotics.
    else: ##If number is not greater than 0, run this if loop
        print "This dataset contains 0 entries with 0 prescriptions. Continuing..." ##Print information to console.
        filtered_data = sorted_data ##The filtered data is therefore equal to sorted data. The rest of the function requires a "filtered_data" variable.

    filtered_data_min = min(filtered_data["numerator"]) ##Find the fewest prescriptions at any timepoint for any surgery
    print "The fewest prescriptions in the dataset is: %s" % filtered_data_min ##Print fewest prescriptions number to console
    filtered_data_max = max(filtered_data["numerator"]) ##Find the maximum prescriptions at any timepoint for any surgery
    print "The most prescriptions in the dataset is: %s" % filtered_data_max ##Print maximum prescriptions for any surgery


    '''In order to identify outliers, this function defines an outlier as either:
    Lower than 25th percentile, minus 1.5 x interquartile range
    Greater than 75th percentile, plus 1.5 x interquartile range'''
    q1 = filtered_data["numerator"].quantile(0.25) ##Identify number of prescriptions equal to the lower quartile (value at 25th percentile).
    q3 = filtered_data["numerator"].quantile(0.75) ##Identify number of prescriptions equal to the upper quartile (value at 75th percentile).
    iqr = q3-q1 ##Interquartile range is simple upper quartile minus the lower quartile.
    print "The interquartile range is: %s" % iqr ##Print the interquartile range to the console

    Low_outlier_value = q1 - (1.5*iqr) ##Determine the value below which prescribing data will be called as outliers
    identify_outliers.High_outlier_value = q3 + (1.5*iqr) ##Detemine the value above which the prescribing data will be called as outliers.
    # This value is assigned to a value that can be called outside of the function, to be added to trends graphs in later functions.

    outliers = filtered_data[(filtered_data["numerator"] < Low_outlier_value) | (filtered_data["numerator"] > identify_outliers.High_outlier_value)] ##Subset the data file to include only outliers
    print "This dataset contains %s outliers, represented as circles in the boxplot below" % outliers.shape[0] ##Print the number of outliers to the console

    save_boxplot = plt.figure()
    plt.boxplot(list(filtered_data["numerator"])) ##The prescribing data is displayed as a boxplot. Circles represent outliers.
    plt.show() ##Show the plot when function is called.
    save_boxplot.savefig("Outlier_BoxPlot.pdf")

    if print_outliers_to_console == True: ##A list of the surgeries with at least one outlier can be displayed on the console
        outlier_gp_list = list(outliers["org_name"].unique()) ##Get a list of surgeries with at least one outlier, from the outliers subset calculated before the boxplot

        print("\nThis is a list of all GP practices where antibiotic prescriptions have been identified as outliers:\n") ##Initiate print to console
        if len(outlier_gp_list) > 0: ##If there is at least one outlier, the following loop will be called.
            for gp in outlier_gp_list: ##For each individual surgery, the following actions will be taken.
                gp_id_table = outliers[outliers["org_name"]==gp] ##Find the name of the individual surgery
                gp_id = gp_id_table.iloc[0]["org_id"] ##Find the ID of the individual surgery (for use with graphing functions later in the script)
                print "%s, %s" % (gp, gp_id) ##Print surgery name and ID to console.
        else: ##However, if there are no outliers, this action will be called:
            print "None." ##Print the word "None"


def data_import(data_file): ##This function sanity checks the input.
    print "\nSanity checking data import..."
    data_slice = data_file.loc[0:3] ##If the data has been imported correctly as a dataframe, it can be sliced.
    if data_slice.shape[0] == 4 and data_slice.shape[1] == 9: ##If the data can be sliced, it should have 4 rows. We check for 9 columns as that is the input format this script works with.
        return True ##If the data has the correct number of headers and rows, return the value True
    else:
        return False ##If the data does not have the correct number of headers and rows, return the value False


def plot_trends_all_surgeries(data_file): ##For each unique surgery in the data file, plot prescribing trends, all on the same axis.
    print "\nPlotting trends for all surgeries... Please note, this takes a while..." ##Tell the user via the console that this graph may take a while to plot. It prevents them closing the console or suspecting an error.
    unique_org_ids = data_file['org_id'].unique()  ##Get a list of all surgeries

    save_trends_all_surgeries = plt.figure() ##Save figure to variable to output as PDF later
    ax = plt.gca()  ##Set the default axis for the graph
    for orgs_id in unique_org_ids:  ##For each surgery in the list of all surgeries, perform the following actions
        new_dataframe = data_file[data_file['org_id'] == str(orgs_id)]  ##Get a new dataframe subset just for the one surgery
        graph_points = new_dataframe[['date', 'numerator']]  ##From the new dataframe generated abive, get the date and prescription number
        graph_points.plot(x='date', y='numerator', ax=ax)  ##Plot date and prescriptions on axis generated before the for loop

    ax.get_legend().remove()  ##Remove legend from graph, as there are too many surgeries to list in the legend.
    ax.set_ylim([0, None]) ##Set the minimum y-axis value to 0, so there is correct context for the graphing figures.
    plt.gcf().autofmt_xdate()  ##Format the x-axis for date data, rather the strings, floats, or integers.
    plt.axhline(identify_outliers.High_outlier_value, lw = 2, ls = '--', color = "red") ##Plot the line, above which, data would be called as an outlier
    plt.show()  ##Show the plot
    save_trends_all_surgeries.savefig("trends_all_surgeries.pdf") ##Save the plot to current working directory
    print "Plotting trends for all surgeries complete!"


def plot_trends_combined_surgeries(data_file): ##This combines the antibiotic prescribing data for all surgeries into a single value, and then plots this as a trend over time
    print "\nCombining data for all surgeries and plotting trends..."
    unique_date_ids = data_file['date'].unique()  ##Get a list of all the reporting dates within the data file
    dates_axis = []  ##Initiate a list for dates
    summed_axis = []  ##Initiate a list to combine all data for that date from all surgeries

    for dates in unique_date_ids: ##For each date in the list of all reporting dates within the data file
        dates_axis.append(dates)  ##Append each date to date_axis list, initiated above this for loop
        new_dataframe = data_file[data_file['date'] == dates]  ##Subset dataframe just the current for-loop date
        summed = new_dataframe['numerator'].sum()  ##Sum the prescribing column for all surgeries for this one date
        summed_axis.append(summed)  ##Append the sum to the list initiated above this for-loop

    new_df = pd.DataFrame({'date_axis': dates_axis, 'summed_axis': summed_axis})  ##Turn lists generated in the for loop into dataframe

    save_trends_combined_surgery = plt.figure()
    ax = plt.gca()
    new_df.plot(x='date_axis', y='summed_axis', ylim = [0, None], ax=ax)  ##Plot the combined data as a single line for each timepoint

    plt.gcf().autofmt_xdate()  ##Format x-axis to take dates, rather than strings, integers, or floats.
    plt.show()  ##Show the plot.
    save_trends_combined_surgery.savefig("trends_combined_surgeries.pdf", format='pdf') ##Save plot as PDF to current working directory
    print "Trends for all surgeries combined complete!"

def plot_trends_pick_surgery(data_file, name): ##Pick one surgery in input and plot prescribing trends for that one surgery. Takes data and ID
    print "\nPlotting trends for specified surgery..."
    if data_file['org_id'].str.endswith(name).any(): ##We only want to plot a graph if the ID provided actually exists.
        save_trends_pick_surgery = plt.figure() ##Save figure to variable to save as PDF later on
        ax = plt.gca()  ##Set the default axis for the graph
        new_dataframe = data_file[data_file['org_id'] == str(name)]  ##Get a new dataframe subset just for the one surgery from the ID provided
        graph_points = new_dataframe[['date', 'numerator']]  ##From the new dataframe, get all the dates and prescription data

        graph_points.plot(x='date', y='numerator', ax=ax)  ##Plot date and prescriptions over time for this one surgery

        ax.legend(loc='upper right', labels=new_dataframe['org_id']) ##Initiate legend, and provide the surgery ID as a label.
        plt.axhline(identify_outliers.High_outlier_value, lw=2, ls='--', color="red") ##Add the line above which the data would be called as an outlier.
        ax.set_ylim([0, None]) ##Set the minimum y-limit to 0, to provide context for the surgery's prescribing data
        plt.gcf().autofmt_xdate()  ##Format the x-axis to take dates, rather than strings, floats, or integers.
        plt.show()  ##Show the plot
        save_trends_pick_surgery.savefig("trends_one_surgery.pdf") ##Save plot to PDF in current working directory
        print "Graph for one surgery complete!"

    else: ##If the surgery ID does not exist in data file, then complete the following actions
        print 'Could not find surgery!' ##Tell the console that the surgery doesn't exist.


def plot_trends_two_surgeries_by_IDs(data_file, name1, name2): ##Pick two surgeries and compare prescribing trends on the same axis
    print "\nPlotting trends for two surgeries..."
    if data_file['org_id'].str.endswith(name1).any() & data_file['org_id'].str.endswith(name2).any(): ##Check that both provided IDs are in the data file, if they are, complete the following actions
        save_trends_two_surgeries = plt.figure() ##Initiate plot to variable to save as PDF later
        ax = plt.gca()  ##Set the default axis for the graph

        for two_id in name1, name2:  ##For each surgery in the provided IDs
            new_dataframe = data_file[data_file['org_id'] == str(two_id)]  ##Get a new dataframe just for one surgery
            graph_points = new_dataframe[['date', 'numerator']]  ##From the new dataframe, get the date and prescription number for each surgery

            graph_points.plot(x='date', y='numerator', ax=ax)  ##Plot date and prescriptions for each surgery

        new_dataframe1 = data_file[data_file['org_id'] == str(name1)]  ##Get a new dataframe subset just for the first surgery
        legend_points1 = new_dataframe1[['org_id', 'org_name']]  ##From the new dataframe, get the ID and surgery name

        new_dataframe2 = data_file[data_file['org_id'] == str(name2)]  ##Get a new dataframe subset just for the second surgery
        legend_points2 = new_dataframe2[['org_id', 'org_name']]  ##From the new dataframe, get the ID and surgery name

        legendname1 = legend_points1.iloc[0]['org_id'] + ', ' + legend_points1.iloc[0]['org_name'] ##Combine the first surgery ID and name into one value to be used in the legend
        legendname2 = legend_points2.iloc[0]['org_id'] + ', ' + legend_points2.iloc[0]['org_name'] ##Combine the second surgery ID and name into one value to be used in the legend
        plt.axhline(identify_outliers.High_outlier_value, lw=2, ls='--', color="red") ##Add the line, above which, the values would be called as outliers
        ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.2), labels=(legendname1, legendname2)) ##Add the legend to the plot
        ax.set_ylim([0, None]) ##Set the minimum y-axis value to 0, to provide context for the data
        plt.gcf().autofmt_xdate()  ##Format the x-axis to take date data, rather than integers, floats, or strings
        plt.show()  ##Show the plot
        save_trends_two_surgeries.savefig("trends_two_surgeries.pdf")
        print "Plotting graph for two surgeries complete!"
    else:
        print('One, or both, of the surgery IDs is incorrect!') ##If one or both surgery IDs don't exist, the graph will not be generated.


def test_module(): ##This test module should be run first and tests all functions above with a script-generated data set.
    data_test = pd.DataFrame(columns=['measure', 'org_type', 'org_id', 'org_name', 'date', 'numerator', 'denominator', 'calc_value', 'percentile']) ##initiate an empty dataframe with the same headers as we expect our input data to include.
    date_test = pd.date_range('1/10/2014', '1/10/2015', freq='M') ##Initiate a dataframe of 12 months of dates
    numerator_count = 0 ##initiate an iterable value for fake prescribing data
    for new_gp in range(0, 10): ##Each fake GP will be given a value from 0-9, and will be actioned in the following loop:
        numerator_count = numerator_count + 100 ##Each GP will have the number of prescriptions equal to the previous GP plus 100, to avoid duplications and enable uniformity.
        for new_date in range(0, len(date_test)): ##This for-loop in a for-loop is saying "For each month for the one GP"
            new_data = {'measure':'Test', ##Provide a Test measure
                        'org_type':'Fake_GP', ##Provide Fake_GP as organisation type
                        'org_id':'P' + str(new_gp), ##The surgery ID shall be from P0 to P9, as per the "new_gp" value in the above for-loop
                        'org_name':'Fake GP number ' + str(new_gp), ##The surgery name is simply "Fake GP number X", where X is 0-9 depending on loop iteration
                        'date':date_test[new_date], ##Append the current date iteration
                        'numerator':numerator_count, ##Append the current numerator iteration (this will be the same for all dates for each GP).
                        'denominator':1, ##This can be any value
                        'calc_value':numerator_count, ##This can be any value
                        'percentile':100} ##This can be any value
            data_test = data_test.append(new_data, ignore_index=True) ##Append all of the above into a fake dataframe, which mimics what we would expect for our input data

    print '\nThere should be Fake GPs with ID P0 - P9. \nPrinting list of Fake GPs... \n' ##To test the dataframe has been created correctly, the Fake GP IDs will be printed to the console for the user to check
    for each_fake_GP in data_test['org_id'].unique(): ##So for each fake GP in the fake dataframe:
        print(each_fake_GP) ##Print the name

    '''We will now test all functions in this script with the fake dataset'''
    print '\nIdentifying outliers, but there shouldn\'t be any...' ##We know there shouldn't be any outliers in the fake dataset
    identify_outliers(data_test) ##Run the identify_outliers function. No outliers should be returned during execution

    print '\nGenerating graph 1... \n\n There should be 10 straight lines, at 100 to 1,000, every 100... \n'
    plot_trends_all_surgeries(data_test) ##Running this script with the fake data should return a graph where the are straight horizontal lines from 100 to 1,000, every 100

    print '\nGenerating graph 2... \n\n There should be 1 straight line, summed to 5,500...\n'
    plot_trends_combined_surgeries(data_test) ##This script should sum all of the prescribing data for all fake GPs at each fake timepoint. Since these values are set by us, we know there should be one straight line at 5,500

    print '\nGenerating graph 3... \n\n There should be 1 straight line, picked randomly. The legend y-axis should match the value below the graph\n'
    '''In order to test the plot_trends_pick_surgery, which plots prescribing data for just one surgery,
    we first will randomly pick one of our fake surgeries randomly. This graph should therefore be different
    for each test run'''
    unique_org_ids = data_test['org_id'].unique() ##Get a list of all fake surgeries
    rand_id = random.choice(unique_org_ids) ##Randomly pick one of the list of fake surgeries

    plot_trends_pick_surgery(data_test, rand_id) ##Run the plot_trends_pick_surgery function for test data, with one randomly picked fake surgery. A graph should be returned

    new_dataframe3 = data_test[data_test['org_id'] == str(rand_id)]  ##Get a new dataframe subset just for the randomly-picked surgery
    legend_points3 = new_dataframe3[['numerator']]  ##From the new dataframe, get the prescription number for the fake surgery

    print '\nThe line should be at y =', legend_points3.iloc[0]['numerator'], '\n\n' ##The user should compare this value with the horizontal line on the graph

    print 'Generating graph 4... \n\n There should be 2 straight lines, picked randomly. The legend y-axis should match the value below the graph'
    '''In order to test the plot_trends_two_surgeries_by_IDs function, two random surgeries will be selected, as above'''
    rand_id2 = random.choice(unique_org_ids) ##From the list of all fake surgeries generated above, pick another one
    newdf4 = data_test[data_test['org_id'] == str(rand_id2)] ##Generate a new dataset just for this randomly picked surgery
    lp4 = newdf4[['numerator']] ## Get expected horizontal line value for this randomly picked surgery

    rand_id3 = random.choice(unique_org_ids) ##From the list of all fake surgeries generated above, pick another one
    newdf5 = data_test[data_test['org_id'] == str(rand_id3)] ##Generate a new dataset just for this randomly picked surgery
    lp5 = newdf5[['numerator']] ##Get expected horizontal line value for this randomly picked surgery

    plot_trends_two_surgeries_by_IDs(data_test, rand_id2, rand_id3) ##Test the function with both randomly picked surgeries. A graph is expected to be output

    print '\n The two lines should be at y=', lp4.iloc[0]['numerator'], ' and y =', lp5.iloc[0]['numerator'] ##The user should compare these two values with the horizontal lines on the returned graph.



'''Now all functions have been defined, we need to execute the code'''

if run_test_module == True: ##In the list of input variables, if this is true, it will run the test module only (essentially setting all other input variables to false).
    print 'Running test module...' ##Tell console that the test module is running.
    test_module() ##Call test module with no input - all input is generated within the function.
    print '\n\n______________________________________________________\nIf all the graphs have printed correctly, and match the values on the command line, then please set run_test_module to False and proceed...\n______________________________________________________'
    ##Tell the console that the test module has finished running, and that they should set the run_test_module to False to run the rest of the code.
else: ##If run_test_module is False or non-existent

    if data_import_test == True and data_import(data) == True: ##If data_import_test is selected by user is true, then run data import function. If the returned value is True, then action:
        print 'Data has been imported successfully.' ##Print that data import has been sanity checked.
    elif data_import_test == True and data_import(data) == False: ##If the user wants to run the import function, but the data_import function returns False, then action:
        data_slice_fail = data.loc[0:3] ##Attempt to slice, as in the data_import function
        print 'Data file not in expected format. Expected 4 rows and 9 columns, observed %s rows and %s columns...\n Quitting process...' % (data_slice_fail.shape[0], data_slice_fail.shape[1]) ##Print the actual number of rows and headers in the slice.
        os._exit(0) ##Quit the script as the user input is wrong.

    if run_identify_outliers == True: ##The user can select to identify outliers or not
        identify_outliers(data) ##If the variable is true, the identify_outliers will be run with the provided data.
    ##No "else" is provided, as we do not want to action anything if the run_identify_outliers value is False.

    if plot_trends_for_all_surgeries == True: ##The user can choose to run plot_trends_all_surgeries function. If True, then action:
        plot_trends_all_surgeries(data) ##Run this function with the user-provided input data.

    if plot_trends_combining_all_surgeries == True: ##The user can choose to run plot_trends_combined_surgeries function. If True, then action:
        plot_trends_combined_surgeries(data) ##Run this function with the user-provided input data.

    if plot_trends_for_one_surgery == True: ##The user can choose to run plot_trends_pick_surgery function. If True, then action:
        plot_trends_pick_surgery(data, plot_trends_for_one_surgery_id) ##Run this function with the user-provided input data and user-provided surgery ID

    if plot_trends_for_two_surgeries == True: ##The user can choose to run plot_trends_all_surgeries function. If True, then action:
        plot_trends_two_surgeries_by_IDs(data, plot_trends_for_two_surgeries_id_1, plot_trends_for_two_surgeries_id_2) ##Run this function with the user-provided input data and user-provided surgery IDs

print '\n\nEnd of script.' ##tell user that this is the end of the script.
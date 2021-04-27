# Create and Configure an Analysis Plot

## Step 1: Import a Summary Ensemble
![Image](./Resources/Pictures/import_ensemble.png) 


Navigate through the "File" drop-down menu and select 'Import->Summary Cases->Import Summary Ensemble' as shown above. 

![Image](./Resources/Pictures/file_location.png) 


A prompt will appear; select the "..." (as illustrated in the above picture) and navigate to the folder which contains the ensemble. It will appear a file-path to the folder you have selected. In our case we are using the Reek ensemble. 

![Image](Resources/Pictures/find_ensemble.png) 


The Reek ensemble we are working with contains 9 realization each having four iterations ranging from iter 0 to iter 3. To import the iter-0 ("base_pred") we add the following syntax to the file path: "\*/iter-1/\*", the astrix symbol ("\*") means that it will match any number of any character. As the above illustration shows, press the "Find" it will search for all the ".SMSPEC" files associated with the "iter-0".

![Image](Resources/Pictures/select_ensemble.png)

Select realization 0 through 9, as illustrated in the above screenshot and click 'ok'. This will open up a new prompt will appear; asking you to name the ensemble. We will call this "iter-1". Then press "OK".

Similarly import another summary ensemble corresponding to "iter-3" and name it "iter-3".

## Step 2: Create a Delta Ensemble 

![Image](Resources/Pictures/rightclick_summarycases.png) 

Select "New Delta Ensemble" from right-click on "Summary Cases" as shown above.

![Image](Resources/Pictures/select_delta_ensemble.png) 

Create a Delta Ensemble as the difference between the two cases (iter-6-iter-0)


## Step 3: Create Analysis Plot

![Image](Resources/Pictures/create_analysis_plot.png) 

In project tree, right click on "Analysis Plot" and select new Analysis Plot as displayed in screenshot above.

![Image](Resources/Pictures/select_vector.png) 

In Property Editor, in group Selected Vectors, click on the button with three dots “…” as illustrated above


![Image](Resources/Pictures/analysis_plot_editor.png)  

Set source to Delta ensemble, select well OP_1-5 and summary Vector WOPT as shown above. Once desired property is selected, click "OK"

![Image](Resources/Pictures/bar_settings.png) 

Change bar setting configuration (Bar Orientation: Horizontal, Select Summary Item in Major Grouping  and sort by abs(Value) as illustrated in the figure above.


![Image](Resources/Pictures/bar_label.png) 
Activate Bar labels and show legends.

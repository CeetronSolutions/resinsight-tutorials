# Preparing Plot Templates
Objective is to store plot setup with customized curve appearance for reuse on different data.


## Step 1: Importing summary cases

Navigate through the "File" drop-down menu and select ´Import->Summary Cases->Import Summary Cases Recursively´

![Image](./Resources/Pictures/import_recursively.png)

![Image](./Resources/Pictures/find_recursively.png)


A prompt will appear; select the "..." (as illustrated in the above picture) and navigate to the folder which contains the ensemble. It will appear a file-path to the folder you have selected. In our case we are using the Reek ensemble.

![Image](Resources/Pictures/filter_summarycases.png)

The Reek ensemble we are working with contains 9 realization each having four iterations ranging from iter 0 to iter 3. To import the iter-0 ("base_pred") we add the following syntax to the file path: "\*/iter-0/\*", the astrix symbol ("\*") means that it will match any number of any character. As the above illustration shows, press the "Find" it will search for all the ".SMSPEC" files associated with the "iter-0".

![Image](Resources/Pictures/select_ensemble.png)

Select realization 0 through 9, as illustrated in the above screenshot. This will open up the plot window.

Open the "Plot Window" by clicking this button on the [Quick Access bar](../graphical-user-interface/graphical-user-interface.md#quick-access-buttons) or pressing the shortcut "ctrl+shift+P"


## Step 2: Create Summary Plot
![Image](Resources/Pictures/select_twocases.png)
Select two summary cases in the project tree as shown above and from right-click menu select "Open Summary Plot Editor" 

As the screen shot above illustrates we now want to select "Well", "OP_5" and the property we are interested in displaying. In our case this will be the Oil Production Total or "WOPT", select in the scrolling window or use the search functionality on top to find it.


## Step 3: Change the curve appearance
![Image](Resources/Pictures/change_title.png)
![Image](Resources/Pictures/change_color.png)
![Image](Resources/Pictures/change_axis.png)
![Image](Resources/Pictures/change_font.png)
Change the curve appearance of thw two curves the way you linke best. For example, rename the title, increase font size of axis labels and legends, changing color of curves are some options to begin with.

## Step 4: Save plot template

![Image](Resources/Pictures/save_template.png)
Once desired curve appearance is achieved, in the plot area, right-click and select "Save as Plot Template". Create a folder inn your user area and store this template in thsi folder using the template name "wopr_two_cases" as illustated above


## Step 5: Apply an existing template
![Image](Resources/Pictures/apply_template.png)
In the project tree , select two other summary cases than the ones used to produce template. From the right-click menu, select " Create Plot from Template" and select the recently created template as illustated above.

![Image](Resources/Pictures/test_template.png)
Visual settings you stored in the template should be applied to the geenrated plot as shown above.


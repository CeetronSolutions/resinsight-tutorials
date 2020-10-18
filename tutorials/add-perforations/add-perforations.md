# Adding perforations to well-paths


## Step 1: Open an existing project

<img src="Resources/Pictures/1_open_project.png" width="500">

First, we open up the existing project. Click "File->Open Project" or press "Ctrl+O" navigate to "Resources/Model/add-perforation.rsp". Another possibility is to redo the tutorial [Making A Well](../making-a-well/making-a-well.md)

## Step 2: Create perforation Interval

<img src="Resources/Pictures/2_create_perforation_interval.png" width="500">

To create a perforation interval, in the [Project Tree](../graphical-user-interface/graphical-user-interface.md#project-tree) right-click "Well-1" and select "Create Completions->Create Perforation Interval"

<img src="Resources/Pictures/3_perforation_0_0.png" width="500">

This will create a new sub-category that will show as "Completions" and "Perforations". It will initiate with the coordinate 0 measured depth (MD) to 0 MD. Select the item "0 - 0".

<img src="Resources/Pictures/4_adjust_interval.png" width="500">

In the [Property Editor](../graphical-user-interface/graphical-user-interface.md#property-editor) there will appear two sliding options. These can be adjust to create an interval in terms of MD. If you are using the provided project "add-perforation.rsp" adjust the Start MD to be equal to 2780.3 and the End MD to be 4730.4. This will then create a perforation interval between these two coordinates. 

<img src="Resources/Pictures/5_well_geometry_and_skin.png" width="500">

These two options control the geometry of the perforations and the "Skin Factor".

<img src="Resources/Pictures/6_start_end_date.png" width="500">

Ïn addition we can adjust the start and end-date by enabling "Custom Start Date" and/or "Custom End Date".

<img src="Resources/Pictures/7_one_interval.png" width="800">

After having changed the interval as suggested above, we observe in the [Reservoir View](../graphical-user-interface/graphical-user-interface.md#reservoir-view) that the
perforated interval is highlighted in a green color.

## Step 3: Create multisegmented perforations

<img src="Resources/Pictures/8_create_another_interval.png" width="500">

We can then add another interval to our existing well.

<img src="Resources/Pictures/9_adjust_lengths.png" width="500">

As performed in [Step 2](#step-2:-create-perforation-interval) adjust both intervals to the values illustrated above by manipulating the Start MD and End MD in the Property Tree.

<img src="Resources/Pictures/10_two_intervals.png" width="800">

The green perforations should now look similar to the above picture. Indicating that you have successfully created multi-segmented perforations.

<img src="Resources/Pictures/11_export_completion_data.png" width="500">

These perforations can now be exported by right-clicking the Perforation option in the Project Tree and selecting the "Export Completion Data for Current Well Path".

## Step 4: Create fishbones completion

<img src="Resources/Pictures/12_create_fishbone.png" width="500">

To add fishbones completion we right-click the Completion option in the Project Tree and select "Create Completions->Create Fishbones".

<img src="Resources/Pictures/13_automatic_scaling.png" width="500">

If you have never created fishbones before, you will be prompted by ResInsight to set the scaling factor to 1 to better visually represent the fishbone structure. In our case we click select "Yes"

<img src="Resources/Pictures/14_fishbone_initial.png" width="800">

We can now observe the initial configuration of the fishbones completions in the Reservoir View.

<img src="Resources/Pictures/15_adjust_location_of_fishbone.png" width="500">

In the Property Editor new options have been made available. The first sub-category named "Location" enables you to adjust the positioning of the fishbone completions.

<img src="Resources/Pictures/16_adjust_configuration.png" width="500">

The second sub-category is the "Lateral Configuration", here you can adjust the layout of the fishbones. At what angles, how dense, and orientation the laterals should leave the main trajectory. Adjust these settings and observe the effects in the Reservoir View.

<img src="Resources/Pictures/17_export_fishbone.png" width="500">

After having tested different combinations, you can export the current completion data by right-clicking the "Fishbones" option and navigating to "Export Completions->Export Completion Data for Current Well Path".

## Step 5: Create Fracture

<img src="Resources/Pictures/18_create_fracture.png" width="500">

We can now add a Fracture to the trajectory. By again right-clicking the Completions and navigating to "Create Completions->Create Fracture".

<img src="Resources/Pictures/19_adjust_location_fracture.png" width="500">

The Fracture will be initialised at 0 MD. In the Property Editor adjust the slider such that a blue circle enters the Reservoir View. (If the "add-perforation.rsp" is the project you can se the MD to be equal to 4305.53)

<img src="Resources/Pictures/20_show_fracture_perpendicular.png" width="800">

In the Reservoir View, the fracture should look similar to the picture above.

<img src="Resources/Pictures/21_edit_fracture_template.png" width="500">

All fractures are created from a template, this template can be edited by clicking the "Edit" option in the Property Editor.

<img src="Resources/Pictures/22_adjust_geometry.png" width="500">

A new menu will appear, here you can adjust different parameters of the fracture including the permeability. In this tutorial we will only adjust the direction of the fracture. Feel free
to adjust any setting here and observe the effects in the Reservoir View.

<img src="Resources/Pictures/23_change_fracture_direction.png" width="500">

By selecting the "Fracture Orientation" a drop-down menu will appear, select the "Along Well Path" option.

<img src="Resources/Pictures/24_show_fracture_along.png" width="800">

In the Reservoir View the fracture should now look similar to this, depending on how much you altered the configuration in previous steps.

<img src="Resources/Pictures/25_export_fracture.png" width="500">

The fracture can now be exported by right-clicking the "Fractures" option in the Project Tree and navigating to "Export Completions->Export Completion Data for Current Well Path"

## Step 6: Export all completion data

<img src="Resources/Pictures/26_export_all.png" width="500">

All completion data for this well can be exported by right-clicking the Completions option in the Project Tree and navigating to "Export Completions->Export Completion Data for Current Well".



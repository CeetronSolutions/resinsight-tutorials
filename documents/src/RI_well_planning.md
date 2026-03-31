---
title: "Well Planning"
author: "ResInsight Team"
date: "2026"
---


# Introduction

Well Planning can be used to identify and evaluate new well targets.

# Configure OPM Flow

ResInsight is able to start a simulation using the OPM Flow simulator. The path to flow must be specified in Preferences, e.g. `/usr/bin/flow`

## Windows and WSL

When using Windows and WSL, the distribution must be selected in Preferences. Specify the path to the simulator using the full path on the file system of the Linux distribution, e.g. `/usr/bin/flow`

# Use Job to Run Simulation

1. Open Scripts/Jobs window
1. Right-click on Jobs, and select "New OPM Flow Simulation"
1. Select the `norne-atw2013/NORNE_ATW2013.DATA` file and select output folder
1. Run the simulation, and the simulation grid will automatically open in **ResInsight**

# Contour Maps

Contour maps can be used to identify the distribution of hydrocarbons in the reservoir. These maps can be used to create polygons.

1. In the Project Tree, right-click the view and select **New Contour Map from 3D View**
1. A contour map is created, and select the last time step
1. Select **Map Projection**, and set **Result Aggregation** to **Oil Column**
1. Enable **Value Filter**, select **Above**, and set the threshold value to 11
1. In the contour map view, right-click and select **Create Polygon From Contour Map**



---
title: "Well Planning"
author: "ResInsight Team"
date: "2026"
---

<!--
  Source file for RI_intro2025.pdf
  Images: reference paths relative to this file, e.g. ../../tutorials/grid-visualization/Resources/Pictures/foo.png
  To combine tutorials, paste or inline them below (pandoc does not support file includes natively
  without a filter, so copy content here or use a pre-processing step).
-->

# Introduction

Well Planning can be used to identify and evaluate new well targets.

# Configure OPM Flow

ResInsight is able to start a simulation using the OPM Flow simulator. The path to flow must be specified in Preferences, e.g. \texttt{/usr/bin/flow}

## Windows and WSL

When using Windows and WSL, the distribution must be selected in Preferences. Specify the path to the simulator using the full path on the file system of the Linux distribution, e.g. \texttt{/usr/bin/flow}

# Use Job to Run Simulation

\begin{enumerate}
\item Open Scripts/Jobs window
\item Right-click on Jobs, and select "New OPM Flow Simulation"
\item Select the \texttt{norne-atw2013/NORNE\_ATW2013.DATA} file and select output folder
\item Run the simulation, and the simulation grid will automatically open in \textbf{ResInsight}
\end{enumerate}

# Contour Maps

Contour maps can be used to identify the distribution of hydrocarbons in the reservoir. These maps can be used to create polygons.

\begin{enumerate}
\item In the Project Tree, right-click the view and select \textbf{New Contour Map from 3D View}
\item A contour map is created, and select the last time step
\item Select \textbf{Map Projection}, and set \textbf{Result Aggregation} to \textbf{Oil Column}
\item Enable \textbf{Value Filter}, select \textbf{Above}, and set the threshold value to 11
\item In the contour map view, right-click and select \textbf{Create Polygon From Contour Map}
\end{enumerate}



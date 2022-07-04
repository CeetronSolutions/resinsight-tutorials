# Ensemble Plotting

## Importing an Ensemble

Import an ensemble as described in [this tutorial](../summary-ensemble/summary-ensemble.md)

## Default plots

In preferences, the default plot can be specified. This can either be one or more summary vector or one or more templates.

![Image](Resources/Pictures/preferences-default-curves.png) ![Image](Resources/Pictures/preferences-default-templates.png)

## History Vector Appearance

History vectors can optionally be appended when a summary vector is added to a plot. Default curve style and curve color can also be defined.

![Image](Resources/Pictures/preferences-history-vectors.png)

## Use Phase to define Curve Color

From preferences, it is also possible to activate curve colors by phase. This will use a default curve color for oil(green), red(gas) and water(blue). The curve color can be activated for both sigle curve and ensemble curve display.

## Creating an Ensemble Plot for Well OP_1

Make sure preferences is set to color curve by phase, and append history vector during create or append operations.


Type "WOPR" in the search field in **Data Sources**

![Image](Resources/Pictures/data-source-filter-wopr.png)


Select "New Summary Plot" from the right-click menu of **WOPR**

![Image](Resources/Pictures/data-source-new-summary-plot.png)


A plot with both WOPR and WOPRH is created. Note that the default curve color is green, and the default curve style for the history vector is set according to preferences.

![Image](Resources/Pictures/ensemble-wopr-woprh.png)

Individual curves can be highlighted when clicking on curves. Activate the right-click menu on a curve to show the curve as a single curve in a new plot.

![Image](Resources/Pictures/new-plot-from-curve.png)

Investigate other realizations using the source stepping toolbar.

![Image](Resources/Pictures/single-curve-source-stepping.png)

Drag and drop other realizations into the plot to compare different curves.

![Image](Resources/Pictures/drag-drop-realizations.png)


## Documentation References
[Summary Plots](https://resinsight.org/plot-window/summaryplots/)

[Ensemble Plots](https://resinsight.org/plot-window/ensembleplotting/)

[Preferences](https://resinsight.org/misc/preferences/#plotting)


---
title: "Ensemble Well Log"
author: "ResInsight Team"
date: "2026"
---


# Ensemble Well Log Guide

## Overview

Ensemble Well Log extracts grid properties along a well path for every realization in a grid ensemble, and plots the results with ensemble statistics. This is used to study how structural and property uncertainty affects a planned or existing well. This guide uses the Drogon ensemble with varying grid geometry.

---

# Getting Started

## Model Data

The ensemble is located in `model-data/drogon-varying-grid-geometry`. It contains 21 realizations organized in the FMU folder structure:

```
realization-0/iter-0/eclipse/model/DROGON-0.EGRID
realization-1/iter-0/eclipse/model/DROGON-1.EGRID
...
realization-20/iter-0/eclipse/model/DROGON-20.EGRID
```

The grid geometry differs between realizations, so a given well path crosses the layers at different depths in each realization.

Two deviated well paths crossing all three zones (Valysar, Therys and Volon) are available in `wellpaths`:

| Well | File | Location |
|---|---|---|
| A4 | `wellpaths/A4.dev` | Eastern part of the field, heading north-east |
| B | `wellpaths/B.dev` | Southern part of the field, about 1.6 km south of A4, heading east-south-east |

| Zone | K-layers |
|---|---:|
| Valysar | 1–10 |
| Therys | 11–26 |
| Volon | 27–31 |

---

# Extraction Workflow

## Step 1: Import the Well Path

1. Select **File > Import > Well Data > Import Well Paths from File**
2. Select `A4.dev` and `B.dev` in `model-data/drogon-varying-grid-geometry/wellpaths`

The well paths are added to **Wells** in the **Project Tree**. The steps below use **A4**. Repeat Steps 2–5 for **B** to compare the uncertainty at the two locations.

## Step 2: Create Ensemble Well Log

1. In the **Project Tree**, right-click the well path **A4** and select **Create Ensemble Well Log...**
2. In the **Choose Eclipse Cases** dialog:
   - Click **...** next to **Path pattern** and select `model-data/drogon-varying-grid-geometry`. The pattern ends with `*`, which searches all subfolders
   - Set **File type** to **EGRID**
   - Click **Search** and verify that 21 grid files are listed
3. Click **OK**

The first grid is loaded to populate the list of available properties.

## Step 3: Select Well and Properties

The **Create Ensemble Well Log** dialog has two tabs.

**Well** tab:

| Field | Value |
|---|---|
| Well Path Source | From Project Wells |
| Well Path | A4 |
| Create Ensemble Well Logs From Exported Files | Checked |

**Properties** tab:

1. Select the properties to extract, e.g. **PORO**, **PERMX** and **PRESSURE**
2. Also select **INDEX_K**. This is required for depth equalization (see Step 5)
3. Set **Time Step** for dynamic properties like **PRESSURE**

Click **OK**. ResInsight loads each realization in turn, extracts the selected properties along the well path, and closes the grid again.

### Exported Files

The extracted values for each realization are written to a LAS file in a `lasexport` folder next to the grid file:

```
realization-0/iter-0/eclipse/model/lasexport/
```

The LAS files are grouped into an ensemble using the FMU folder structure, giving one ensemble named `iter-0`.

---

# Plot Analysis

## Step 4: Review the Ensemble Well Log Plot

A **Well Log Plot** is created in the **Plot Window**, with one track for each selected property. Each track contains an **Ensemble Curve Set** showing one curve per realization, together with P10, P90 and Mean statistics curves.

Select an **Ensemble Curve Set** to configure it in the **Property Editor**:

- **Colors**: Single color, or **Color by Ensemble Curve Set** (see Step 6)
- **Statistics**: Toggle **Show Statistics Curves**, **Show Ensemble Curves** and the individual P10, P50, P90 and Mean curves
- **Curve Appearance**: Line style, thickness and symbols

## Step 5: Apply Depth Equalization

When the grid geometry varies, the same layer is found at different measured depths in each realization. Statistics computed at a fixed depth then mix values from different layers.

1. Select the **Ensemble Curve Set** in the **Project Tree**
2. Set **Depth Equalization** to **By K-Layer**

The curves are now aligned on layer tops and bottoms before statistics are computed. **Depth Equalization** is only editable when **INDEX_K** is present in the LAS files.

**Note:** Depth equalization requires the well to cross the K-layers in the same order in all realizations. Where the layer crossings differ, the equalized curves become discontinuous and the statistics are not meaningful.

Compare the statistics curves with **Depth Equalization** set to **None** and **By K-Layer**.

## Step 6: Color by Summary Ensemble (Optional)

The well log curves can be colored and filtered using an ensemble curve set from a summary plot.

1. Select **File > Import > Import Grid and Summary Ensemble**, select `model-data/drogon-varying-grid-geometry`, check **Create Summary Ensemble** only and import
2. Create a summary plot with an **Ensemble Curve Set**, e.g. **FOPT**, and set **Coloring Mode** to **By Ensemble Parameter**
3. Select the **Ensemble Curve Set** in the well log plot:
   - Set **Filter by Ensemble Curve Set** to the summary ensemble curve set
   - Set **Coloring Mode** to **Color by Ensemble Curve Set**

The well log curves now share the colors of the summary curves. When a filter is applied to the summary ensemble curve set, only the matching realizations are shown in the well log plot. Check **Based on Filtered Cases** to compute statistics from the filtered realizations only.

---

# Python Scripting

The extraction can also be scripted with `rips`. See `PythonExamples/generate_ensemble_of_well_logs.py` for an example that loads each realization, creates extraction curves and exports LAS files.

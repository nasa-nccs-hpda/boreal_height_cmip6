
# Notebooks Directory

## Description

- 0_Boreal_height_cmip_extent 
 -- Preparation for Prediction of Boreal Height in North America with CMIP6 bioclimatic variables, soil, permfrost
- 1_Grid_ATL08 
 -- Aggregate ICESat-2 ATL08 20m point observations into CMIP6 bioclimatic grids at ~1km resoltuion
- 2_Train_RF_Model 
 -- Uses 1-km gridded ATL08 Boreal Height data as dependent variable and climatologocial variables, permafrost and soil variables as predictors
- 3_Prediction
 -- Applies trained model to CMIP6 SSPs to predict height for 4 SSPs acorss 4 time intervals, then takes the per-pixel median of each of those 16 scnarios to create maps
- 4_Landscapes
 -- Analyzes median borel height by hydrobasin and Gradient class
- 5_Current_Distros_Test_Compare
 -- Looks at distributions of reserved test set of ATL gridded obeservations, precidected current observations, and all ATL08 point observations
- 6_Build_stack_landscape_tcc_smry
 -- Comiles recent tree canopy height rends 
- 7_Recent_vs_Predicted_Graphs
 -- Compares recent (1984-2020) NA Boreal Tree canopy height trend


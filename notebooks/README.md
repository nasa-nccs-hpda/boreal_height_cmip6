
# Notebooks Directory

## Description

- 0_Boreal_height_cmip_extent 
 -- Preparation for Prediction of Boreal Height in North America with CMIP6 bioclimatic variables, soil, permfrost
- 1_Grid_ATL08 
 -- Aggregate ICESat-2 ATL08 20m point observations into CMIP6 bioclimatic grids at ~1km resoltuion
- 2_Train_RF_Model 
 -- Compiles climatologocial variables, permafrost and soil variables as predictors and trains model of 1-km gridded ATL08 Boreal Height data as dependent variable 
- 3_Prediction
 -- Applies trained model to CMIP6 SSPs to predict height for 4 SSPs across 4 time intervals, then takes the per-pixel median of each of those 16 scenarios to create maps
- 4_Build_stack_landscape_tcc_smry
 -- Compiles recent tree canopy height trends 
- 5_Landscapes
 -- Analyzes median boreal height by hydrobasin and forest scructure class
- 6_Distribution_Compare
 -- Compares distributions of reserved test set of ATL gridded obeservations, precidected current observations, and all ATL08 point observations by forest structure class
- 7_Recent_vs_Predicted_Graphs
 -- Compares recent (1984-2020) NA Boreal Tree canopy height trend with predicted future trends


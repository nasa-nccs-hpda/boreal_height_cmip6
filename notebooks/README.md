
# Notebooks Directory

## Description

- 0_Boreal_height_cmip_extent 
 -- Preparation for Prediction of Boreal Height in North America with CMIP6 bioclimatic variables, soil, permfrost
- 1_Train_RF_Model 
 -- uses 1-km gridded ATL08 Boreal Height data as dependent variable and climatologocial variables, permafrost and soil variables as predictors
- 2_Prediction
 -- Applies trained model to CMIP6 SSPs to predict height for 4 SSPs acorss 4 time intervals, then takes the per-pixel median of each of those 16 scnarios to create maps
- 3_Landscapes
 -- Analyzes median borel height by hydrobasin and Gradient class
- 4_Current_Distros_Test_Compare
 -- Looks at distributions of reserved test set of ATL gridded obeservations, precidected current observations, and all ATL08 point observations
- 5_Build_stack_landscape_tcc_smry
 -- uses 1-km gridded ATL08 Boreal Height data as dependent variable and climatologocial variables, permafrost and soil variables as predictors
- 6_Recent_vs_Predicted_Graphs
 -- Compares recent height trends to predicted height trends   


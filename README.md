[![DOI](https://zenodo.org/badge/695169040.svg)](https://zenodo.org/doi/10.5281/zenodo.10994653)
---
# Persistence of a North American boreal forest shift through 2100: Transitional landscapes feature recent and predicted growth in vegetation structure

<br>[Paul M. Montesano](https://scholar.google.com/citations?hl=en&user=Bx87sEIAAAAJ), Melanie Frost, Jian Li, [Mark Carroll](https://scholar.google.com/citations?user=Hnp-SlQAAAAJ&hl=en&oi=ao), [Christopher S. R. Neigh](https://scholar.google.com/citations?hl=en&user=F_yzYcUAAAAJ), Matthew J. Macander, [Gerald V. Frost](https://scholar.google.com/citations?user=68KbVi0AAAAJ&hl=en), [Joseph O. Sexton](https://scholar.google.com/citations?user=rrwOXjYAAAAJ&hl)

[Innovation Lab, CISTO, NASA GSFC](https://science.gsfc.nasa.gov/cisto/istr/overview) | Maryland, U.S.A

------------------
## Purpose 
- Predict boreal canopy heights through 2100 using ICESat-2 ATL08 observations, current and future (CMIP-6 SSPs) bioclimatic variables, permafrost, & soil variables  
- Examine for landscapes classified according to prevailing forest strucure gradient
- Assess relative to recent multi-decadal landscape-sclae trends in tree canopy cover

## General steps
- Assemble ICESat-2 ATL08 and bioclimatic variables  
- Build random forest regression model of current boreal height based on biocliamtic variables, permafrost, soil variables
- Apply model to future bioclimatic variable from CMIP-6 SSPs to predict structure changes through 2100  
- Summarize recent tree cover trends within landscapes
- Compare landscape summaries of recent tree cover trends results within forest gradient classes with predictions of potential changes in canopy height (https://iopscience.iop.org/article/10.1088/1748-9326/abb2c7/meta)

## Abstract 

High northern latitude changes with Arctic amplification across a latitudinal forest gradient suggest a shift towards an increased presence of trees and shrubs. The persistence of change may depend on the future scenarios of climate and on the current state, and site history, of forest structure. Here, we explore the persistence of a gradient-based shift in the boreal by connecting current forest patterns to recent tree cover trends and future modeled estimates of canopy height through 2100. Results show variation in the predicted potential height changes across the structural gradient from the boreal forest through the taiga-tundra ecotone. Positive potential changes in height are concentrated in transitional forests, where recent positive changes in cover prevail, while potential change in boreal forest is highly variable. Results are consistent across climate scenarios, revealing a persistent biome shift through 2100 in North America concentrated in transitional landscapes regardless of climate scenario.

## Dataset Generation and Training
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.10998324.svg)](https://doi.org/10.5281/zenodo.10998324)

Refer to supplimental materials for thorough description.

<p>
    <img src="https://github.com/nasa-nccs-hpda/boreal_height_cmip6/blob/main/data/atl.png" alt>
</p>
<p>
    <em>The filtered and flagged set of 20 m segment ICESat-2 ATL08 observations of canopy height (h_can_20m) used to grid the model training and testing data for predictions of current and future boreal forest canopy height. </em>
</p>

## Contributors

Paul Montesano, Mel Frost, Jian Li, Zach Williams

## References
TBA

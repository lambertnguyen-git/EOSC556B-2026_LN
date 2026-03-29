# EOSC556B-2026_LN 
## Multichannel Analysis of Surface Waves (MASW) inversion for a synthetic multilayer system 

## Repository Structure
- `260322_MASWSim.ipynb`: main notebook for synthetic MASW forward modeling and inversion
- `project_utils.py`: will contain the functions at code cleanup
- `LNenvironment.yml`: conda environment
- `test_project_util.py`: unit tests for helper functions (in progress)
> The main code is not ready. As such, the functions have not been pulled out into the project_util yet. 

## BACKGROUND 
Multichannel Analysis of Surface Waves (MASW) is a geophysical method used to estimate shear wave velocity (Vs) profiles. Shear wave velocity is a proxy for soil stiffness and is widely used in geotechnical and earthquake engineering for site classification and assessment of seismic hazards such as liquefaction. MASW involves deploying an array of geophones at fixed intervals, generating surface waves (Rayleigh waves), recording wavefields and extracting dispersion curves. The dispersion curves are then inverted to estimate subsurface shear wave velocity profiles. 

While direct measurements of shear wave velocity (e.g., downhole testing) provide higher accuracy, MASW offers a non-invasive and efficient alternative for characterizing larger areas. This efficiency comes at the cost of increased uncertainty due to the inversion process. 

## QUESTION 
How can shear-wave velocity profiles be recovered from Rayleigh wave dispersion using nonlinear inversion, and how sensitive are the solutions to subsurface layering and velocity contrasts?

## APPROACH 
0. Initial Vs, Vp, thickness, and densities were set. 
1. The model will be setup for a 2 layer system with thicknesses 5 m and 10 m. A half step is included. 
2. Simpeg does not have a forward operator for MASW. There are several MASW forward operators that are avaialble for python. Two of hese include disba and pysurf96. disba was used for this initial run This is included within the environment file. 2a. Later, we will try pysurf96 as the forward operator to understand if there are differences with disba. disba: https://github.com/keurfonluu/disba 
3. The model (and disba) is dependent on layer thicknesses, Vs, p-wave velocity (Vp), and density (rho).    
    3a. We will keep the layer thicknesses and number of layers constant for this code swap. We will potentially vary these at a later stage. 
    3b. We are working to solve Vs in this inversion. 
    3c. Vp is typically 2x faster than Vs. We will keep this simplifying assumption to reduce the variables. 
    3d. Density will also be kept constant for this code swap. The change in the density may lead to changes in the dispersion curves but this expected to be a low-sensitivity parameter. This may be adjusted at a later stage, but is a low priority. 
4. We will apply the steepest descent gradient method to converge to the solution. Newton's method may be checked prior to the final presentation.

## USAGE 
1. Clone the repository: 
Terminal: git clone https://github.com/your-username/EOSC556B-2026_LN.git Terminal: cd EOSC556B-2026_LN 
2. Create and activate the environment: 
Terminal: conda env create -f LNenvironment.yml 
Terminal: conda activate eosc-556B
> WINDOWS USERS: you may have to adjust the environment file from python-mumps to -pydiso
3. Run the main notebook: Open: 260322_MASWSim.ipynb 
Run all cells from top to bottom 
4. Expected output: 
Synthetic dispersion curve with noise 
> This project is in progress so these plots may not be ready:
Inverted Vs curves 
Observed vs Predicted Dispersion Curves 
Convergence Figure (Objective function) 
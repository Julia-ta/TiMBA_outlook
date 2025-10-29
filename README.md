![TiMBA Logo](https://github.com/TI-Forest-Sector-Modelling/TiMBA/blob/main/timba_logo_v3.png?raw=true)  

-----------------

# TiMBA - Timber market Model for policy-Based Analysis

[![CI - Test](https://img.shields.io/github/actions/workflow/status/TI-Forest-Sector-Modelling/TiMBA/actions.yml?label=CI%20-%20Test)](https://github.com/TI-Forest-Sector-Modelling/TiMBA/actions/workflows/actions.yml)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=TI-Forest-Sector-Modelling_TiMBA&metric=coverage)](https://sonarcloud.io/summary/new_code?id=TI-Forest-Sector-Modelling_TiMBA)
![GitHub Release](https://img.shields.io/github/v/release/TI-Forest-Sector-Modelling/TiMBA)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.13842492.svg)](https://doi.org/10.5281/zenodo.13842492)
[![License](https://img.shields.io/github/license/TI-Forest-Sector-Modelling/TiMBA)](https://github.com/TI-Forest-Sector-Modelling/TiMBA/blob/main/COPYING)

-----------------

<!-- TOC -->

- [TiMBA - Timber market Model for policy-Based Analysis](#timba---timber-market-model-for-policy-based-analysis)
  - [Cite TiMBA](#cite-timba)
  - [Install TiMBA](#install-timba)
    - [Double check installation and test suite](#double-check-installation-and-test-suite)
  - [Use TiMBA](#use-timba)
    - [Model settings](#model-settings)
      - [Settings as parameters](#settings-as-parameters)
      - [Advanced settings](#advanced-settings)
  - [TiMBA extended model description](#timba-extended-model-description)
  - [Roadmap and project status](#roadmap-and-project-status)
  - [Contributing to the project](#contributing-to-the-project)
  - [Authors](#authors)
  - [Contribution statement](#contribution-statement)
  - [License and copyright note](#license-and-copyright-note)
  - [Acknowledgements](#acknowledgements)
  - [References](#references)

<!-- /TOC -->

**TiMBA** is a partial economic equilibrium model for the global forest products market. The model endogenously simulates 
production, consumption and trade of wood and wood-based products in 180 countries. TiMBA recursively computes the market 
equilibrium for each country and product in a given period by maximizing the social surplus in the global forest sector. 
In the equilibrium processes, product supply, demand and price are balanced for each simulation period. 

## Cite TiMBA

We are happy that you use TiMBA for your research. When publishing your work in articles, working paper, presentations 
or elsewhere, please cite the model as 

[TI-FSM, Morland, C., Schier, F., Tandetzki, J., & Honkomp, T. (2025). TiMBA (Timber market Model for policy-Based Analysis) (v1.0.3). Zenodo. https://doi.org/10.5281/zenodo.15182340](CITATION.cff)

The authors' collective is named Thünen Institute Forest Sector Modelling (TI-FSM). The individual authors are listed as 
Co-authors in alphabetical order. 
## Install TiMBA

The package is developed and tested with Python 3.9 on Windows. TiMBA is compatible with all Python versions up to 3.12.6
with Windows and Ubuntu OS. The functionality with Python versions and different OS is continuously tested using GitHub
Actions Before proceeding, please ensure that Python is installed on your system. It can be downloaded and installed
from [Python.org](https://www.python.org/downloads/release/python-3126/).

1. Clone the repository
Begin by cloning the repository to your local machine using the following command: 
    >git clone https://github.com/TI-Forest-Sector-Modelling/TiMBA.git
   > 
2. Switch to the TiMBA directory  
Navigate into the TiMBA project folder on your local machine.
   >cd TiMBA
   >
3. Create a virtual environment  
It is recommended to set up a virtual environment for TiMBA to manage dependencies. The package is tested for 
   Python versions up to 3.12.6. With a newer Python version, we can not guarantee the full functionality of the package.
   Select the correct Python interpreter.   
   Show installed versions: 
   >py -0  
   >
   - If you have installed multiple versions of Python, activate the correct version using the py-Launcher.
   >py -3.12.6 -m venv venv 
   > 
   - If you are using only a single version of Python on your computer:
   >python -m venv venv
   >
4. Activate the virtual environment  
Enable the virtual environment to isolate TiMBA dependencies. 
   >venv\Scripts\activate
   >
5. Install TiMBA in the editable mode  
   >pip install -e .

    If the following error occurs: "ERROR: File "setup.py" or "setup.cfg" not found."
    you might need to update the pip version you use with: 
    >python.exe -m pip install --upgrade pip

6. The package does not come with predefined data. To download the default input data along with additional information needed to run TiMBA use the command
   >load_timba -FP your_path

7. If the user does not set any folderpath the standard input data will be loaded to the current working directory or the folderpath which is set with:
   >run_timba -FP your_path 
   

### Double check installation and test suite
Double check if installation was successful by running following command from terminal:  
   >timba_run --help

The help provides you information about the basic model settings which changed to adapt model runs to your needs 
(see section [Model settings](#model-settings) for further details).

Test if TiMBA is running by executing the model only for the first period:

  >timba_run -MP=1


The TiMBA model comes with a test suite to ensure its functionality.
Run the test suite to check the functionality of the package and validate the produced results with those provided by the
TI-FSM using the coverage report:

  > coverage run


To reduce the test suite running time, only the first period will be computed and compared. The test suite results will not be saved.
The computed results and provided validation results are compared with a relative tolerance of 5%.  

The coverage report of the TiMBA model can be accessed using:
 > coverage report


## Use TiMBA
The package comes with a built-in CLI to compute the TiMBA for various inputs. While the parametric input can be seen in cmd output calling `timba_run --help` from the terminal, an important part to mention is user input data that need to be imported from a selected folder. You shall not change the following structure within the data folder:
TiMBA is provided with an input file (scenario_input.xlsx), including all input data necessary to run the model. The section [TiMBA extended model description](#timba-extended-model-description-) delivers a detailed description of the included input data.
```bash
.
`- data
  `-- input
    `-- 01_Input_Files
      |-- scenario_input.xlsx #contains all input data to the model. 
    `-- 02_Additional_Information
      |-- additional_information.xlsx 
      |-- worldprice.xlsx
    `-- 03_Serialization
      |-- AddInfoContent.pkl #contains information about the last input data which is processed by the model
      |-- WorldDataContent.pkl #contains information about the last input data which is processed by the model
      |-- WorldPriceContent.pkl #contains information about the last input data which is processed by the model
```

The package will generate a result directory called `output` which is located inside the data folder. The final directory after one run will look something like this:
```bash
.
`- data
  `-- output
      |-- ....log #contains the logged process of the simulation
      |-- DataContainer_....pkl #contains all output information as pkl file
      |-- results....csv #contains main results as csv file
      |-- worldprices....csv #contains world price results as csv file
      |-- forest....csv #contains forest area and stock results as csv file
      |-- manufacture....csv #contains results for manufacturing as csv 
      |-- results_aggregated....csv #contains aggregated results on continent level as csv file

```
**Important output information**  
No output file will ever be overwritten by the application itself. New results-files will be generated in the format `results_D<yyyymmdd>T<hh-mm-ss>.csv` and will be saved to the output folder as well. The logfile itself won't be overwritten as well but also no new file created on additional runs. Log information simply gets appended to the existing logfile. Removing the logfile ahead of executing the model won't result in errors.

### Model settings
Multiple settings are integrated in TiMBA to allow users to interact with the model and adapt the modelling parameters to their research interests.
Following chapter provides a brief overview of the model settings. A detailed description of the settings is provided in the documentation. 

Basic model settings include:
- The base year of simulation (year in which is simulation starts)
- The maximum number of periods for the simulations
- A flag to use product prices as shadow or calculated prices [default: shadow_PP]
- A flag to compute world prices as shadow, constant or average prices [default: shadow_WP]
- A flag to specify the adopted material balance [default: C_specific_MB]
- A flag to activate global material balance balancing all wood flows globally [default: False]
- A computation factor for Transportation Import/Export [default: 1]
- A flag for the use of serialized input pkl files [default: False]
- A flag for the use of dynamized developments in TiMBA [default: True]
- A flag which will cap prices by a maximum [default: False]
- A flag to show verbose optimization output [default: True]
- A flag to show verbose calculation information [default: False]

TiMBA is delivered with a set of default settings, which were tested and validated. The default settings can be changed when executing the package in the CMD or in `default_parameters.py` (changes in settings by the CLI will overwrite parameters in `default_parameters.py`).
  
#### Settings as parameters
The CLI provides to access basic model settings, and their default values. 
Check if CLI command is registered and available on your computer by executing either:

- >timba_run --help

Default settings can be changed in the following way:
- >timba_run -MP=5 -PP="calculated_PP" -WP="shadow_WP"

For this example, TiMBA will simulate 5 periods using calculated prices as product prices and shadow prices as world market prices.

#### Advanced settings
In addition to the settings accessible via the CLI, users can control advanced settings through changes in `Defines.py` 
Advance settings include:
- solver settings (like accuracy, number of iterations and penalties)
- conversion factors

**Caution: The model results were validated for a selection of setting combinations.**   
Some setting combinations might not be coherent and can lead to errors in the simulations or to unreliable results. Those combinations have neither been tested nor validated.   
Note: TiMBA has been tested for periods one to nine. Additionally, if the number of periods is changed, it is necessary to compare and adjust this in the ExogChange sheet in the input file.

## TiMBA extended model description 
TiMBA is a partial economic equilibrium model for the global forest products market. The market equilibrium is subject to 
market clearance and constraints balancing necessary raw materials and produced wood products and limiting the trade (Samuelson 1952). 
The model structure distinguishes between raw, intermediate and end products. TiMBA differentiates three types of roundwood 
(wood fuel, coniferous and non-coniferous industrial roundwood), two additional raw products for paper production (other fibre pulp and waste paper), 
two intermediate products (mechanical and chemical pulp) and eight finished products (coniferous and non-coniferous sawnwoods, veneer sheets and plywood, 
particle board, fibreboard, newsprint, printing and writing paper, and other paper and paperboards). Except for sawnwoods, intermediate and end products are 
produced from a mix of coniferous and non-coniferous industrial roundwood. Scenario simulations with TiMBA are guided by parameters and assumptions shaping 
future developments. In the model framework, wood products are implicitly treated as perfect substitutes, regardless of their origin, as long as they belong 
to the same commodity group. As the optimization of the market equilibrium in a given year does not include an elasticity of substitution, demand is merely 
shifted by changes in income and price (Murray et al. 2004). The supply of roundwood depends on wood prices and forest development which in turn is basically 
determined by the growth dynamics of forest stock, the change in forest area, and harvest volumes. The GDP development indicating national incomes is an important 
driver of change. In TiMBA, demand for wood-based products is positively correlated to income, thus, an increase in income basically leads to an increase in demand. 
Forest area development and thus, timber supply is coupled to GDP per capita developments based on the concept of the environmental Kuznets curve (Panayotou 2004). 
In its basic version, TiMBA uses the assumptions made in the “Middle of the road” scenario described in “The Shared Socioeconomic Pathways” (the so called SSP2 scenario) to 
model future GDP developments and population growth. This scenario describes a world of modest population growth and where social, economic and technological trends continue 
similarly to historical patterns (Riahi et al. 2017). Price and income elasticities of demand are taken from Morland et al. (2018). Further exogenous specifications on technology 
developments (input-output coefficients and manufacturing cost) are estimated based historical developments from 1993-2020. Information on trade inertia are based on 
WTO data as provided in the GFPM (Buongiorno et al. 2015; GFPM version 1-29-2017-World500) while data on WTO Ad-valorem taxes rates are taken from Schier et al. (2025). 
The base year for the scenario simulations with the current version of TiMBA is 2020.
The input data used for simulation with TiMBA needs to be calibrated and provided in a source file prior to model runs. This file is provided together with the model. 
The calibration procedure is described in Buongiorno and Zhu (2015) and altered according to Schier et al. (2018). The input data for calibrating the model are 
obtained from three global databases: The FAO forestry statistics (FAOSTAT), the FAO Forest Global Resources Assessment (FAO 2020) and the World Bank Development 
Indicators (World Bank). The model output comprises information about production, consumption and trade quantities, and prices as well as forest development. The 
model concept bases on the formal description of the Global Forest Products Model (GFPM) (Buongiorno et al. 2015, Buongiorno et al. 2003). 


## Roadmap and project status

The development of TiMBA is ongoing and we are already working on future releases.

- To provide an easy way to visualize and analyse the output of TiMBA we published the interactive analysis toolbox TiMBA:_charts (Morland et al. 2025) that is also available in our [TiMBA repository](https://github.com/TI-Forest-Sector-Modelling/TiMBA). 

Several projects are currently extending different components of TiMBA:
- In the project [iNFORSu](https://www.thuenen.de/en/institutes/forestry/projects-1/modelling-of-the-global-roundwood-supply), we are working on the revision of the module computing forest area and stock development. Forest area development should not longer be only depend on the of GDPpc. Instead, further drivers significantly shaping forest area shall be included into the simulation. This should bring forest development and thus, wood supply closer to reality. 
- In the project [BioSDG](https://www.thuenen.de/en/institutes/forestry/projects-1/the-bioeconomy-and-the-sustainable-development-goals-of-the-united-nations-biosdg) and [CarbonLeak](https://www.thuenen.de/en/cross-institutional-projects/carbon-leak), we extended the model to track and quantify carbon fluxes and stocks related to the forest sectors. Based on IPCC-based methods, carbon stocks in forest biomass and harvested wood products as well as substitution effects are quantified for each simulation period. This extension enables in-depth impact assessments of forest-based climate mitigation policies (e.g., carbon pricing policies and mitigation target-setting policies for the Land Use, Land Use Change and Forestry sector). The high flexibility of TiMBA allows it to cover a large panel of policy designs and conduct sensitivity analyses.   
- In another project, we are implementing bilateral trade flows into the model framework. This step is important to enhance policy impact assessments on e.g., leakage effects.
- Given the fast processing time, we are extending TiMBA to conduct exhaustive uncertainty analysis using Monte Carlo simulations. While these Monte Carlo simulations are currently used in the quantification of carbon stocks, their applications can be deployed to any input data of the model.


Frequently check [TiMBA repository](https://github.com/TI-Forest-Sector-Modelling/TiMBA) for new releases.

## Contributing to the project
We welcome contributions, additions and suggestion to further develop or improve the code and the model. To check, discuss and include them into this project, we would like you to share your ideas with us so that we can agree on the requirements needed for accepting your contribution. 
You can contact us directly via GITHUB by creating issues, or by writing an Email to:

wf-timba@thuenen.de

A scientific documentation will follow and be linked here soon. So far, this README serves as a comprehensive introduction and guidance on how to get started. 



## Authors
TiMBA was developed and written by an authors' collective named Thünen Institute Forest Sector Modelling (TI-FSM). 

The individual authors are listed in alphabetical order 
- [Christian Morland](https://www.thuenen.de/de/fachinstitute/waldwirtschaft/personal/wissenschaftliches-personal/ehemalige-liste/christian-morland-msc) [(ORCID 0000-0001-6600-570X)](https://orcid.org/0000-0001-6600-570X), 
- [Franziska Schier](https://www.thuenen.de/de/fachinstitute/waldwirtschaft/personal/wissenschaftliches-personal/dipl-ing-franziska-schier) [(ORCID 0000-0002-3378-1371)](https://orcid.org/0000-0002-3378-1371), 
- [Julia Tandetzki](https://www.thuenen.de/de/fachinstitute/waldwirtschaft/personal/wissenschaftliches-personal/julia-tandetzki-msc) [(ORCID 0000-0002-0630-9434)](https://orcid.org/0000-0002-0630-9434), and 
- [Tomke Honkomp](https://www.thuenen.de/de/fachinstitute/waldwirtschaft/personal/wissenschaftliches-personal/tomke-honkomp-msc) [(ORCID 0000-0002-6719-0190)](https://orcid.org/0000-0002-6719-0190). 

## Contribution statement
Within the authors' collective TI-FSM, the authors have contributed over years their individual strengths and knowledge to make the model work:

| Author            | Conceptualization and theoretical framework | Methodology | Data Curation and Management | Formal Analysis | Programming | Writing and Documentation | Visualization | Review and Editing | Supervision |
|:------------------|:-------------------------------------------:|:-----------:|:----------------------------:|:---------------:|:-----------:|:-------------------------:|:-------------:|:------------------:|:-----------:|
| Christian Morland |                      X                      |      X      |              X               |        X        |      X      |             X             |       X       |         X          |             |
| Franziska Schier  |                      X                      |      X      |              X               |        X        |             |             X             |               |         X          |      X      |
| Julia Tandetzki   |                      X                      |      X      |              X               |        X        |      X      |             X             |       X       |         X          |             |
| Tomke Honkomp     |                      X                      |      X      |              X               |        X        |      X      |             X             |       X       |         X          |             |

## License and copyright note

Licensed under the GNU AGPL, Version 3.0. 

Copyright ©, 2024, Thuenen Institute, TI-FSM, wf-timba@thuenen.de

 This program is free software: you can redistribute it and/or modify
 it under the terms of the GNU Affero General Public License as
 published by the Free Software Foundation, either version 3 of the
 License, or (at your option) any later version.

 This program is distributed in the hope that it will be useful, but
 WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 Affero General Public License for more details.

 You should have received a copy of the GNU Affero General Public
 License along with this program.  If not, see
 <https://www.gnu.org/licenses/agpl-3.0.txt>.



## Acknowledgements

This work is the result of great joint efforts of the forest products market analysis team at the Thünen Institute of Forestry and others from 2018 to 2024. In the last years, many people made important contributions to this work. Without their support, reflection, and constructive criticism, this undertaking would not have been as successful as it turns out to be now. We would like express our gratitude to all of them. In particular, we would like to thank 
-	Pixida GmbH and especially Tobias Hierlmeier for professional support in revising and restructuring the model architecture and code and being valuable help in programming tasks
-	Thünen Institute Service Centre for Research Data Management and especially Harald von Waldow for providing expertise, consultation, and support during the release process
-	Holger Weimar and Matthias Dieter for the trustful and cooperative working environment, rational support and critical discussion and the opportunity to keep on going
-	Johanna Schliemann for technical support whenever needed
-	The Thünen Institut of Forestry and its Head Matthias Dieter for providing financial resources over the years 
- [makeareadme.com](https://www.makeareadme.com/) for providing the template this README is leaned on.

## References
- Buongiorno, J.; Zhu, S.; Zhang, D.; Turner, J.; Tomberlin, D. The Global Forest Products Model; Academic Press: Cambridge, MA, USA, 2003; ISBN 978-0-12-141362-0
- Buongiorno, J. Global modelling to predict timber production and prices: The GFPM approach. Forestry 2015, 88, 291–303.
- Buongiorno, J.; and Zhu, S. 2015. Technical change in forest sector models: The GFPM approach.  Scand. J. For. Research, 30, 30-48.
- GFPM - Global Forest Product Model is available at https://onedrive.live.com/?authkey=%21AEF7RY7oAPlrDPk&id=93BC28B749A1DFB6%21118&cid=93BC28B749A1DFB6
- FAO. Global Forest Resources Assessment: Terms and Definitions; Forest Resources Assessment Working Paper 188; FAO: Rome, Italia, 2020; Available online: http://www.fao.org/3/I8661EN/i8661en.pdf
- FAO. Global Forest Resources Assessment. 2022. Available online: https://fra-data.fao.org/
- FAOSTAT. Forestry Production and Trade: Datenbank. Available online: https://www.fao.org/faostat/en/#data/FO
- Morland, C.; Schier, F.; Janzen, N.; Weimar, H. Supply and demand functions for global wood markets: Specification and plausibility testing of econometric models within the global forest sector. For. Policy Econ. 2018, 92, 92–105
- Morland, C.; Tandetzki, J.; & Honkomp, T. (2025). TiMBA Charts (v0.2.0). Zenodo. https://doi.org/10.5281/zenodo.15689299
- Murray, B.C.; McCarl, B.A.; Lee, H.-C. Estimating Leakage from Forest Carbon Sequestration Programs. Land Econ. 2004, 80, 109–124
- Panayotou, T. Empirical Tests and Policy Analysis of Environmental Degradation at Different Stages of Economic Development; Working Paper No. 238; International Labour Organization: Geneva, Switzerland, 1993; Available online: http://www.ilo.org/public/libdoc/ilo/1993/93B09_31_engl.pdf 
- Riahi, K.; van Vuuren, D.P.; Kriegler, E.; Edmonds, J.; O’Neill, B.C.; Fujimori, S.; Bauer, N.; Calvin, K.; Dellink, R.; Fricko, O.; et al. The Shared Socioeconomic Pathways and their energy, land use, and greenhouse gas emissions implications: An overview. Glob. Environ. Chang. 2017, 42, 153–168.
- Samuelson, Paul A. Spatial Price Equilibrium and Linear Programming; The American Economic Review, 1952, 42 (3), 283–303; Available online http://www.jstor.org/stable/1810381.
- Schier, F.; Morland, C.; Tandetzki, J.; Honkomp, T. (2025). TI-Forest-Sector-Modelling/TiMBA_Additional_Information: Additional Information for TiMBA Setup (v1.0.1). Zenodo. https://doi.org/10.5281/zenodo.14928911.
- TI-FSM (2025) TiMBA - Timber market Model for policy-Based Analysis: Documentation of model structure, data, and parameters. Braunschweig: Johann Heinrich von Thünen-Institut, 35 p, Thünen Working Paper 263, DOI:10.3220/253-2025-16
- World Bank. World Development Indicators|DataBank. Available online: https://databank.worldbank.org/source/world-development-indicators

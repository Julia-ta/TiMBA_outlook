---
title: 'TiMBA (Timber market Model for policy-Based Analysis)'

tags:
  - Python
  - Forest sector model
  - Partial equilibrium model
  - Optimization
  - Wood markets
authors:
  - name: TI-FSM
    affiliation: 1
  - name: Tomke Honkomp
    orcid: 0000-0002-6719-0190
    equal-contrib: true
    affiliation: 1
  - name: Christian Morland
    orcid: 0000-0001-6600-570X
    equal-contrib: true
    affiliation: 1
  - name: Franziska Schier
    orcid: 0000-0002-3378-1371
    equal-contrib: true
    affiliation: 1
  - name: Julia Tandetzki
    orcid: 0000-0002-0630-9434
    equal-contrib: true
    affiliation: 1
affiliations:
  - name: Thünen Institue of Forestry
    index: 1
    ror: 00mr84n67
date: 26 September 2024
bibliography: paper.bib
---

# Summary
TiMBA is a partial economic equilibrium model to simulate interdependencies and developments of the global forest products market for 180 countries and 16 forest-based products. The model determines the market equilibrium by ensuring market clearance, balancing raw material needs with the manufacturing and demand of wood products while imposing constraints on trade, following principles similar to those of @Samuelson:1952. TiMBA recursively calculates the market equilibrium for each country and product endogenously over a given period by maximizing social surplus in the global forest sector. Scenario simulations are driven by both exogenous and endogenous parameters and assumptions about future market dynamics and policy directives. The model’s output includes detailed information on production, consumption, trade volumes, cost and prices, as well as forest area and stock developments.

![](https://github.com/TI-Forest-Sector-Modelling/TiMBA_Additional_Information/raw/main/images/timba_product_transformation.png)

**Figure 1:** Product structure and processing flows in TiMBA. (*Product represented for visual purposes as aggregates)


# Statement of need

Globally, forests play a critical role by providing a wide range of ecological, economic, and social services, including carbon sequestration, biodiversity conservation, and timber production [@Nabuurs:2023]. However, the increasing pressures of climate change, land-use competition, and demand for different ecosystem services necessitate sound tools for understanding forest dynamics and managing the provision of its diverse resources [@Riviere:2020]. The forest sector is influenced by both market forces (e.g., prices, demand or supply for forest products) and non-market forces (e.g., policies and regulations targeting carbon sequestration and biodiversity conservation). Governmental and international institutions have implemented various and potentially conflicting policies to, e.g., mitigate deforestation [@EuropeanParliamentandCounciloftheEuropeanUnion:2023], promote sustainable management [@MacDicken:2015], and shape trade policies [@Apeti:2023]. The implementation of such policies can have profound effects on the forest sector at the local, regional, and global scale. TiMBA allows for assessing the impacts of forest-related policies and their influence on far-reaching market dynamics.

TiMBA, as a partial economic equilibrium model, helps to analyze the dynamic interactions between supply and demand in forest product markets, trade, forest developments, and policies. Therefore, TiMBA can enhance our understanding of the contribution of forests in an era of significant environmental and socioeconomic challenges [@Riviere:2020]. It enables policymakers and researchers to evaluate policy interventions and future market conditions in the forest sector, which are otherwise difficult to grasp in their complexity [@Schier:2022]. TiMBA can be used to address issues like the interaction between market dynamics and forest resource allocation, the impact of diverse policies and climate change on the forest sector, and the exploration of future forest product markets and global trade trends.

In contrast to existing global forest sector models, like GLOBIOM [@IBFIIASA:2023], GTM [@Sohngen:1999] and EFI-GTM [@Kallio:2004], TiMBA covers 180 countries and 16 commodities in its base version.

This sectoral and spatial coverage comes with key advantages. TiMBA's spatial coverage enables the detailed analysis of forest product markets and trade trends without requiring post-optimization disaggregation. This capability is essential for, e.g., assessing leakage and spill-over effects of unilateral policies or regulations. Deforestation and forest degradation in countries of the southern hemisphere primarily drive global forest area developments [@FAO:2020]. While most global forest sector models aggregate these countries into regions, TiMBA explicitly represents them. This allows users to investigate. e.g., country-specific deforestation dynamics together with climate mitigation and biodiversity conservation efforts.

The sectoral coverage of TiMBA can be flexibly extended to include a lignocellulose-based subsector, empowering users to explore the role of traditional and emerging forest-based products within the future bioeconomy.

Unlike previous forest sector models, TiMBA is written in Python and published open-access. The source code and data are transparently disclosed, enabling researchers to easily modify and extend the model framework to address new research topics. Further, the model relies exclusively on open-access, free-of-charge libraries (including the solver used for the optimization), which allow users to conduct analyses without higher software costs. In that way, TiMBA tries to encourage transparent and community-based forest sector analyses.

# Mathematics

The model concept is based on the formal description of the Global Forest Products Model (GFPM)  [@Buongiorno:2015;@Buongiorno:2003]. The model recursively maximizes the total economic welfare of the forest sector of each represented country, which is defined as the sum of producer and consumer surpluses. The following quadratic problem is maximized using the CVXPY package [@Diamond:2016; @Agrawal:2018] and the OSQP solver [@Stellato:2020]:

$$\max_{Z}=\sum_{i}\sum_{k}\int_{0}^{D_{i,k}}P_{i,k}\left(D_{i,k}\right)dD_{i,k}-\sum_{i}\sum_{k}\int_{0}^{S_{i,k}}P_{i,k}\left(S_{i,k}\right)dS_{i,k}$$
$$-\sum_{i}\sum_{k}\int_{0}^{Y_{i,k}}m_{i,k}\left(Y_{i,k}\right)dY_{i,k}-\sum_{i}\sum_{j}\sum_{k}c_{i,j,k}T_{i,j,k}$$

with $P$ as price, $D$ as demand, $S$ as supply, $Y$ as manufacturing, $m$ as manufacturing costs, $T$ as trade, $c$ as transportation costs and the indices $i$ for country, $j$ as trade partner country and $k$ as commodity.

### Demand:

The demand for wood-based products (end products in [figure 1](https://github.com/TI-Forest-Sector-Modelling/TiMBA_Additional_Information/raw/main/images/timba_product_transformation.png)) is governed by income ($y$) and prices ($P$). 

$$P_{i,k}(D_{i,k}) = P_{i,k,t-1}\left(\frac{D_{i,k}}{D^{*}_{i,j}}\right)^{1/\delta_{i,k}}$$

$$D_{i,k}^{*}=D_{i,k,t-1}\left(1+\alpha_{y}g_{y}+\alpha_{D,t-1}g_{D,t-1}+\alpha_0\right)$$

with $\delta$ as the demand price elasticity, $g_y$ as the growth rate of income (taken from @Riahi:2017), $g_D$ as the exogenous growth rate of demand, $\alpha$ as the exogenous parameters to shift the influence of the growth rates, and $t$ as time index.


### Supply:

The supply of roundwood and related primary products ([figure 1](https://github.com/TI-Forest-Sector-Modelling/TiMBA_Additional_Information/raw/main/images/timba_product_transformation.png)) depends on wood prices ($P$) and forest development ($g_I$) which in turn is determined by the growth dynamics of forest stock, the change in forest area, and supply quantities of the previous period ($S_{i,k,t-1}$):

$$P_{i,k}(S_{i,k}) = P_{i,k,t-1}\left(\frac{S_{i,k}}{S^{*}_{i,j}}\right)^{1/\lambda_{i,k}}$$

$$S_{i,k}^{*}=S_{i,k,t-1}\left(1+\beta_{y}g_{y}+\beta_{I}g_{I}\right)$$

with $\lambda$ as the supply price elasticity, $g_y$ as the growth rate of income, $g_I$ as the growth rate of forest inventory, and $\beta$ as the exogenous parameters to shift the influence of the growth parameters.

Forest area development and thus, timber supply is linked to GDP per capita developments based on the concept of the environmental Kuznets curve for deforestation [@Panayotou:1993]. 

$$g_{I}=\left(1+\gamma_0\left(\frac{I_{t-1}}{A_{t-1}}\right)^\sigma+\left(\alpha_0+\alpha_{1}y^{'}\right)e^{\alpha_{2}y^{'}}\right)$$

with $I$ as the forest inventory, $A$ as the forest area, $\sigma$ as the elasticity of inventory per unit area, $y^{'}$  as the income per capita, and $\gamma$ and $\alpha$ as exoenous paramters to shift the growth rates.

### Manufacturing:
The production of intermediate and end products depends on manufacturing costs and input-output coefficients. The calibrated input-output coefficients depict the amount of input of primary or intermediate products to produce one unit of end product. The manufacturing costs represent the marginal costs of input, including implicitly costs for labour, energy, capital, and other materials. Manufacturing costs are expressed and shifted using the following equations: 

$$m_{i,k}(Y_{i,k}) = m^{*}_{i,k,t-1}\left(\frac{Y_{i,k}}{Y_{i,j,t-1}}\right)^{\zeta_{i,k}}$$

$$m^{*}_{i,k}=m_{i,k,t-1}\left(1+g_m\right)$$

with $\zeta$ as the manufacturing cost elasticity and $g_m$ as the growth rate of manufacturing costs.

### Trade:
The trade of primary, intermediate, and end products depends on the world price and the transport costs per unit for each commodity ($k$). Transport costs are expressed and shifted using the following equations:

$$c_{i,j,k}(T_{i,j,k}) = c^{*}_{i,j,k,t-1}\left(\frac{T_{i,j,k}}{T_{i,j,k,t-1}}\right)^{\tau_{i,j,k}}$$

$$c^{*}_{i,j,k}=c_{i,j,k,t-1}\left(1+g_f+g^i_t+g^x_i\right)$$

with $\tau$ as the transportation cost elasticity, $g_f$ as the growth rate of freight costs, and $g_t^i$ and $g_t^x$ as the growth rates of import and export ad-valorem taxes.

# Acknowledgements

We acknowledge the contributions from Pixida GmbH and especially Tobias Hierlmeier to revise and improve the model code, the financial and valuable support of the head of the Thünen Institute of Forestry, Matthias Dieter as well as the head of the working group on Forest Products Markets, Holger Weimar. We further thank for the technical support from the Thünen Institute Service Centre for Research Data Management, Harald von Waldow, and Johanna Schliemann, in charge of IT administration at Thünen Insitute of Forestry.

# References

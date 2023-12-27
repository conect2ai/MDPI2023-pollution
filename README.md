&nbsp;
&nbsp;
<p align="center">
  <img width="800" src="http://conect2ai.dca.ufrn.br/static/assets/img/logo.png" />
</p> 

&nbsp;

# Introduction

This space is dedicated to sharing and documenting the work developed as part of an article by the research group [**Conect2AI**](http://conect2ai.dca.ufrn.br).

# About Us

The Conect2AI research group is composed of undergraduate and graduate students from the Federal University of Rio Grande do Norte (UFRN) and aims to apply Artificial Intelligence (AI) and Machine Learning in emerging fields. Our expertise includes Embedded Intelligence and IoT, optimizing resource management and energy efficiency, contributing to sustainable cities. In energy transition and mobility, we apply AI to optimize energy use in connected vehicles and promote more sustainable mobility.

# Technologies

- [Python](https://www.python.org/)

- [Jupyter Notebook](https://jupyter.org/)

- [OSMnx](https://osmnx.readthedocs.io/en/stable/)

- [SUMO](https://sumo.dlr.de/docs/index.html)

- [TraCI](https://sumo.dlr.de/docs/TraCI.html)

# Project

The project consists of a set of Jupyter Notebooks that aim to analyze data from trips made by a vehicle. First you will need to install the dependencies:

```bash
pip install -r requirements.txt
```

After that, you can run the notebooks in the following order:

1. [Initial Analysis](./initial_analysis.ipynb)

    Initially, data from trips made in Natal, Rio Grande do Norte, Brazil were collected. These initial data were used to make a comparative analysis between gasoline and ethanol.

2. [Predict AFR](./predict_afr.ipynb) and [Predict MAF](./predict_maf.ipynb)

    After conducting the initial study, more travel data were collected, expanding the base for training prediction models. As a result, we had:

    - Gasoline: 112964 amostras
    - Ethanol: 40291 amostras

    Prediction models were trained for the two variables (AFR and MAF) used in the calculation of CO₂ presented in the [análise inicial](./initial_analysis.ipynb). The models are saved in [models](./models).

3. [Predict CO₂](./predict_co2.ipynb)

    With the prediction models for AFR and MAF, it was possible to perform the prediction of CO₂.

4. [Create Graph Data](./create_graph_network.ipynb)

    To simulate, it is necessary to obtain a graph of the locality where the simulation will take place.

5. [Simulate](./simulate_sumo.ipynb)

    With the graph and the travel data, it is possible to perform the simulation. Using SUMO, it was possible to simulate two scenarios:

    - Scenario 1: Using gasoline
    - Scenario 2: Using ethanol

    The results of the simulation were compared with the actual data from a portion of a trip using gasoline and another portion using ethanol.

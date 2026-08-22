# Hyperbolic Multi-Agent Reasoning

Supplementary data and dataset-generation resources for the paper:

**Multi-agent reasoning in hyperbolic discs**

## Overview

This repository contains the supplementary datasets and dataset-generation resources used in the experiments on multi-agent reasoning in the Poincaré disc.

The repository provides:

- the tree embeddings used for the single-agent reasoning experiment;
- the narrative text used to construct the multi-agent hierarchical decision structure;
- the script used to generate the multi-agent JSON dataset;
- the resulting dataset containing the hierarchical state structure and conditional probability rules.

## Repository structure

```text
hyperbolic-multi-agent-reasoning/
│
├── README.md
├── LICENSE
│
├── single-agent/
│   └── game24_search_tree.csv # Dataset for the single-agent task (A tree of states for Game of 24)
│
└── multi-agent/
    ├── narrative_generator.py # Script for creating narrative
    ├── probability_generator.py # Script for adding probabilities to keys
    └── exhaustive_combinations_clean.json # Dataset for the multi-agent task
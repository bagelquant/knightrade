# Version Log

Recording by:

- version number, e.g. 0.0.0
    - sprint number, e.g. sprint 1

## Milestones

- 0.0.0: basic setup of the project
- 0.1.0: `data_handler.py` module 
- 0.2.0: `data_preprocessor.py` module 
- 0.3.0: backtest core functinoality 
- 0.4.0: visualization 
- 0.5.0: optimization 
- 0.6.0: async-io 
- 1.0.0: first release

## 0.0.0

Objective:

- Basic setup of the project
    - Project structure
    - `docs/version_log.md`
    - `docs/conventions.md`
    - `docs/proposal.md`
    - `.gitignore`
    - `pyproject.toml`
- Module design

#### Sprint 0

Date: 2025-03-03 - 2025-03-03

Tasks:
- [X] Completed version 0.0.0
- [X] Setup environment

## 0.1.0

DataHandler module

#### Sprint 1

- [X] `standard_data.py` module
- [ ] `data_handler.py` module

Standard Data Object is a class that provides a standard data structure for the project. It is a simple wrapper around `pandas.DataFrame` with some additional methods. It is used to ensure the data is in a consistent format. Especially for type hinting and data manipulation.


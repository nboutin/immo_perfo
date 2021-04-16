# Usecase

Compute variable for a period
Period can be Month, Year, Eternity

# Requirement

Naming convention: R[chapter]_[index]_[version], ex: R01_001_A 

## Variable

R01_001_A Define by name, value_type, period (see class diagram)
R01_002_A Formula is defined to compute variable value
R01_003_A Variable as input does not have formula definition
R01_004_A Variable as computed value has formula definition
R01_005_A Formula parameter are Population, Period

## Model

Model is a Python package containing one or several modules.
Modules inside a model define Variables by inheritance with class Variable.
A model must be provided to ImmoCore

## Immo Core

Store Variables instances define by a model.
Variable are loaded by ImmoCore by providing a path to a Python package.
ImmoCore can construct a Population according to loaded Model.

## Cache

Keep variable computed value
Keep on value per period

## Population

Population is data for Simulation
Population is link between Variable and Cache (data of Variable)
example: caches[Variable.name] = Cache()

## Simulation

Simulation use an instance of Population as input data
and to compute variable value

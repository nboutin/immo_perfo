# Usecase

Calculer une variable suivant une period
Period est Month, Year, Eternity


# Specification

# Variable

Define by name, value_type, period (see class diagramme)
Formula is defined to compute variable value
Variable can be used as input or is computed
Variable as input does not have formula definition
Variable as computed value has formula definition

# Cache

Keep variable computed value
Keep on value per period

# Population

Population is data for Simulation
Population is link between Variable and Holder (data of Variable)
example: holders['loyer_nu'] = Holder()

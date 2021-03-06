# DATA

DISCRETE_Y = True  # Is target variable discrete?
N_CLASSES = 2      # If so, how many classes does it have?
WEIGHTS = None     # How are these classes represented?
N_SAMPLES = 1000   # How many units?
N_FEATURES = 100   # How many features?
N_INFORMATIVE = 5  # How many of these are predictive?

# MODELING

K = 5              # How many folds for cross-validation?
TRAIN_SIZE = .2    # What proportion of units should be used
                   # to select blocking variables?

# SIMULATIONS

N_SIMULATIONS = 100 # How many datasets should be simulated?

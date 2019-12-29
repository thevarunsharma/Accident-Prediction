print(__name__)
class Bayesian_Probability:
    def __init__(self, d1, d2):
        """
        d1 : dict
            conditional probability of event X on accident, P(X | A)
        d2 : dict
            probability of event X, P(X)
        """
        self.prob_XA = d1
        self.prob_X  = d2


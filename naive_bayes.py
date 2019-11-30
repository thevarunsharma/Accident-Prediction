from decimal import Decimal

class Bayesian_Probability:
    def __init__(self, d1, d2):
        self.prob_XA = d1
        self.prob_X  = d2

class NaiveBayes:
    def __init__(self, Probs, state_map):
        self.Probs = Probs
        self.state_map = state_map

    @staticmethod
    def get_state_prob(d, state, state_map):
        for s in state_map[state]:
            if s in d:
                return d[s]

    def road_prob(self, state, type_of_road):
        pxa = __class__.get_state_prob(self.Probs['Type of Road'].prob_XA,
                             state, self.state_map)[type_of_road]
        px = __class__.get_state_prob(self.Probs['Type of Road'].prob_X,
                            state, self.state_map)[type_of_road]
        if pxa == 0 or px == 0:
            return 1
        return Decimal(pxa)/Decimal(px)

    def location_prob(self, state, location):
        pxa = __class__.get_state_prob(self.Probs['Type of Location'].prob_XA,
                             state, self.state_map)[location]
        px = self.Probs['Type of Location'].prob_X[location]
        if pxa == 0 or px == 0:
            return 1
        return Decimal(pxa)/Decimal(px)

    def licence_prob(self, state, licence):
        pxa = __class__.get_state_prob(self.Probs['Type of Licence'].prob_XA,
                             state, self.state_map)[licence]
        px = self.Probs['Type of Licence'].prob_X[licence]
        if pxa == 0 or px == 0:
            return 1
        return Decimal(pxa)/Decimal(px)

    def vehicle_prob(self, state, vehicle):
        pxa = __class__.get_state_prob(self.Probs['Type of Vehicle'].prob_XA,
                             state, self.state_map)[vehicle]
        px = __class__.get_state_prob(self.Probs['Type of Vehicle'].prob_X,
                            state, self.state_map)[vehicle]
        if pxa == 0 or px == 0:
            return 1
        return Decimal(pxa)/Decimal(px)

    def alcohol_prob(self, state, drunk_or_not):
        pxa = __class__.get_state_prob(self.Probs['Drinking'].prob_XA,
                             state, self.state_map)[drunk_or_not]
        px = __class__.get_state_prob(self.Probs['Drinking'].prob_X,
                            state, self.state_map)[drunk_or_not]
        if pxa == 0 or px == 0:
            return 1
        return Decimal(pxa)/Decimal(px)

    def junction_prob(self, junction):
        pxa = self.Probs['Type of Junction'].prob_XA[junction]
        px = self.Probs['Type of Junction'].prob_X[junction]
        if pxa == 0 or px == 0:
            return 1
        return Decimal(pxa)/Decimal(px)

    def prior_prob(self, state):
        return Decimal(__class__.get_state_prob(self.Probs['Priors'].prob_XA,
                                                state, self.state_map))

    def get_probability(self, state, type_of_road, location,
                        licence, vehicle, drunk=False, junction=None):
        p_road = self.road_prob(state, type_of_road)
        p_loc = self.location_prob(state, location)
        p_lic = self.licence_prob(state, licence)
        p_veh = self.vehicle_prob(state, vehicle)
        p_prior = self.prior_prob(state)
        P = p_road * p_loc * p_lic * p_veh * p_prior
        if drunk:
            P *= self.alcohol_prob(state, 'Drunk')
        if junction is not None:
            P *= self.junction_prob(junction)
        return P*100

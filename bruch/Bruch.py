__author__ = 'Raphael Simsek'class Bruch(object):    """    Bruch is a class, which has the capabilities to calculate a fraction with every    possible mathematical usage scenario.    :param int zaehler: numerator of the fraction    :param int nenner: denominator of the fraction    """    def __iter__(self):        """        Overrides iterrator to make the class iterable,        which is overwritten to give the possibility of coding the following:        self.zaehler, self.nenner = Bruch        :return:        """        return (self.zaehler, self.nenner).__iter__()    def __init__(self, zaehler=0, nenner=1):  # using default values for zaehler, nenner        """        Constructor of the class Bruch, to identify the given object of the Bruch class        :return:        """        if isinstance(zaehler, Bruch):            self.zaehler, self.nenner = zaehler  # this is possible because iter is overwritten        elif isinstance(self.zaehler and self.nenner, int):            if nenner != 0:                self.zaehler = zaehler                self.nenner = nenner            else:                raise ZeroDivisionError("Please change the value of the denominator, as a devision by 0 is not possible")        else:            raise TypeError("Numerator and denominator have to be of type int to be allowed in a fraction")    def __float__(self):        """        Overrides float to return the value of the fraction if the float method is called        :return: the divided float value of the fraction is returned        """        return float(self.zaehler / self.nenner)  # because future division is not imported float has to be called    def __repr__(self):        """        Overrides the representation method which returns a string of the current given fraction        :return: returns the value of the fraction parsed to a string        """        if self.nenner == 1:            return "("+str(self.zaehler)+")"        else:            return "("+str(self.zaehler)+"/"+str(self.nenner)+")"
#! /usr/bin/python

class RocketFamily(object):
    def __init__(self, launches, failures, name):
        self.name = name
        self.launches = launches
        self.failures = failures

# Failure counting rules:
# If the primary payload reached its target orbit, it's a success, regardless
# of "anomalies" or "secondary payload failures".
# Most of these numbers are copied from Wikipedia infoboxes and haven't been
# checked.

Falcon9 = RocketFamily(29, 2, 'Falcon 9')
Shuttle = RocketFamily(135, 2, 'Shuttle')
ProtonK = RocketFamily(365, 47, 'Proton-K')
ProtonM = RocketFamily(98, 10, 'Proton-M')
Soyuz2 = RocketFamily(62, 5, 'Soyuz-2')
SoyuzFG = RocketFamily(56, 0, 'Soyuz FG')
SoyuzU = RocketFamily(784, 20, 'Soyuz U')
Zenit = RocketFamily(83, 12, 'Zenit')
AtlasV = RocketFamily(64, 1, 'Atlas V')
Ariane4 = RocketFamily(116, 3, 'Ariane 4')
Ariane5 = RocketFamily(87, 4, 'Ariane 5')
DeltaII = RocketFamily(153, 2, 'Delta II')
DeltaIV = RocketFamily(33, 1, 'Delta IV') # DemoSat reached incorrect orbit
Antares = RocketFamily(5, 1, 'Antares')
Pegasus = RocketFamily(42, 4, 'Pegasus') # Counting Flight 2 but not Flight 5
PSLV = RocketFamily(36, 2, 'PSLV')
GSLV = RocketFamily(10, 5, 'GSLV') # includes F04
LongM2 = RocketFamily(74, 4, 'Long March 2')
HIIA = RocketFamily(30, 1, 'H-IIA')

families = [Falcon9, Shuttle, ProtonK, ProtonM, Soyuz2, SoyuzFG, SoyuzU, Zenit, AtlasV, Ariane4, Ariane5, DeltaII, DeltaIV, Antares, Pegasus, PSLV, GSLV, LongM2, HIIA]

by_name = dict((rkt.name, rkt) for rkt in families)

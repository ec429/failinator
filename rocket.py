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
ProtonM = RocketFamily(98, 10, 'Proton-M')
Soyuz2 = RocketFamily(62, 5, 'Soyuz-2')
SoyuzFG = RocketFamily(56, 0, 'Soyuz FG')
SoyuzU = RocketFamily(784, 20, 'Soyuz U')
AtlasV = RocketFamily(64, 1, 'Atlas V')
Ariane5 = RocketFamily(87, 4, 'Ariane 5')
DeltaII = RocketFamily(153, 2, 'Delta II')
DeltaIV = RocketFamily(33, 0, 'Delta IV') # 1 partial failure, but primary payload reached target orbit

families = [Falcon9, Shuttle, ProtonM, Soyuz2, SoyuzFG, SoyuzU, AtlasV, Ariane5, DeltaII, DeltaIV]

by_name = dict((rkt.name, rkt) for rkt in families)

from worldengine.simulations.basic import find_threshold_f
from noise import snoise2
import numpy

def permeability_sim(height,width,seed):
    rng = numpy.random.RandomState(seed)  # create our own random generator
    base = rng.randint(0, 4096)

    perm = numpy.zeros((height, width), dtype=float)

    octaves = 6
    freq = 64.0 * octaves

    for y in range(0, height):#TODO: numpy optimization?
        # yscaled = float(y) / height  # TODO: what is this?
        for x in range(0, width):
            n = snoise2(x / freq, y / freq, octaves, base=base)
            perm[y, x] = n

    return perm

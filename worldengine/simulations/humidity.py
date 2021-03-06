from worldengine.simulations.basic import find_threshold_f
import numpy
       
def humidity_sim(humids,precipitation,irrigation,ocean):
    precipitationWeight = 1.0
    irrigationWeight = 3
    shape=precipitation.shape
    data = numpy.zeros(shape, dtype=float)
    
    pdata = precipitation 
    pweight=precipitationWeight
    idata= irrigation
    iweight=irrigationWeight
    data1 = ( pdata * pweight - idata * iweight )
    data2 = (precipitationWeight + irrigationWeight)
    data=data1/data2

    # These were originally evenly spaced at 12.5% each but changing them
    # to a bell curve produced better results
    
    quantiles = {}
    quantiles['12'] = find_threshold_f(data, humids[6], ocean)
    quantiles['25'] = find_threshold_f(data, humids[5], ocean)
    quantiles['37'] = find_threshold_f(data, humids[4], ocean)
    quantiles['50'] = find_threshold_f(data, humids[3], ocean)
    quantiles['62'] = find_threshold_f(data, humids[2], ocean)
    quantiles['75'] = find_threshold_f(data, humids[1], ocean)
    quantiles['87'] = find_threshold_f(data, humids[0], ocean)
    return data, quantiles

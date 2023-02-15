estimator400 = [14632.85427537180657964200, 8.481293968584910913932617404498]
estimator600 = [14334.16628814087016507983, 12.363334961753698948427881987300]
estimator800 = [13581.11124571907384961378, 23.266305511724205246082419762388]



def estimateDistance(grayScaleValue):
    estimated400 = estimator400[1] + estimator400[0]*1/grayScaleValue
    estimated600 = estimator600[1] + estimator600[0]*1/grayScaleValue
    estimated800 = estimator800[1] + estimator800[0]*1/grayScaleValue
    
    return ((estimated400 + estimated600 + estimated800)/3)/100
''' Utility Functions
'''

from datetime import datetime , timedelta
import math

def printProgressBar (fps,iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█'):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    estimated_time = None
    if fps != 0:
        estimated_time = math.ceil((total-iteration)/(fps))
    else:
        estimated_time = int(9999)
    fps = "FPS: {:.2f}".format(fps)

    estimated_time = "Estimated Time : {}".format(str(timedelta(seconds=estimated_time)))
    print('\r%s |%s| %s%% %s\t\t%s\t\t%s' % (prefix, bar, percent, suffix, fps, estimated_time), end = '\r')
    # Print New Line on Complete
    if iteration == total:
        print()

def printProgressBar1 (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█'):
    """ Print progress bar with required % completion """ 
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = '\r')
    # Print New Line on Complete
    if iteration == total:
        print()

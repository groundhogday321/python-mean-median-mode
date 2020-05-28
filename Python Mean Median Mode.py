



import scipy.stats
import numpy
import statistics

# MEAN (arithmetic mean)
drive_speeds_mph = [55, 60, 61, 65, 66, 67, 70, 71]

# with numpy
mean1 = numpy.mean(drive_speeds_mph)
print(mean1)
# prints 64.375

# with statistics
mean2 = statistics.mean(drive_speeds_mph)
print(mean2)
# prints 64.375

# MEDIAN (middle value - if two values in middle take the arithmetic mean)
house_prices = [50000, 101000, 105000, 110000, 115000, 120000, 125000, 415000]

# with numpy
median1 = numpy.median(house_prices)
print(median1)
# prints 112500.0

# with statistics
median2 = statistics.median(house_prices)
print(median2)
# prints 112500.0

# MODE (value that occurs most often)
height_in_inches = [65, 66, 66, 67, 68, 68, 69, 70, 70, 70, 70]

# with statistics
mode1 = statistics.mode(height_in_inches)
print(mode1)
# prints 70

# with scipy
mode2 = scipy.stats.mode(height_in_inches)
print(mode2)
# prints ModeResult(mode=array([70]), count=array([4]))
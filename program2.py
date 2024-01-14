# The task is to read a set of temperature data (the monthly high temperatures at Heathrow Airport for 1948 through 2016) from a file and then find some basic information: the highest and lowest
#temperatures, the mean (average) temperature, and the median temperature (the temperature in the middle if all the temperatures are sorted).
# Determine how many unique temperatures are in the list.

temperatures = []
file_name = 'E:\Python codes\Practice_codes\python_programs\lab_05.txt'
with open(file_name) as infile:
    for row in infile:
        temperatures.append(float(row.strip()))

highest_temperature = max(temperatures)
lowest_temperature = min(temperatures)
average_temperature = sum(temperatures) / len(temperatures)
temperatures.sort()
median = len(temperatures) // 2
median_temperature = (temperatures[median] + temperatures[~median]) / 2

print("max = {}" .format(highest_temperature))
print("min = {}" .format(lowest_temperature))
print("mean = {}" .format(average_temperature))
print("median = {}" .format(median_temperature))

#unique temperatures

unique_temperatures = len(set(temperatures))

print("Length of temps - {}" .format(len(temperatures)))
print("Length of unique temps - {}" .format(unique_temperatures))
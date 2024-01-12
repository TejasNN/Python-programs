# The task is to read a set of temperature data (the monthly high temperatures at Heathrow Airport for 1948 through 2016) from a file and then find some basic information: the highest and lowest
#temperatures, the mean (average) temperature, and the median temperature (the temperature in the middle if all the temperatures are sorted).

temperatures = []
file_name = 'E:\Python codes\Practice_codes\python_programs\lab_05.txt'
with open(file_name) as infile:
    for row in infile:
        temperatures.append(int(float(row.strip())))

highest_temperature = max(temperatures)
lowest_temperature = min(temperatures)
average_temperature = sum(temperatures) / len(temperatures)
median = len(temperatures) // 2
median_temperature = (temperatures[median] + temperatures[~median]) / 2

print(highest_temperature)
print(lowest_temperature)
print("%.2f" % average_temperature)
print(median_temperature)


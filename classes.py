class Time:
    """ A class that represents a time of day """
    def __init__(self):
        self.hours = 0
        self.minutes = 0


time1 = Time()  # Create an instance of the Time class called time1
time1.hours = 7
time1.minutes = 30

time2 = Time()  # Create a second instance called time2
time2.hours = 12
time2.minutes = 45

print('{} hours and {} minutes'.format(time1.hours, time1.minutes))
print('{} hours and {} minutes'.format(time2.hours, time2.minutes))
###
# Program that returns a string specifying the time in a given format.
#

def time_string(hours, minutes, time_format):
    if time_format == 24:
        return f'{hours:02}:{minutes:02}'
    else:
        if hours > 12:
            return f'{hours-12}:{minutes:02}pm'
        elif hours == 12:
            return f'{hours}:{minutes:02}pm'
        elif hours > 0:
            return f'{hours}:{minutes:02}am'
        elif hours == 0:
            return f'{hours+12}:{minutes:02}am'
            

hour = int(input('Enter an hour: '))
minute = int(input('Enter the minutes: '))
format = int(input('Enter the time format (12 for 12-hour clock and 24 for a 24-hour clock): \n'))
print(f'{time_string(hour, minute, format)}')

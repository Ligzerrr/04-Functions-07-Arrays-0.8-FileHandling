import converters

print('### Test converters')
print(f'Three meters is {converters.m_to_cm(3)}cm')
print(f'Four hundred centimeters is {converters.cm_to_m(400)}m')
print(f'Fifteen centimeters is {converters.cm_to_inch(15)} inch')
print(f'Five feet ten inches is {converters.feet_inch_to_cm(5,10)}cm')
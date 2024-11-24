#!/usr/bin/env python3
# Student ID: asarmiento6
from lab7c import *  # Import necessary functions and Time class

# Define Time objects
t1 = Time(8, 0, 0)
t2 = Time(8, 55, 0)
t3 = Time(9, 50, 0)

# Define time delta (50 minutes)
td = Time(0, 50, 0)

# Add time
tsum1 = sum_times(t1, td)
tsum2 = sum_times(t2, td)
t3None = change_time(t3, 1800)  # This assumes `change_time` is defined in lab7c.py

# Format and print the results
ft = format_time
print(ft(t1), '+', ft(td), '-->', ft(tsum1))
print(ft(t2), '+', ft(td), '-->', ft(tsum2))
print('09:50:00 + 1800 sec', '-->', ft(t3))


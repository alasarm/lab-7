#!/usr/bin/env python3
# Student ID: asarmiento6

class Time:
    """Simple object type for time of the day.
    data attributes: hour, minute, second
    """
    def __init__(self, hour=12, minute=0, second=0):
        """Constructor for time object""" 
        self.hour = hour
        self.minute = minute
        self.second = second

def format_time(t):
    """Return time object (t) as a formatted string"""
    return f'{t.hour:02d}:{t.minute:02d}:{t.second:02d}'

def sum_times(t1, t2):
    """Add two time objects and return the sum."""
    sum = Time(0, 0, 0)
    sum.second = t1.second + t2.second
    sum.minute = t1.minute + t2.minute + (sum.second // 60)  # Add overflow from seconds
    sum.second %= 60  # Normalize seconds
    sum.hour = t1.hour + t2.hour + (sum.minute // 60)  # Add overflow from minutes
    sum.minute %= 60  # Normalize minutes
    sum.hour %= 24  # Normalize hours (optional if staying within 24-hour time)
    return sum

def valid_time(t):
    """Check for the validity of the time object attributes:
        24 > hour > 0, 60 > minute > 0, 60 > second > 0 """
    if t.hour < 0 or t.minute < 0 or t.second < 0:
        return False
    if t.minute >= 60 or t.second >= 60 or t.hour >= 24:
        return False
    return True

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print(f"Error: {filename} not found.")

if __name__ == "__main__":
    read_file('laboutput.txt')


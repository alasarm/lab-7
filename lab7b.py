#!/usr/bin/env python3
# Student ID: [seneca_id]

class Time:
    """Simple object type for time of the day.
    data attributes: hour, minute, second
    """
    def __init__(self, hour=0, minute=0, second=0):
        """Constructor for time object""" 
        self.hour = hour
        self.minute = minute
        self.second = second

def format_time(t):
    """Return time object (t) as a formatted string."""
    return f'{t.hour:02d}:{t.minute:02d}:{t.second:02d}'

def valid_time(t):
    """Check for the validity of the time object attributes:
        24 > hour >= 0, 60 > minute >= 0, 60 > second >= 0."""
    if t.hour < 0 or t.minute < 0 or t.second < 0:
        return False
    if t.hour >= 24 or t.minute >= 60 or t.second >= 60:
        return False
    return True

def change_time(t, seconds):
    """
    Adjust the time object (t) by adding or subtracting seconds.
    """
    if not valid_time(t):
        raise ValueError("Invalid time object.")
    
    total_seconds = t.hour * 3600 + t.minute * 60 + t.second + seconds
    # Normalize to 24-hour range
    total_seconds %= 86400
    if total_seconds < 0:
        total_seconds += 86400

    t.hour = total_seconds // 3600
    t.minute = (total_seconds % 3600) // 60
    t.second = total_seconds % 60

def append_to_file(filename):
    """Append user input to the specified file."""
    try:
        with open(filename, 'a') as file:
            user_input = input("Enter text to append: ")
            file.write(user_input + '\n')
            print(f"'{user_input}' appended to {filename}.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Test change_time() functionality
    time1 = Time(9, 50, 0)
    print("Original time:", format_time(time1))
    change_time(time1, 1800)  # Add 1800 seconds (30 minutes)
    print("After adding 1800 seconds:", format_time(time1))
    change_time(time1, -1800)  # Subtract 1800 seconds (30 minutes)
    print("After subtracting 1800 seconds:", format_time(time1))

    # Append to file functionality
    append_to_file('laboutput.txt')


#!/usr/bin/env python3
# Student ID: asarmiento6

class Time:
    """Simple object type for time of the day.
    Data attributes: hour, minute, second
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

def time_to_sec(t):
    """Convert a Time object to total seconds."""
    if not valid_time(t):
        raise ValueError("Invalid time object.")
    return t.hour * 3600 + t.minute * 60 + t.second

def sec_to_time(seconds):
    """Convert total seconds to a Time object."""
    if seconds < 0:
        raise ValueError("Seconds cannot be negative.")
    seconds %= 86400  # Normalize to 24-hour range
    hour = seconds // 3600
    minute = (seconds % 3600) // 60
    second = seconds % 60
    return Time(hour, minute, second)

def sum_times(t1, td):
    """Sum two Time objects. Returns a new Time object."""
    total_seconds = time_to_sec(t1) + time_to_sec(td)
    return sec_to_time(total_seconds)

def change_time(t, seconds):
    """Change the given time by a certain number of seconds."""
    total_seconds = time_to_sec(t) + seconds
    return sec_to_time(total_seconds)

def read_times_from_file(filename):
    """
    Read time data from a file and return a list of Time objects.
    Each line in the file should be in the format HH:MM:SS.
    """
    time_list = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                parts = line.split(':')
                if len(parts) == 3:
                    hour, minute, second = map(int, parts)
                    t = Time(hour, minute, second)
                    if valid_time(t):
                        time_list.append(t)
                    else:
                        print(f"Invalid time found in file: {line}")
                else:
                    print(f"Invalid format in file: {line}")
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
    return time_list

# Main code to test and demonstrate functionality
if __name__ == "__main__":
    # Test the time-to-seconds and sec-to-time functions
    t1 = Time(8, 0, 0)  # 08:00:00
    t2 = Time(8, 55, 0)  # 08:55:00
    td = Time(0, 50, 0)  # 50 minutes

    # Sum times
    tsum1 = sum_times(t1, td)
    tsum2 = sum_times(t2, td)

    # Change time by seconds
    t3 = Time(9, 50, 0)  # 09:50:00
    t3_changed = change_time(t3, 1800)  # Add 1800 seconds (30 minutes)

    # Format and print results
    ft = format_time
    print(f"{ft(t1)} + {ft(td)} --> {ft(tsum1)}")
    print(f"{ft(t2)} + {ft(td)} --> {ft(tsum2)}")
    print(f"{ft(t3)} + 1800 sec --> {ft(t3_changed)}")

    # Read times from file
    times = read_times_from_file('laboutput.txt')
    print("\nTimes read from file:")
    for t in times:
        print(format_time(t))


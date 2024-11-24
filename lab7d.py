#!/usr/bin/env python3
# Student ID: [seneca_id]

class Time:
    """Simple object type for time of the day.
       data attributes: hour, minute, second
       function attributes: __init__, __str__, __repr__
                            time_to_sec, format_time,
                            change_time, sum_times
    """
    
    def __init__(self, hour=12, minute=0, second=0):
        """Constructor for time object"""
        self.hour = hour
        self.minute = minute
        self.second = second
    
    def format_time(self):
        """Return time object as a formatted string"""
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'
    
    def sum_times(self, t2):
        """Add two time objects and return the sum."""
        # Convert both times to seconds
        t1_seconds = self.time_to_sec()
        t2_seconds = t2.time_to_sec()
        
        # Sum the times in seconds
        total_seconds = t1_seconds + t2_seconds
        
        # Convert the total seconds back to a time object
        return sec_to_time(total_seconds)
    
    def change_time(self, seconds):
        """Change time by adding or subtracting seconds"""
        time_seconds = self.time_to_sec()
        new_time = sec_to_time(time_seconds + seconds)
        self.hour, self.minute, self.second = new_time.hour, new_time.minute, new_time.second
        return None

    def time_to_sec(self):
        """Convert time object to total seconds since midnight"""
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    def valid_time(self):
        """Check if the time object has valid time attributes"""
        if self.hour < 0 or self.minute < 0 or self.second < 0:
            return False
        if self.minute >= 60 or self.second >= 60 or self.hour >= 24:
            return False
        return True

def sec_to_time(seconds):
    """Convert a number of seconds to a time object in hour, minute, second format"""
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time


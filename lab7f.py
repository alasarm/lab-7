#!/usr/bin/env python3
# Student ID: asarmiento6

class Time:
    """Class for representing a time object with hour, minute, and second."""

    def __init__(self, hour=0, minute=0, second=0):
        """Constructor for time object."""
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        """String representation of the time object."""
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def __repr__(self):
        """Return a representation of the time object in HH.MM.SS format."""
        return f'{self.hour:02d}.{self.minute:02d}.{self.second:02d}'

    def time_to_sec(self):
        """Convert the time object to total seconds."""
        return self.hour * 3600 + self.minute * 60 + self.second

    def format_time(self):
        """Return the time formatted as HH:MM:SS."""
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def change_time(self, seconds):
        """Change the time by adding or subtracting the given number of seconds."""
        total_seconds = self.time_to_sec() + seconds
        
        # Normalize total_seconds to stay within a 24-hour range (86400 seconds in a day)
        total_seconds %= 86400  # Ensure time stays within a day (24 hours)
        
        # Convert the total seconds back to hours, minutes, and seconds
        new_hour = total_seconds // 3600  # Calculate hours
        total_seconds %= 3600  # Get remaining seconds after hours
        new_minute = total_seconds // 60  # Calculate minutes
        new_second = total_seconds % 60  # Get remaining seconds
        
        # Return the new time object
        return Time(new_hour, new_minute, new_second)
    
    def sum_times(self, other):
        """Sum the current time with another time object and return a new Time object."""
        total_seconds = self.time_to_sec() + other.time_to_sec()

        # Normalize to a 24-hour period
        total_seconds %= 86400

        # Convert total seconds back to hours, minutes, and seconds
        new_hour = total_seconds // 3600
        total_seconds %= 3600
        new_minute = total_seconds // 60
        new_second = total_seconds % 60
        
        return Time(new_hour, new_minute, new_second)

    def is_valid_time(self):
        """Check if the current time is valid (e.g., hour should be between 0 and 23, minute and second between 0 and 59)."""
        return 0 <= self.hour <= 23 and 0 <= self.minute <= 59 and 0 <= self.second <= 59

    def __eq__(self, other):
        """Override equality operator to compare two Time objects."""
        return self.hour == other.hour and self.minute == other.minute and self.second == other.second

    def __lt__(self, other):
        """Override less-than operator to compare two Time objects."""
        return self.time_to_sec() < other.time_to_sec()

    def __le__(self, other):
        """Override less-than-or-equal operator to compare two Time objects."""
        return self.time_to_sec() <= other.time_to_sec()

    def __gt__(self, other):
        """Override greater-than operator to compare two Time objects."""
        return self.time_to_sec() > other.time_to_sec()

    def __ge__(self, other):
        """Override greater-than-or-equal operator to compare two Time objects."""
        return self.time_to_sec() >= other.time_to_sec()

    def __ne__(self, other):
        """Override not-equal operator to compare two Time objects."""
        return not self.__eq__(other)

    def __add__(self, other):
        """Overload the + operator to add two Time objects."""
        total_seconds = self.time_to_sec() + other.time_to_sec()

        # Normalize to a 24-hour period
        total_seconds %= 86400

        # Convert total seconds back to hours, minutes, and seconds
        new_hour = total_seconds // 3600
        total_seconds %= 3600
        new_minute = total_seconds // 60
        new_second = total_seconds % 60
        
        return Time(new_hour, new_minute, new_second)


# Test cases to validate the implementation
if __name__ == "__main__":
    # Test for Time object creation
    time1 = Time(9, 50, 0)
    time2 = Time(2, 30, 10)
    
    # Print objects to test __str__ and __repr__
    print("Time 1:", time1)  # Should print '09:50:00'
    print("Time 2:", time2)  # Should print '02:30:10'
    
    # Test the __repr__ method
    print("repr(Time 1):", repr(time1))  # Should print '09.50.00'
    print("repr(Time 2):", repr(time2))  # Should print '02.30.10'
    
    # Test sum_times method
    summed_time = time1.sum_times(time2)
    print("Summed Time:", summed_time)  # Should print the sum in HH:MM:SS format
    
    # Test time_to_sec method
    print("Time 1 in seconds:", time1.time_to_sec())  # Should print the number of seconds since 00:00:00
    print("Time 2 in seconds:", time2.time_to_sec())  # Should print the number of seconds since 00:00:00
    
    # Test change_time method
    time3 = time1.change_time(5000)  # Add 5000 seconds
    print("Time 1 after change by 5000 seconds:", time3)  # Should print the time after adding 5000 seconds

    # Test is_valid_time method
    print("Is Time 1 valid?", time1.is_valid_time())  # Should return True
    invalid_time = Time(25, 61, 0)
    print("Is Invalid Time valid?", invalid_time.is_valid_time())  # Should return False
    
    # Test comparison operators
    print("Time 1 == Time 2:", time1 == time2)  # Should print False
    print("Time 1 < Time 2:", time1 < time2)  # Should print False
    print("Time 1 <= Time 2:", time1 <= time2)  # Should print False
    print("Time 1 > Time 2:", time1 > time2)  # Should print True
    print("Time 1 >= Time 2:", time1 >= time2)  # Should print True
    print("Time 1 != Time 2:", time1 != time2)  # Should print True

    # Test addition operator
    time_sum = time1 + time2
    print("Time 1 + Time 2:", time_sum)  # Should print the sum in HH:MM:SS format


def get_days_later(days):
    """
    Returns the string representation of days later.

    Args:
        days (int): The number of days.

    Returns:
        str: String indicating the number of days later.
    """
    if days == 1:
        return ' (next day)'
    elif days > 1:
        return f' ({days} days later)'
    else:
        return ''

def add_time(start, duration, day=False):
    """
    Adds the given duration to the start time and returns the new time.

    Args:
        start (str): The starting time in the format 'HH:MM AM/PM'.
        duration (str): The duration to be added in the format 'HH:MM'.
        day (str, optional): The starting day of the week (case insensitive). Defaults to False.

    Returns:
        str: The new time after adding the duration.
    """
    new_time = ''
    week_days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    full_day = 24
    half_day = 12
    days = 0
    new_hours = 0

    # Split up start and duration and store time as int
    start_hours, start_minutes, ampm = start.replace(':', ' ').split(' ')
    duration_hours, duration_minutes = map(int, duration.split(':'))
    start_hours, start_minutes = int(start_hours), int(start_minutes)

    # Convert to 24 hour time clock for accurate addition
    if ampm == 'PM':
        start_hours += half_day
    
    # Calculate the hours and minutes after adding
    total_hours = start_hours + duration_hours
    new_minutes = start_minutes + duration_minutes
    # Set minutes so that they are less than 1 hr aka 60 mins
    if new_minutes >= 60:
        total_hours += new_minutes // 60
        new_minutes = new_minutes % 60
    if new_minutes // 10 == 0:
        new_minutes = '0' + str(new_minutes)
    
    # Find number of days from total hours calculated
    if total_hours > 24:
        days += total_hours // 24
    
    # Set the correct hours time back in 12-hour clock
    new_hours = total_hours % half_day
    if new_hours == 0:
        new_hours = 12
    
    # Calculate weather in 'AM' or 'PM'
    if ampm == 'PM' and total_hours > 12:
        total_hours -= 12
    
    # Variable to find the number of times time changed from 'AM' to 'PM' and vice versa
    # Helpful in finding the which is right 'AM' or 'PM' for current time
    new_ampm = (total_hours // 12) % 2
    # If it rolled over back to same then no need to change, else change
    if new_ampm == 1:  
        if ampm == 'AM':
            ampm = 'PM'
        else:
            ampm = 'AM'
    
    # If optional variable not given then simply print else find the day and then print
    if not day:
        new_time = str(new_hours) + ':' + str(new_minutes) + ' ' + ampm + get_days_later(days)
    if day:
        day = day.strip().lower()
        new_day = week_days[(week_days.index(day) + days) % 7]
        new_day = new_day[0].upper() + new_day[1:]
        new_time = str(new_hours) + ':' + str(new_minutes) + ' ' + ampm + ', ' + new_day + get_days_later(days)
    return new_time

# Example test
print(add_time('3:30 PM', '2:12', 'Monday'))  # should return '5:42 PM, Monday'

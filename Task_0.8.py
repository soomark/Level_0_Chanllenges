# Function converts seconds to hour and minutes
def time_conversion(seconds):
    # Convert seconds to hour
    hours = seconds // 3600

    # Converts seconds to minute
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    print("%0d hours %0d minutes " % (minutes, seconds))


seconds_input = (int(input("Enter the Time in seconds: ")))
time_conversion(seconds_input)

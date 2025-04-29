#CP6
def print_24_hour_labels():
    for hour in range(24):
        if hour == 0:
            label = "12 AM - Midnight"
        elif hour == 12:
            label = "12 PM - Noon"
        elif hour < 12:
            label = f"{hour} AM"
        else:
            label = f"{hour - 12} PM"
        print(label)

print_24_hour_labels()

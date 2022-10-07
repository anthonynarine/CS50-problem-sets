# cs50 problem set 1 meal

def main():
# prompts the user for a time.
    time_entered = input ("What time is it? ")
# call the convert function pass in the user input
    time_entered = convert(time_entered)
    if time_entered >= 7 and time_entered <=8:
        print("breakfast time")
    elif time_entered >= 12 and time_entered <=13:
        print ("lunch time")
    elif time_entered >= 18 and time_entered <= 19:
        print ("dinner time")
    else:
        print ("it's not time for a meal")


def convert(time):
# split hours and minutes and convert to a float
    hours, minutes = time.split(":")
    hours = float (hours)
# 60 mins in an hour. / 60 for minutes
    minutes = float(minutes) / 60
# return minuts and hours to main function 
    return hours + minutes


if __name__ == "__main__":
        ...
        main()
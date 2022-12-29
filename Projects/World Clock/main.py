import datetime  
while (True):
  city = input("Enter city: ")
  city = city.lower()
  current_time = datetime.datetime.utcnow()
  hour = current_time.hour
  minute = current_time.minute
  second = current_time.second
  
  if city == "boston":
    hour = hour - 4 

  elif city == "tokyo":
    hour = hour + 9

  elif city == "chicago":
    hour = hour - 5 

  elif city == "seattle":
    hour = hour - 7

  ## add more cities here

  elif city == "mumbai":
    if (minute + 30) > 60:
      if hour >=24:
        hour = abs(24 - (hour + 6))   # Solve this problem of more than 24 thing.
        hour = hour + 6
        minute = abs(60 - (minute + 30))
    else:
      hour = hour + 5
      minute = minute + 30

  elif city == "beijing":
    hour = hour + 8

  elif city == "karachi":
    hour = hour + 5

  elif city == "now":
    hour = hour

  elif city == "exit":
    break
    
  else:
    print(city, "is not added")
    city = "GMT" 

  print(city[0].upper() + city[1:].lower(), str(hour) + ":" + str(minute) + ":" + str(second))

# The error is of GMT time setting. As GMT time setting outputs time as of now.
# The error is of GMT time setting. As GMT time setting outputs time as of now.

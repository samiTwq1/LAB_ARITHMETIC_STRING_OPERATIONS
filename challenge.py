Seconds = int(input("Enter the number of seconds: "))

Hours = Seconds // 3600

Minutes = (Seconds % 3600) // 60

remaining_seconds = Seconds % 60

print("Hours:", Hours)

print("Minutes:", Minutes)

print("Seconds:", remaining_seconds)

print("0", Hours,  ":0", Minutes, ":0",remaining_seconds)
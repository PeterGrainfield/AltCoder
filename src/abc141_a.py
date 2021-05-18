S = input()

weather = ("Sunny", "Cloudy", "Rainy")

for i in range(len(weather)):
    if S == weather[i]:
        print(weather[(i+1)%len(weather)])
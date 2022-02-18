def listToString(s):
    str1 = ""
    for ele in s:
        str1 += ele
    return str1

class Weather ():

    def __init__(self):
        self.weather = ""

    def sun_weather(self):
        self.weather = "cолнце"
        print(self.weather + " погода на данный момент")

    def rain_weather(self):
        self.weather = "дождь"
        print(self.weather + " погода на данный момент")

    def drought_weather(self):
        self.weather = "засуха"
        print(self.weather + " погода на данный момент")


class Plants():
    def __init(self, harvest_process):
        self.harvest_process = harvest_process
    def get_name_plant(self):
        self.plantnames = list(input("Введите название - "))
        return listToString(self.plantnames)
    def get_descriptive_name(self):
        self.plantspecies = list(input("Введите тип растения - "))
        return listToString(self.plantscpecies)
    def harvest_process(self,harvest_process,n):
        if self.plantspecies.lower() == "овощи":
            if harvest_process > n:
                harvest_process = 0
            else:
                harvest_process += 1
        #elif self.plantspecies.lower() == "дерево":
        return harvest_process

class Garden_bed():
    def __init__(self):


#gryads = GardenBeds()
#a = gryads.
#gryads.plant_selection()
#print(gryads.plant_selection())
wear = Weather()
wear.sun_weather()
print(wear.weather)
wear.rain_weather()
print(wear.weather)
weather = wear.weather
potato = Plants()
cv = potato.get_name_plant()
print(cv)



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
    def __init(self, harvest_process,id):
        self.harvest_process = harvest_process
        self.id = id

    def get_name_plant(self):
        self.plantnames = list(input("Введите название - "))
        return listToString(self.plantnames)

    def get_descriptive_name(self):
        self.plantspecies = list(input("Введите тип растения - "))
        return listToString(self.plantscpecies)

    def harvest_process(self,harvest_process,n):
        if self.id == 1:
            if harvest_process > n:
                harvest_process = 0
            else:
                harvest_process += 1
       # elif self.id == 2:

        return harvest_process

class Garden_bed():

    def __init__(self, int_max_size):
        self.array = [None] * int_max_size
        self.size = int_max_size

    def append(self, value):
        int_i = 0
        ith_value = self.array[int_i]
        while ith_value != None:
            int_i += 1
            ith_value = self.array[int_i]
        self.array[int_i] = value

    def remove(self, value):
        bool_found = False
        int_i = 0
        while not bool_found:
            if self.array[int_i] == value:
                self.pop_index(int_i)
                bool_found = True
            int_i += 1

    def insert(self, int_index, value):
        int_i = 0
        while self.array[int_i] != None:
            int_i += 1
        while int_i > int_index:
            self.array[int_i] = self.array[int_i - 1]
            int_i -= 1
        self.array[int_i] = value

    def count(self, value):
        counter = 0
        int_i = 0
        while int_i < self.size and self.array[int_i] != None:
            if self.array[int_i] == value:
                counter += 1
            int_i += 1
        return counter

class Garden_master(Garden_bed):

    def __init__(self,int_max_size):
        super.__init__(int_max_size)



wear = Weather()
wear.sun_weather()
print(wear.weather)
wear.rain_weather()
print(wear.weather)
weather = wear.weather
potato = Plants()
cv = potato.get_name_plant()
print(cv)
gryadka = Garden_bed(50)
gryadka.append(5)
print(gryadka.count(6))
print(gryadka.array)

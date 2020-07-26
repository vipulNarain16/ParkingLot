import type_of_Vechicle
class basic_parkinglot:
    def __init__(self):
        self.space = 0
        self.slotNum = 0
        self.total_occslots = 0

    def createparkinglot(self,space):
        self.slot = [0] * space
        self.space = space
        return  self.space

    def park_vechicle(self,registrationnumber,color):
        if self.total_occslots < self.space:
            #get slot number
            for i in range(len(self.slot)):
                if(self.slot[i]==0):
                    slotNum = i
            self.slot[slotNum] = type_of_Vechicle.car(registrationnumber,color)
            self.slotNum = self.slotNum+1
            self.total_occslots = self.total_occslots + 1
            return slotNum+1
        else:
            print("Sorry, parking lot is full")
            return -1

    def print_details(self):
        for i in range(len(self.slot)):
            if(self.slot[i]!=-1):
                print("Slot number is {}, registration number is {} and color is {} of the parked vehicles."
                      .format(str(i+1),str(self.slot[i].registrationnumber),str(self.slot[i].color)))
            else:
                continue

    def remove(self,slotNum):
        self.slot[slotNum-1] = 0
        self.total_occslots = self.total_occslots -1
        return self.total_occslots

#retrieve slot number from registration number of car,
    def get_details(self,registrationnumber,color):
        for i in range(len(self.slot)):
            if self.slot[i].registrationnumber == registrationnumber :
                return i+1
            else:
                continue
        for i in self.slot:
            registrationnum=[]
            if i.color == color:
                registrationnum.append(registrationnumber)
            return registrationnum
        return -1







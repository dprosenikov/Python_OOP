from project.medicine.medicine import Medicine
from project.medicine.painkiller import Painkiller
from project.medicine.salve import Salve
from project.supply.supply import Supply
from project.supply.food_supply import FoodSupply
from project.supply.water_supply import WaterSupply
from project.survivor import Survivor


class Bunker:
    def __init__(self):
        self.survivors = []
        self.supplies = []
        self.medicine = []

    @property
    def food(self):
        food_list = [f for f in self.supplies if f.__class__.__name__ == 'FoodSupply']
        if not food_list:
            raise IndexError("There are no food supplies left!")
        return food_list

    @property
    def water(self):
        water_list = [w for w in self.supplies if w.__class__.__name__ == 'WaterSupply']
        if not water_list:
            raise IndexError("There are no water supplies left!")
        return water_list

    @property
    def painkillers(self):
        painkiller_list = [p for p in self.medicine if p.__class__.__name__ == 'Painkiller']
        if not painkiller_list:
            raise IndexError("There are no painkillers left!")
        return painkiller_list

    @property
    def salves(self):
        salves_list = [s for s in self.medicine if s.__class__.__name__ == 'Salve']
        if not salves_list:
            raise IndexError("There are no salves left!")
        return salves_list

    def add_survivor(self, survivor: Survivor):
        if survivor in self.survivors:
            raise ValueError("Survivor with name {name} already exists.")
        self.survivors.append(survivor)

    def add_supply(self, supply: Supply):
        self.supplies.append(supply)

    def add_medicine(self, medicine: Medicine):
        self.medicine.append(medicine)

    def heal(self, survivor: Survivor, medicine_type: str):
        pass
        #medicine_item = '26'
        #if survivor.needs_healing:
            #medicine_item = '62'
            #if isinstance(medicine_type, Painkiller):
                #medicine_item = self.painkillers.pop()
            #elif isinstance(medicine_type, Painkiller):
                #medicine_item = self.salves.pop()
            #print(medicine_item)
            #medicine_item.apply(survivor)
            #return f"{survivor.name} healed successfully with {medicine_type}"

    def sustain(self, survivor: Survivor, sustenance_type: str):
        pass

    def next_day(self):
        pass

# surv1 = Survivor('Mitko', 34)
# surv1.health = 50
# keks = FoodSupply()
# analgin = Painkiller()
# sal = Salve()
# bunk = Bunker()
# bunk.add_survivor(surv1)
# bunk.add_supply(keks)
# bunk.add_medicine(analgin)
# bunk.add_medicine(sal)
# print(bunk.medicine)
# print(bunk.painkillers)
# print(analgin)
# bunk.heal(surv1, 'analgin')
# print(surv1.needs)
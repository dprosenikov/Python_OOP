from project.supply.supply import Supply


class WaterSupply(Supply):
    def __init__(self):
        Supply.__init__(self, 40)

#WS = WaterSupply()
#print(WS.needs_increase)
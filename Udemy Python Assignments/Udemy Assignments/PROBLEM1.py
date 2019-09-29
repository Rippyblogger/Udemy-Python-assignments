class Line:

    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
        #method to calculate distance of a line with  dimensional coordinates
    def distance (self):
        import math
        dis = (self.coor1[0]-self.coor2[0])**2 + (self.coor1[1]-self.coor2[1])**2
        dis = math.sqrt(dis)
        return dis
    #method to calculate slope of a line with 2 dimensional coordinates
    def slope (self):
        slo = (self.coor2[1] - self.coor1[1]) / (self.coor2[0]- self.coor1[0])
        return slo


solution = Line((3,2),(8,10))
print(solution.slope())

print (solution.distance())

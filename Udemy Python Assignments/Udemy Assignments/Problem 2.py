class Cylinder:
    import math
    pi = math.pi
    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        Vol = Cylinder.pi*(self.radius**2)*self.height
        return Vol
    def surface_area(self):
        SurfaceArea = (2*Cylinder.pi*self.radius*self.height)+(2*Cylinder.pi*(self.radius**2))
        return SurfaceArea
        return Cylinder.pi

Cyl = Cylinder(2,3)
print(Cyl.volume())
print(Cyl.surface_area())
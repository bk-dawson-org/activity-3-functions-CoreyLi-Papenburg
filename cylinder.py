import math

def getCylinderVolume(height, radius) :
    volume = (radius**2)*height*(math.pi)
    return volume

x = getCylinderVolume(((float(input("What is the height of the cylinder? ")))), (float(input("what is the radius of the cylinder?" ))))
print("The volume of the cylinder is:", x)

def getNumberOfSlices(radius, height, volumeOfSlice):
    volume = getCylinderVolume(height, radius)
    numberOfSlices = volume/volumeOfSlice
    return numberOfSlices

numberOfSlices1 = getNumberOfSlices(((float(input("What is the height of the cylinder? ")))), ((float(input("what is the radius of the cylinder?" )))), (float(input("What is the volume of each slice?"))))
print("The number of slices of of that volume is:", numberOfSlices1)



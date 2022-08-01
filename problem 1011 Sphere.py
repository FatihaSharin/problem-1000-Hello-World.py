def i(R):
  return (4/3)*3.14159*R**3
  
radius=int(input())

VOLUME=i(radius)
VOLUME=round(VOLUME,3)

print("VOLUME = {}".format(VOLUME))

from pythagoreon import arithmeticMean, geometricMean, harmonicMean

print(round(arithmeticMean(1,2,3,4),5))
print(round(arithmeticMean(-3,-2,-1,0,1,2,3),5))
print(round(arithmeticMean(2,4,6,8,10,12),5))
print(round(arithmeticMean(1,5,7,6,-9),5))

print("\n")

print(round(geometricMean(1,2,3,4),5))
print(round(geometricMean(-3,-2,-1,0,1,2,3),5))
print(round(geometricMean(2,4,6,8,10,12),5))
print(round(geometricMean(1,5,7,6,-9),5))
print("\n")


print(round(harmonicMean(1,2,3,4),5))
print(round(harmonicMean(-3,-2,-1,1,2,3,7),5))
print(round(harmonicMean(2,4,6,8,10,12),5))
print(round(harmonicMean(1,5,7,6,-9),5))
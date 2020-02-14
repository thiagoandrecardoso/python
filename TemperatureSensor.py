import statistics

temperatures_C = [33, 66, 65, 0, 59, 60, 62, 64, 70, 76, 80, 81, 80, 83, 90, 79, 61, 53, 50, 49, 53, 48, 45, 39]

temperatures_C_min = min(temperatures_C)
temperatures_C_max = max(temperatures_C)

listTempBigger70 = []
tempBigger80 = 0
for temperature in temperatures_C:
    if temperature >= 70:
        listTempBigger70.append(temperature)
    if temperature > 80:
        tempBigger80 += 1

temperatures_C_mean = statistics.mean(temperatures_C)

temperatures_C[3] = temperatures_C_mean

temperatures_F = []

for C in temperatures_C:
    temperatures_F.append(1.8 * C + 32)

# Decision
if len(listTempBigger70) > 4 or tempBigger80 > 0 or temperatures_C_mean > 65:
    print("system needs change")
else:
    print("system does not need alteration")

listHourTemperatureBigger70 = []
for i in range(len(temperatures_C)):
    if temperatures_C[i] >= 70:
        listHourTemperatureBigger70.append(i)
        # 0 hours

print(listHourTemperatureBigger70)

consecutive = 0
for i in range(len(listHourTemperatureBigger70) - 1):
    if listHourTemperatureBigger70[i] + 1 == listHourTemperatureBigger70[i + 1]:
        consecutive += 1
    else:
        consecutive = 0
if consecutive > 4:
    print("has more than 4 consecutive hours")

temperatures_F_mean = statistics.mean(temperatures_F)

if temperatures_C_mean > temperatures_F_mean:
    print("temperatures C mean bigger temperatures F mean")
elif temperatures_C_mean < temperatures_F_mean:
    print("temperatures C mean smaller temperatures F mean")
else:
    print("temperatures C mean equal temperatures F mean")

standardDeviationC = statistics.pstdev(temperatures_C)
standardDeviationF = statistics.pstdev(temperatures_F)

if standardDeviationC > standardDeviationF:
    print("standardDeviationC > standardDeviationF")
elif standardDeviationC < standardDeviationF:
    print("standardDeviationC < standardDeviationF")
else:
    print("standardDeviationC = standardDeviationF")

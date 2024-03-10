name1 = "Seham"
hieght_m1 = 160
weight_kg1 = 47

name2 = "Alya"
hieght_m2 = 159
weight_kg2 = 54

name3 = "Shatha"
hieght_m3 = 157
weight_kg3= 46

def bmi_calculator(name,height_m, weight_kg):
    bmi = weight_kg / (height_m)**2
    print("bmi:" , bmi)
    if bmi <25:
        return name + "  ,is not over weight"
    else:
        return name + " ,is over weight"
result1 = bmi_calculator(name1,hieght_m1, weight_kg1)
result2 = bmi_calculator(name2,hieght_m2,weight_kg2)
result3 = bmi_calculator(name3,hieght_m3 ,weight_kg3)
print(result1)
print(result2)
print(result3)

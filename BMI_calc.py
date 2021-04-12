import json

f = open('input.json',)
pairs = json.load(f)
count = 0
for dict_ in pairs:
    HeightCm = dict_['HeightCm']
    height_meter = HeightCm/100
    WeightKg = dict_['WeightKg']
    BMI_score= WeightKg/(height_meter**2)
    dict_.update({"BMI_Score":BMI_score})
    if BMI_score <= 18.4:
        dict_.update({"BMI_Category ":"Underweight"})
        dict_.update({"Health_risk ":"Malnutrition risk"})
    elif BMI_score >=18.5 and BMI_score <=24.9:
        dict_.update({"BMI_Category ":"Normal weight"})
        dict_.update({"Health_risk ":"Low risk"})
    elif BMI_score >=25  and BMI_score <=29.9:
        dict_.update({"BMI_Category ":"Overweight"})
        dict_.update({"Health_risk ":"Enhanced risk"})
        count = count +1
    elif BMI_score >=30  and BMI_score <=34.9:
        dict_.update({"BMI_Category ":"Moderately obese"})
        dict_.update({"Health_risk ":"Medium risk"})
    elif BMI_score >=35   and BMI_score <=39.9:
        dict_.update({"BMI_Category ":"Severely obese"})
        dict_.update({"Health_risk ":"High risk"})
    else:
        dict_.update({"BMI_Category ":"Very severely obese"})
        dict_.update({"Health_risk ":"Very high risk"})

print ("\n Json output:-  {} \n".format(pairs))
print ("\n Total number of Overweight peoples are :- {}".format(count))

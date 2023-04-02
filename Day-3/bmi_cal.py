print("=====BMI CALCULATOR=====")

weight = float(input("Enter your weight[in Kg]: "))
ht = float(input("Enter your height[in cm]: "))
height = ht/100

bmi = int(weight/(height)**2)

bmi_round = round(bmi, 1)

print("==========================")
print(f"Your BMI value is {bmi_round}! ")
print("==========================")
if bmi_round <= 16.0:
    print("Remarks: Underweight (Severe thinness)")

elif 16.0 < bmi_round <= 16.9:
    print("Remarks: Underweight (Moderate thinness)")

elif 17 <= bmi_round <= 18.4:
    print("Remarks: Underweight (Mild thinness)")

elif 18.5 <= bmi_round <= 24.9:
    print("Remarks: Normal range")

elif 25 <= bmi_round <= 29.9:
    print("Remarks: Overweight (Pre-obese)")

elif 30 <= bmi_round <= 34.9:
    print("Remarks: Obese (Class I)")

elif 35 <= bmi_round <= 39.9:
    print("Remarks: Obese (Class II)")

elif bmi_round >= 40:
    print("Remarks: Obese (Class III)")

print("==========================")


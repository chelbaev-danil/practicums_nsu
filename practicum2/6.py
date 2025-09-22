LBS_TO_KG = 0.453592
INCHES_TO_METERS = 0.0254

weight = int(input())
height = int(input())

weight_kg = LBS_TO_KG*weight
height_m = INCHES_TO_METERS*height

bmi = weight_kg / (height_m**2)

print(f"{bmi:.2f}")
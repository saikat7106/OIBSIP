height = float(input('enter the height in m: '))
weight = float(input('enter the weight in kg: '))

the_BMI=weight/(height)**2

print(('your body mass index is: ',the_BMI))

if (the_BMI<15):
    print('oh my god!you are severly underweight.please take well care and visit a doctor')

elif(the_BMI>=15 and the_BMI<18.5):
    print('oops!you are underweight.please take care of yourself')

elif(the_BMI>=18.5 and the_BMI<25):
    print('congratulations!you are completely healthy')

elif(the_BMI>=25 and the_BMI<30):
    print('Eeee!you are overweight')

elif(the_BMI>=30):
    print('shees!you are obese')
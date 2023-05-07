#!/usr/bin/env python
# coding: utf-8


name = input("Enter your name")

weight = float(input("Enter your weight in Kg: "))

height = float(input("Enter your height in meter: "))

bmi = weight / (height**2)

print(f'Your BMI is {bmi}')

if bmi>0:
    if bmi<18.5:
        print(name + ', you are underweight')
    elif bmi<=24.9:
        print(name + ', you have normal BMI')
    elif bmi<=29.9:
        print(name +' ,you are Overweight')
    elif bmi<=34.9:
        print(name + ', you are obese')
    elif bmi<=39.9:
        print(name + ', you are severely obese')
    else:
        print(name + ', you are morebidly obese')
else:
    print('Enter a valid input')






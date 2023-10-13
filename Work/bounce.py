# bounce.py
#
# Exercise 1.5

height = 100
bounce_back = height * 0.6
bounce_count = 1

while bounce_count < 11:
    print(bounce_count, round(bounce_back, 4))
    bounce_count = bounce_count + 1
    bounce_back = bounce_back * 0.6




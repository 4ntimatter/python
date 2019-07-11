input = open('input_nums.txt')
text = input.read()
input.close()
input_list = text.split(",")
number_of_numbers=len(input_list)
for i in range(0, number_of_numbers):
    a=input_list[i]
    input_list[i] = float(a)

duration=[]
for i in range(1,number_of_numbers):
    a = input_list[i]
    b = input_list[i-1]
    c = a-b
    duration.append(c)

print(duration)
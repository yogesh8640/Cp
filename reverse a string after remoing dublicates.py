input_str=input()
output_str=""

for i in input_str:
    if i not in output_str:
        output_str+=i
print(output_str[::-1])

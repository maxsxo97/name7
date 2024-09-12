num = 1210
num_str = str(num)
count_dict = {}
for char in num_str:
    if char in count_dict:
        count_dict[char] += 1
    else:
        count_dict[char] = 1
for key, value in count_dict.items():
    print(f"{key} = {value}")

blood_type = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']

result_A = 0
result_B = 0
result_O = 0
result_AB = 0

for i in blood_type:
    if i == 'A':
        result_A += 1
    elif i == 'B':
        result_B += 1
    elif i == 'O':
        result_O += 1
    else:
        result_AB += 1

blood_dic = {
    'A': (result_A),
    'O': (result_O),
    'B': (result_B),
    'AB': (result_AB)
    }

print(blood_dic)

# # 강사님 풀이
blood_list = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']

blood_dict = {
    'A': 0,
    'B': 0,
    'C': 0,
    'AB': 0,
}

for blood in blood_list:
    blood_dict[blood] += 1
    
print(blood_dict)


###################
location_list = ['서울', '부산', '부산', '서울', '대전', '광주', '제주']

location_dict = {

}

for location in location_list:
    if location in location_dict.keys():
        location_dict[location] += 1
    else:
        location_dict[location] = 1

print(location_dict)


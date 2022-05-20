def find_distance_hamming(data_1, data_2):
    data_1 = bin(int(data_1)).split("b")[1]
    data_2 = bin(int(data_2)).split("b")[1]

    if len(data_1) < 8:
        data_1 = ("0" * (8 - len(data_1))) + data_1
    if len(data_2) < 8:
        data_2 = ("0" * (8 - len(data_2))) + data_2

    res = 0
    for i in range(0, len(data_1), 1):
        if data_1[i] != data_2[i]:
            res += 1

    return res


file_in = open("input2.dat")

data = dict()

for line in file_in.readlines():
    key_value = line.split(" ")
    data[key_value[0]] = key_value[1].split("\n")[0]

file_in.close()
# print(data)

distances = dict()

for first_key in data:
    distances[first_key] = dict()
    for second_key in data:
        if first_key != second_key:
            distances[first_key][second_key] = find_distance_hamming(data[first_key], data[second_key])

# print('distances', distances)

min_distances_letter = dict()
for first_key in distances:
    min_distances_letter[first_key] = ["", 8, 1]
    for second_key in distances[first_key]:
        if distances[first_key][second_key] < min_distances_letter[first_key][1]:
            min_distances_letter[first_key][0] = second_key
            min_distances_letter[first_key][1] = distances[first_key][second_key]
            min_distances_letter[first_key][2] = 1
        elif distances[first_key][second_key] == min_distances_letter[first_key][1]:
            min_distances_letter[first_key][0] += second_key
            min_distances_letter[first_key][2] += 1

# print(min_distances_letter)

min_dist = 10
elem_key = ""

for key in min_distances_letter:
    if min_distances_letter[key][1] < min_dist:
        min_dist = min_distances_letter[key][1]
        elem_key = key

# print(elem_key)

bin_str = ''
c = 0
for i in range(-1, -9, -1):
    c0 = 0
    c1 = 0
    for j in data.keys():
        string = bin(int(data[j]))[2:]
        string = '0' * (8 - len(string)) + string
        if string[i] == '0':
            c0 += 1
        else:
            c1 += 1
    if c0 > c1:
        bin_str += '1'
    elif c0 == c1:
        bin_str += '?'
    else:
        bin_str += '0'


file = open('output.dat', 'w')
file.write(elem_key)
file.write('\n')
bin_str = bin_str[::-1]
n = 2 ** bin_str.count('?')
max_distance = 0
for i in range(n):
    binary = bin(i).split('b')[1]
    binary = '0' * (bin_str.count('?') - len(binary)) + binary
    index = 0
    string = ''
    for c in bin_str:
        if c == '?':
            string += binary[index]
            index += 1
        else:
            string += c
    file.write(str(int('0b' + string, 2)))
    file.write('\n')
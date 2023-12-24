import statistics

with open('matrix.txt', 'r') as file:
    lines = file.read().splitlines()
    tuples = [tuple(line.split(' ')) for line in lines]

print("tuples:", tuples)

new_tuples = [[values[i] for values in tuples] for i in range(len(tuples[0]))]

new_list = []
for sublist in new_tuples:
    sublist_values = []
    for value in sublist:
        #print(value)
        if value.startswith('*') and value.endswith('*'):
            #delete value from tuples
            sublist.remove(value)
            value = value.strip('*')
            if value:
                sublist_values.append(value)
    new_list.append(sublist_values)

print("-------------------------")
filtered_tuples = []
for sublist in new_tuples:
    filtered_sublist = []
    for value in sublist:
        if value not in ("*1*", "*2*", "*3*", "*4*", "*5*", "*6*", "*7*", "*8*", "*9*", "*10*"):
            value = value.replace('*', '')
            filtered_sublist.append(value)
    filtered_tuples.append(filtered_sublist)

print("\nnew_tuples:", filtered_tuples)
print("\nnew_list:", new_list)


remainder_list = []
previous_remainder = None

for sublist, div_list in zip(filtered_tuples, new_list):
    #print(sublist)
    if div_list:
        div_value = None
        for value in div_list:
            if not (value.startswith('*') and value.endswith('*')):
                try:
                    div_value = float(value)
                    break
                except ValueError:
                    pass

        if div_value is not None:
            sublist_remainders = []

            if previous_remainder is not None:
                for i in range(len(sublist)):
                    if not (sublist[i].startswith('*') and sublist[i].endswith('*')):
                        try:
                            sublist[i] = float(sublist[i]) + previous_remainder
                        except ValueError:
                            pass

            for value in sublist:
                #print("hello:", value)

                value = float(value)
                remainder = value % div_value
                sublist_remainders.append(remainder)


            if sublist_remainders:
                most_frequent_remainder = statistics.mode(sublist_remainders)
                remainder_list.append(most_frequent_remainder)
                previous_remainder = most_frequent_remainder

print("\nremainder_list:", remainder_list)
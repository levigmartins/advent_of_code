f = open("inputs/3_input.txt", "r");

# part 1
rucksacks = [];
common_values = [];
total = 0;

for x in f:
    first_compartment = x[0:int((len(x.strip()))/2)];
    second_compartment = x[int((len(x.strip())/2)):int(len(x.strip()))];

    rucksacks.append((first_compartment, second_compartment));

for x in rucksacks:
    first = x[0];
    second = x[1];

    # turn set of intersection into list and retrieve the value
    common_values.append(list(set(first) & set(second))[0]);

for x in common_values:
    if x.isupper():
        total += (ord(x)-38);
    else:
        total += (ord(x)-96);

print(total);

# part 2
groups_rucksacks = [];
common_values_part_2 = [];
total = 0;

f.seek(0);

for x in f:
    groups_rucksacks.append(x.strip());

i = 0

while i < len(groups_rucksacks):
    if i == len(groups_rucksacks) - 2 :
        break;

    common_values_part_2.append(list(set(groups_rucksacks[i]) & set(groups_rucksacks[i+1]) & set(groups_rucksacks[i+2]))[0]);
    i += 3;

for x in common_values_part_2:
    if x.isupper():
        total += (ord(x)-38);
    else:
        total += (ord(x)-96);

print(total);


f.close();
f = open("inputs/1_input.txt", "r");

count = 0;
array = [0]

# Input reading line by line
for x in f:
    if x == '\n':
        count += 1;
        array.append(0);
    else:
        array[count] = array[count] + int(x);

f.close();

# part 1
answer = max(array);
print(answer);

# part 2
sorted_array = sorted(array, key=int, reverse=True);
answer_part_2 = sorted_array[0] + sorted_array[1] + sorted_array[2];
print(answer_part_2);
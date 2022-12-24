f = open("inputs/2_input.txt", "r");

# part 1
total_score = 0;
aux = 0;

for x in f:

    match x[2]:

        case 'X':
            match x[0]:
                case 'A':
                    aux = 3;
                case 'B':
                    aux = 0;
                case 'C':
                    aux = 6;
            total_score += (1+aux);

        case 'Y':
            match x[0]:
                case 'A':
                    aux = 6;
                case 'B':
                    aux = 3;
                case 'C':
                    aux = 0;
            total_score += (2+aux);

        case 'Z':
            match x[0]:
                case 'A':
                    aux = 0;
                case 'B':
                    aux = 6;
                case 'C':
                    aux = 3;
            total_score += (3+aux);

print(total_score);

# part 2
total_score_part_2 = 0;
aux = 0;

f.seek(0); # reset iterator to the top of the file

for x in f:

    match x[2]:

        case 'X':
            match x[0]:
                case 'A':
                    aux = 3;
                case 'B':
                    aux = 1;
                case 'C':
                    aux = 2;
            total_score_part_2 += (0+aux);

        case 'Y':
            match x[0]:
                case 'A':
                    aux = 1;
                case 'B':
                    aux = 2;
                case 'C':
                    aux = 3;
            total_score_part_2 += (3+aux);

        case 'Z':
            match x[0]:
                case 'A':
                    aux = 2;
                case 'B':
                    aux = 3;
                case 'C':
                    aux = 1;
            total_score_part_2 += (6+aux);

print(total_score_part_2);

f.close();
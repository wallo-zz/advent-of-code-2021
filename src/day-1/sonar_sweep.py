with open("input.txt", "r") as sonar_data_file:
    sonar_data = sonar_data_file.readlines()

# Part One
deeper = 0
for index in range(1, len(sonar_data) ):
    if int(sonar_data[index]) - int(sonar_data[index - 1]) > 0:
        deeper += 1
        
print("There are {} measurements larger than the previous one!".format(deeper))

# Part Two
compound_sonar_data = [int(a) + int(b) + int(c) for a, b, c in zip ( \
    [0, 0, *sonar_data], \
    [0, *sonar_data, 0], \
    [*sonar_data, 0, 0] \
)][2:-2]

compound_deeper=0

for index in range(1, len(compound_sonar_data) ):
    if int(compound_sonar_data[index]) - int(compound_sonar_data[index - 1]) > 0:
        compound_deeper += 1

print("There are {} compounded measurements larger than the previous one!".format(compound_deeper))

with open("input.txt", "r") as sonar_data_file:
    sonar_data = sonar_data_file.readlines()

# Part One
deeper = 0
for index in range(1, len(sonar_data) ):
    if int(sonar_data[index]) - int(sonar_data[index - 1]) > 0:
        deeper += 1
        
print("There are {} measurements larger than the previous one!".format(deeper))


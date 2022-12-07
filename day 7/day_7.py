#Part 1
import math


class folder:
    def __init__(self, name):
        self.name = name
        self.subfolders = []
        self.files = []
        self.previous_folder = None
    def add_subfolder(self, subfolder):
        if subfolder not in self.subfolders:
            self.subfolders.append(subfolder)
    def add_file(self, file, size):
        if [file,size] not in self.files:
            self.files.append([file, int(size)])
    def get_subfolder(self, name):
        for subfolder in self.subfolders:
            if subfolder.name == name:
                return subfolder
    def get_file(self, name):
        for file in self.files:
            if file.name == name:
                return file
    def get_subfolders(self):
        return self.subfolders
    def get_files(self):
        return self.files
    def get_name(self):
        return self.name
    def get_objective_part1(self, threshold_folder_size=0):
        total_size = 0
        for file in self.files:
            total_size += file[1]
        for subfolder in self.subfolders:
            folder_size, threshold_folder_size = subfolder.get_objective_part1(threshold_folder_size)
            if folder_size < 100000:
                threshold_folder_size += folder_size
            total_size += folder_size
        return total_size, threshold_folder_size

    def get_objective_part2(self, threshold, lowest_folder_size=math.inf):
        total_size = 0
        for file in self.files:
            total_size += file[1]
        for subfolder in self.subfolders:
            folder_size, lowest_folder_size = subfolder.get_objective_part2(lowest_folder_size)
            if folder_size > threshold and folder_size < lowest_folder_size:
                lowest_folder_size = folder_size
            total_size += folder_size
        return total_size, lowest_folder_size

with open('test.txt') as f:
    #building the system
    lines = f.readlines()
    initial_folder = folder('/')
    position = initial_folder
    i = 1
    while i < len(lines):
        print(i,"/",len(lines))
        line = lines[i]
        if line[2] == "c":
            if line[5:7] == "..":
                position = position.previous_folder
            else:
                position = position.get_subfolder(line[5:-1])
            i += 1
        elif line[2] == "l":
            i += 1
            line = lines[i]
            while line[0] != "$":
                if line[0] == "d":
                    subfolder = folder(line[4:-1])
                    subfolder.previous_folder = position
                    position.add_subfolder(subfolder)
                else:
                    size, file = line.split(" ")
                    position.add_file(file[:-1], size)
                i += 1
                if i == len(lines):
                    break
                line = lines[i]
    total_size, part1_answer = initial_folder.get_objective_part1()
    print("Part 1:", part1_answer)
    threshold = 70000000 - total_size
    print("Part 2:", initial_folder.get_objective_part2(threshold=threshold))



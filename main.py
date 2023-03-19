
# wczytanie danych treningowych
training_set = []

with open("iris_training.txt", 'r') as file:
    lines = file.readlines()

for line in lines:
    items = line.strip().replace('\t', '').replace(',', '.').split()
    if not items[0].isalpha():
        training_set.append([float(x) for x in items[0:4]])

for row in training_set:
    print(row)
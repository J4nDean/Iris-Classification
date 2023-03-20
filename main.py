
# funckcja zwracająca dystans pomiędzy punktami ze wzrou Eyklidesa;
def euclideans(x, y):
    dist = 0.0
    for i in range(len(x)):
        dist += (x[i] - y[i])**2
    return dist**0.5

def closestNeighbors(training_data, test_data, k):
    distances = []
    for i in range(len(training_data)):
        dist = euclideans(test_data, training_data[i])
        distances.append((training_data[i]), dist)
    distances.sort(key=lambda x :x[i])
    neighbors = []
    for i in range(k):
        neighbors.append(distances[i][0])
    return neighbors


# funkcja wczytująca dane z pliku tekstowego
def loadFile(filename):
    dataset = []
    with open(filename) as file:
        for line in file:
            items = line.strip().replace('\t', '').replace(',', '.').split()
            if not items[0].isalpha():
                dataset.append([float(x) for x in items[0:4]])
    return dataset

# wczytanie danych treningowych i testowych
training_data = loadFile('iris_training.txt')
test_data = loadFile('iris_test.txt')

k = int(input("Podaj liczbe sasiadow k: "))

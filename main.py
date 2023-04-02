# funkcja obliczająca odległość euklidesową między dwoma wektorami
def euclidean_distance(x, y):
    distance = 0.0
    for i in range(len(x)):
        distance += (x[i] - y[i]) ** 2
    return distance ** 0.5


# Funkcja klasyfikująca przykład na podstawie k-NN
def classify_example(test_data, training_data, k):
    correct = 0
    for example in test_data:
        distances = []
        for row in training_data:
            # extract numerical attributes from row
            x = [float(attr) for attr in row[:-1]]
            y = [float(attr) for attr in example[:-1]]
            dist = euclidean_distance(x, y)
            distances.append((row, dist))
        distances.sort(key=lambda x: x[1])
        neighbors = [row for row, dist in distances[:k]]
        result = get_majority_class(neighbors)
        if result == example[-1]:
            correct += 1
    accuracy = (correct / len(test_data)) * 100.0
    print(f"Accuracy: {accuracy:.2f}% ({correct}/{len(test_data)})")


# Funkcja zwracająca klasę, do której należy większość sąsiadów
def get_majority_class(neighbors):
    classes = {}
    for neighbor in neighbors:
        response = neighbor[-1]
        if response in classes:
            classes[response] += 1
        else:
            classes[response] = 1
    sorted_classes = sorted(classes.items(), key=lambda x: x[1], reverse=True)
    return sorted_classes[0][0]


def load(filename):
    dataset = []
    with open(filename) as file:
        for line in file:
            items = line.strip().replace('\t', '').replace(',', '.').split()
            if not items[0].isalpha():
                dataset.append([float(x) for x in items[0:4]])
    return dataset


# przykładowe użycie
while True:
    training_data = load('iris_training.txt')
    test_data = load('iris_test.txt')
    k = int(input("Podaj wartość parametru k: "))
    classify_example(test_data, training_data, k)

# funckcja zwracająca dystans pomiędzy punktami ze wzrou Eyklidesa;
def euclideans_distance(x, y):
    distance = 0.0
    for i in range(len(x)):
        distance += (x[i] - y[i])**2
    return distance**0.5

def predict(training_data, test_data, k):
    disances = []
    #for i in range(len(training_data)):



# funkcja wczytująca dane z pliku tekstowego
def load_data(filename):
    dataset = []
    with open(filename) as file:
        for line in file:
            items = line.strip().replace('\t', '').replace(',', '.').split()
            if not items[0].isalpha():
                dataset.append([float(x) for x in items[0:4]])
    return dataset

# wczytanie danych treningowych i testowych
training_data = load_data('iris_training.txt')
test_data = load_data('iris_test.txt')

for i in test_data:
    print(i)
import random
import pickle
# Создание data-set
with open('dataset_6000000.pickle', 'wb') as file:
    n = int(input())
    test_list = [random.randint(-1000, 1000) for x in range(n)]
    pickle.dump(test_list, file)
    print(len(test_list))



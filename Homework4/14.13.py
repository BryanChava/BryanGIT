#BRYAN CHAVARRIA
#1657040

num_calls = 0

def partition(user_ids, i, k):
    j = i - 1
    pivot = user_ids[k]
    for x in range(i, k):
        if (user_ids[x] <= pivot):
            j = j + 1
            user_ids[j], user_ids[x] = user_ids[x], user_ids[j]
    user_ids[j + 1], user_ids[k] = user_ids[k], user_ids[j + 1]
    return (i + 1)

def quicksort(user_ids, i, k):
    global num_calls

    num_calls = num_calls + 1
    if (i < k):
        par = partition(user_ids, i, k)

        quicksort(user_ids, i, par - 1)
        quicksort(user_ids, par + 1, k)
if __name__ == "__main__":
    user_ids = []
    user_id = input()
    while user_id != "-1":
        user_ids.append(user_id)
        user_id = input()
    quicksort(user_ids, 0, len(user_ids) - 1)

    print(num_calls)
    for user_id in user_ids:
        print(user_id)
def frequencyCount(arr):
    n =len(arr)
    counter_dict={}
    for i in range(n):
        counter_dict[i+1] =0

    for num in arr:
        counter_dict[num] +=1

    res =[]

    for key,val in counter_dict.items():
        res.append(val)

    return res

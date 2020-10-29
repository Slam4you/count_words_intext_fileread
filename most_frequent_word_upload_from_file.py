dic = {}
with open(r"C:\Users\Slam\Documents\dataset_3363_3.txt") as inf:
    for line in inf:
        line = line.lower().strip().split(' ')
        print(line)
        for i in range(len(line)):
            if line[i] not in dic:
                dic[line[i]] = 1
            else:
                dic[line[i]] += 1
max_val = max(dic.values())
all_val_dic = {k: v for k, v in dic.items() if v == max_val}
for key, value in all_val_dic.items():
    print(key, value)

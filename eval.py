def p_r_f_strict(gold,test):
    g_num = len(gold)
    true_num = 0
    test_num = len(test)
    for i in range(len(gold)):
        if gold[i] in test:
            true_num+= 1
    if g_num == 0:
        recall = 0
    else:
        recall = true_num/g_num
    if test_num>0:
        precision = true_num/test_num
    else:
        precision = 0
    if recall == 0 and precision == 0:
        f1= 0
    else:
        f1 = 2*precision*recall/(precision+recall)
    return precision, recall, f1
    
def p_r_f_lenient(gold,test):
    g_num = len(gold)
    true_num = 0
    test_num = len(test)
    for i in range(len(gold)):
        for t in test:
            if (gold[i][0]<= t[0] and t[0] <= gold[i][1]) or (gold[i][0]<= t[1] and t[1] <= gold[i][1]) or (t[0] <= gold[i][0] and gold[i][1]<= t[1]):
                true_num += 1
                break
    recall = true_num/g_num
    if test_num>0:
        precision = true_num/test_num
    else:
        precision = 0
    if recall == 0 and precision == 0:
        f1= 0
    else:
        f1 = 2*precision*recall/(precision+recall)
    return precision, recall, f1

if __name__ == "__main__":
    import pandas as pd
    file = pd.read_csv(r"label_test2.txt", sep='\t', engine="python", error_bad_lines=False, encoding='utf-8', header=None)
    predict = file.iloc[:, 1].tolist()
    truth = file.iloc[:, 2].tolist()
    
    p_r_f_lenient(truth, predict)
    
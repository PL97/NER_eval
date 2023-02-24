from nereval.ner_metrics import classifcation_report


if __name__ == "__main__":
    test_from_file = False
    if test_from_file:
        y_pred, y_true = [], []
        with open(r"label_test2.txt",'r') as f:
            for line in f.readlines():
                line = re.sub("\n", "", line).split("\t")
                predict.append(line[2])
                truth.append(line[1])
        
        metrics = classifcation_report(y_true, y_pred)
        import json
        with open('evaluation.json', 'w') as f:
            json.dump(metrics, f)
        # ctrl + shift + I for better display on vscode
    else:
        y_true = ['B-PER', 'I-PER', 'O', 'B-ORG', 'B-ORG', 'O', 'O', 'B-PER', 'I-PER', 'O']
        y_pred = ['O', 'B-PER', 'O', 'B-ORG', 'B-ORG', 'I-ORG', 'O', 'B-PER', 'I-PER', 'O']
        metrics = classifcation_report(y_true, y_pred)

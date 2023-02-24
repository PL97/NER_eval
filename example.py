from nereval.ner_metrics import classifcation_report


if __name__ == "__main__":
    y_true = ['B-PER', 'I-PER', 'O', 'B-ORG', 'B-ORG', 'O', 'O', 'B-PER', 'I-PER', 'O']
    y_pred = ['O', 'B-PER', 'O', 'B-ORG', 'B-ORG', 'I-ORG', 'O', 'B-PER', 'I-PER', 'O']
    metrics = classifcation_report(y_true, y_pred, mode='lenient')
    metrics = classifcation_report(y_true, y_pred, mode='strict')

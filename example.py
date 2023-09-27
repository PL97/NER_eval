from ner_metrics.ner_metrics import classification_report


if __name__ == "__main__":
    y_true = ['B-PER', 'I-PER', 'O', 'B-ORG', 'B-ORG', 'O', 'O', 'B-PER', 'I-PER', 'O']
    y_pred = ['O', 'B-PER', 'O', 'B-ORG', 'B-ORG', 'I-ORG', 'O', 'B-PER', 'I-PER', 'O']
    
    
    ## output as a json file
    # metrics = classifcation_report(y_true, y_pred, mode='lenient')
    metrics = classification_report(y_true, y_pred, mode='strict', verbose=True)
    
    import json
    # Serializing json
    json_object = json.dumps(metrics, indent=4)
    
    # Writing to sample.json
    with open("evaluation.json", "w") as outfile:
        outfile.write(json_object)

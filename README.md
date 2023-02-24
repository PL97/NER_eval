## NER_eval

An simple implementation of strict/lenient matching to evaluate NER performance (precision, recall, F1-score) within 60 lines!

This script currently only supports IOB2 format with both strict and lenient mode.


## Usage

```python
from ner_metrics import classication_report

y_true = [['B-PER', 'I-PER', 'O', 'B-ORG', 'B-ORG', 'O', 'O', 'B-PER', 'I-PER', 'O']]
y_pred = ['O', 'B-PER', 'O', 'B-ORG', 'B-ORG', 'I-ORG', 'O', 'B-PER', 'I-PER', 'O']
classifcation_report(tags_true=y_true, tags_pred=y_pred, mode="lenient") # for lenient match

classifcation_report(tags_true=y_true, tags_pred=y_pred, mode="strict") # for strict match

```
Expected output
```
tag(lenient): PER        precision:0.5   recall:0.5      f1-score:0.5
tag(strict): PER         precision:0.5   recall:0.5      f1-score:0.5
tag(lenient): ORG        precision:1.0   recall:1.0      f1-score:1.0
tag(strict): ORG         precision:0.5   recall:0.5      f1-score:0.5
```

*results is also saved in evaluation.json*

## How to cite this work

If you find this gitr epo useful, please consider citing it using the snippet below:
```bibtex
@misc{ner_eval,
    author={Le Peng},
    title={ner_eval: A Simple Python Snippets for NER Evaluation},
    howpublished={\url{https://github.com/PL97/federated-multi-modality-learning}},
    year={2022}
}
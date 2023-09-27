## NER_eval
A simple implementation of strict/lenient matching to evaluate NER performance (precision, recall, F1-score) in 60 lines!

This script currently only supports the IOB2 format with both strict and lenient modes.

## Installation
```bash
pip install ner_metrics
```
or
```bash
pip install git+https://github.com/PL97/NER_eval.git
```


## Usage

```python
from ner_metrics import classification_report

y_true = ['B-PER', 'I-PER', 'O', 'B-ORG', 'B-ORG', 'O', 'O', 'B-PER', 'I-PER', 'O']
y_pred = ['O', 'B-PER', 'O', 'B-ORG', 'B-ORG', 'I-ORG', 'O', 'B-PER', 'I-PER', 'O']
classification_report(tags_true=y_true, tags_pred=y_pred, mode="lenient") # for lenient match

classification_report(tags_true=y_true, tags_pred=y_pred, mode="strict") # for strict match

```
Expected output
```
tag(lenient): PER        precision:1.0   recall:1.0      f1-score:1.0
tag(strict): PER         precision:0.5   recall:0.5      f1-score:0.5
tag(lenient): ORG        precision:1.0   recall:1.0      f1-score:1.0
tag(strict): ORG         precision:0.5   recall:0.5      f1-score:0.5
```
The results are also saved to *evaluation.json*

## How to cite this work

If you find this git repo useful, please consider citing it using the snippet below:
```bibtex
@misc{ner_eval,
    author={Le Peng},
    title={ner_metrics: A Simple Python Snippets for NER Evaluation},
    howpublished={\url{https://github.com/PL97/NER_eval}},
    year={2022}
}

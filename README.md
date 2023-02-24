## NER_eval
___

An simple implementation of strict/lenient matching to evaluate NER performance (precision, recall, F1-score) within 60 lines!

This script currently only supports IOB2 format with both strict and lenient mode.


## Usage
___

```python
from ner_metrics import classication_report

classifcation_report(tags_true=y_true, tags_pred=y_pred, mode="lenient") # for lenient match

classifcation_report(tags_true=y_true, tags_pred=y_pred, mode="strict") # for strict match

```

## How to cite this work
___

If you find this gitr epo useful, please consider citing it using the snippet below:
```bibtex
@misc{ner_eval,
    author={Le Peng},
    title={ner_eval: A Simple Python Snippets for NER Evaluation},
    howpublished={\url{https://github.com/PL97/federated-multi-modality-learning}},
    year={2022}
}
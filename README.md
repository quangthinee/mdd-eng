# English Mispronunciation Detection and Diagnosis (MDD)
This repository contains the source code for building a model tackling the task of MDD in English. Before creating, training for infering the model, some prerequisites need to be satisfied.
## Prerequisites
### System
1. **Python**: 3.10.10.
2. **OS**:  Ubuntu 22.04.2 LTS.
3. **Kaldi**.

### Python packages
All the needed packages are listed in `requirements.txt`, run this command to start installing all the important packages:
```
pip install -r requirements.txt
```

## Repo Structure
```
|-- README.md
|-- code-test
|   |-- config.yaml
|   `-- test.ipynb
|-- crnn-ctc
|   |-- config
|   |   |-- fbank.conf
|   |   `-- mfcc.conf
|   |-- model
|   |   `-- crnn-ctc.py
|   |-- scripts
|   |   |-- make_feats.sh
|   |   `-- path.sh
|   `-- utils
|       |-- l2_prep.py
|       `-- modelling_units.py
`-- requirements.txt
```

## Further description
Updating

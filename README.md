# Drug-Target-Integration

![alt text](https://thumb.tildacdn.com/tild3332-3535-4761-b562-373639353431/-/format/webp/noroot.png)

Discovering a new drug to market is a complex and resource-consuming process that can cost pharmaceutical companies an average of $2.6 billion and up to a decade of research and development.

## **This is where AI comes in** 

Machine learning models that can accurately predict affinities can not only save pharmaceutical research costs on reducing the amount of high-throughput screening, but also to enlarge the search space and avoid missing potential candidates.

In this project, the activity of a small-molecule drug is measured by its **binding affinity** with the target protein. The Drug field is in SMILES (Simplified Molecular Input Line Entry System) format and Target field comprises of sequence of amino acids. The amino acids are defined by english alphabet characters. 

![alt text](https://i0.wp.com/www.compoundchem.com/wp-content/uploads/2014/09/20-Common-Amino-Acids-v3.png?ssl=1)

## DeepPurpose Library
A Deep Learning Library for Compound and Protein Modeling DTI.

### Encodings

| Drug Encodings | Description  |
| :---:   | :---: | 
| Transformer | Transformer Encoder on ESPF |

| Target Encodings | Description  |
| :---:   | :---: |
| CNN | Convolutional Neural Network on target seq |

### Data 

| Data | Dataset Description | Task Description |
| :---:   | :---: | :---: | 
| BindingDB | BindingDB is a public, web-accessible database of measured binding affinities, focusing chiefly on the interactions of protein considered to be drug-targets with small, drug-like molecules. | Regression. Given the target amino acid sequence/compound SMILES string, predict their binding affinity. |

## Outcome

Our model predicts binding affinity across a diverse set of drugs and target groups. Drug-target interaction prediction task aims to predict the interaction activity score in silico given only the accessible compound structural information and protein amino acid sequence.


# Antimicrobial class specificity prediction

Prediction of antimicrobial class specificity using simple machine learning methods applied to an antimicrobial knowledge graph. The knowledge graph is built on ChEMBL, Co-ADD and SPARK. Endpoints are broad terms such as activity against gram-positive or gram-negative bacteria. The best model according to the authors is a Random Forest with MHFP6 fingerprints.

This model was incorporated on 2024-12-17.

## Information
### Identifiers
- **Ersilia Identifier:** `eos74km`
- **Slug:** `antimicrobial-kg-ml`

### Domain
- **Task:** `Annotation`
- **Subtask:** `Activity prediction`
- **Biomedical Area:** `Antimicrobial resistance`
- **Target Organism:** `Fungi`, `Fast-acid bacteria`, `Gram-positive bacteria`, `Gram-negative bacteria`
- **Tags:** `Antimicrobial activity`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `5`
- **Output Consistency:** `Fixed`
- **Interpretation:** Class probabilities for each antimicrobial class

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| acid_fast | float | high | Classification score indicating the class probability of inhibiting growth of acid-fast bacteria |
| fungi | float | high | Classification score indicating the class probability of inhibiting growth of fungi |
| gram_negative | float | high | Classification score indicating the class probability of inhibiting growth of gram-negative bacteria |
| gram_positive | float | high | Classification score indicating the class probability of inhibiting growth of gram-positive bacteria |
| inactive | float | high | Classification score indicating the class probability of the compound being inactive in antimicrobial assays |


### Source and Deployment
- **Source:** `Local`
- **Source Type:** `External`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos74km](https://hub.docker.com/r/ersiliaos/eos74km)
- **Docker Architecture:** `AMD64`, `ARM64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos74km.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos74km.zip)

### Resource Consumption


### References
- **Source Code**: [https://github.com/IMI-COMBINE/broad_spectrum_prediction](https://github.com/IMI-COMBINE/broad_spectrum_prediction)
- **Publication**: [https://www.biorxiv.org/content/10.1101/2024.12.02.626313v1.full](https://www.biorxiv.org/content/10.1101/2024.12.02.626313v1.full)
- **Publication Type:** `Preprint`
- **Publication Year:** `2024`
- **Ersilia Contributor:** [miquelduranfrigola](https://github.com/miquelduranfrigola)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [MIT](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos74km
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos74km
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!

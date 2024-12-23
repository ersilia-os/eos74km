# Antimicrobial class specificity prediction

Prediction of antimicrobial class specificity using simple machine learning methods applied to an antimicrobial knowledge graph. The knowledge graph is built on ChEMBL, Co-ADD and SPARK. Endpoints are broad terms such as activity against gram-positive or gram-negative bacteria. The best model according to the authors is a Random Forest with MHFP6 fingerprints.

## Identifiers

* EOS model ID: `eos74km`
* Slug: `antimicrobial-kg-ml`

## Characteristics

* Input: `Compound`
* Input Shape: `Single`
* Task: `Classification`
* Output: `Probability`
* Output Type: `Float`
* Output Shape: `List`
* Interpretation: Class probabilities for each antimicrobial class

## References

* [Publication](https://www.biorxiv.org/content/10.1101/2024.12.02.626313v1.full)
* [Source Code](https://github.com/IMI-COMBINE/broad_spectrum_prediction)
* Ersilia contributor: [miquelduranfrigola](https://github.com/miquelduranfrigola)

## Ersilia model URLs
* [GitHub](https://github.com/ersilia-os/eos74km)
* [AWS S3](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos74km.zip)

## Citation

If you use this model, please cite the [original authors](https://www.biorxiv.org/content/10.1101/2024.12.02.626313v1.full) of the model and the [Ersilia Model Hub](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff).

## License

This package is licensed under a GPL-3.0 license. The model contained within this package is licensed under a MIT license.

Notice: Ersilia grants access to these models 'as is' provided by the original authors, please refer to the original code repository and/or publication if you use the model in your research.

## About Us

The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission!
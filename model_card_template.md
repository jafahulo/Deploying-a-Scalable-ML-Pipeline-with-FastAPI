# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
This is a supervised random forests machine learning model which comes from the scikit-learn library.
## Intended Use
This is intended to classify people between earning more than 50k and less than 50k.
This is intended to be used for educational purposes in an udacity course on machine learning pipelines.
## Training Data
The training data comes from a US Census dataset provided by Udacity. It includes features such as age, working class, education level, race, sex, etc.
It also contains a column on salary which is divided between <=50k and >50k.
## Evaluation Data
To evaluate the data we split it into training and testing datasets. I also sliced the data to check metrics based on each feature and value.
## Metrics
The metrics I used are:
* precision - Tells us how many of the positive predictions made are actually correct.
* Recall - measures our ability to correctly identify true results (ie when someone actually makes >50k.)
* F1 - gives a good indicator of the balance between precision and recall. If the number is greater than 1, then recall is better. If it is less than 1, then precision is better.

The model currently scores at:
> Precision: 0.7396 | Recall: 0.6186 | F1: 0.6737

## Ethical Considerations
* Because we are trying to target income levels, it is important to make sure the model is accurate. Introducing a false bias towards a group/subset of people could lead to unfair representation while trying to make decisions based on model predictions such as offering services or special offers.
* Because the training data deals with individuals, it is important to ensure training and testing data stays anonymized.

## Caveats and Recommendations

1. It is recommended to recognized that this data was trained on only US census data. This model may not accurately predict other populations.
2. The model scores indicate that there is room for improvement, users should be made aware that this will not be perfectly accurate, rather this will provide an educated guess based on general population data.


import pandas as pd
test = pd.read_csv(r"kaggle-housePrice\dataset\test.csv")
""" Test: Unhash # the print below to test """
#print(test.head())
# print(test.head().to_string())

""" Train: Unhash # the train below to train """
train = pd.read_csv(r"kaggle-housePrice\dataset\train.csv")
print(train.head())

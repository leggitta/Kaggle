import pandas as pd

def load_titanic(fillna=True, recode=True):
    
    # define training and testing data files
    train_file = "../data/train.csv"
    test_file = "../data/test.csv"

    # read files into pandas
    train = pd.read_csv(train_file)
    test = pd.read_csv(test_file)
    
    # fill any missing values
    if fillna:
    
        # compute default values for missing data
        med_age = train.Age.median()  # median age
        mod_emb = train.Embarked.mode().values[0]  # mode embarked point
        med_fair = train.Fare.median()  # median fair

        # fill missing columns
        train.fillna({'Age': med_age, 'Embarked': mod_emb}, inplace=True)
        test.fillna({'Age': med_age, 'Fare': med_fair}, inplace=True)
        
    # recode categorical values
    if recode:
        
        # recode categorical variables
        sex = {'female': 0, 'male': 1}
        emb = {'S': 0, 'C': 1, 'Q': 2}
        train.replace({'Sex': sex, 'Embarked': emb}, inplace=True)
        test.replace({'Sex': sex, 'Embarked': emb}, inplace=True)
        
    # return training and testing data frames
    return train, test
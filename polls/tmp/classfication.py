import pandas as pd
import numpy as np
import time
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler, LabelEncoder

from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn import tree
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB


# need refractor here
method_dict = {
        "LG": LogisticRegression(),
        "KN": KNeighborsClassifier(),
        "SV": SVC(),
        "GB": GradientBoostingClassifier(n_estimators=1000),
        "DT": tree.DecisionTreeClassifier(),
        "RF": RandomForestClassifier(n_estimators=1000),
        "MP": MLPClassifier(alpha = 1),
        "NB": GaussianNB(),
    }

dict_classifiers = {
    "Logistic Regression": LogisticRegression(),
    "Nearest Neighbors": KNeighborsClassifier(),
    "Linear SVM": SVC(),
    "Gradient Boosting Classifier": GradientBoostingClassifier(n_estimators=1000),
    "Decision Tree": tree.DecisionTreeClassifier(),
    "Random Forest": RandomForestClassifier(n_estimators=1000),
    "Neural Net": MLPClassifier(alpha = 1),
    "Naive Bayes": GaussianNB(),
    # "AdaBoost": AdaBoostClassifier(),
    # "QDA": QuadraticDiscriminantAnalysis(),
    # "Gaussian Process": GaussianProcessClassifier()
}

def batch_classify(X_train, Y_train, X_test, Y_test, classifier_name, verbose=True):
    """
    This method, takes as input the X, Y matrices of the Train and Test set.
    And fits them on all of the Classifiers specified in the dict_classifier.
    The trained models, and accuracies are saved in a dictionary. The reason to use a dictionary
    is because it is very easy to save the whole dictionary with the pickle module.

    Usually, the SVM, Random Forest and Gradient Boosting Classifier take quiet some time to train.
    So it is best to train them on a smaller dataset first and
    decide whether you want to comment them out or not based on the test accuracy score.
    """
    t_start = time.process_time()
    classifier = method_dict[classifier_name]
    classifier.fit(X_train, Y_train)
    t_end = time.process_time()
    t_diff = t_end - t_start;
    train_score = classifier.score(X_train, Y_train)
    test_score = classifier.score(X_test, Y_test)

    result =  {'model': classifier, 'train_score': train_score, 'test_score': test_score,
                                        'train_time': t_diff}
    return result

    # dict_models = {}
    # for classifier_name, classifier in list(dict_classifiers.items())[:no_classifiers]:
    #     t_start = time.process_time()
    #     classifier.fit(X_train, Y_train)
    #     t_end = time.process_time()
    #
    #     t_diff = t_end - t_start
    #     train_score = classifier.score(X_train, Y_train)
    #     test_score = classifier.score(X_test, Y_test)
    #
    #     dict_models[classifier_name] = {'model': classifier, 'train_score': train_score, 'test_score': test_score,
    #                                     'train_time': t_diff}
    #     if verbose:
    #         print("trained {c} in {f:.2f} s".format(c=classifier_name, f=t_diff))
    # return dict_models


def display_dict_models(dict_models, sort_by='test_score'):
    cls = [key for key in dict_models.keys()]
    test_s = [dict_models[key]['test_score'] for key in cls]
    training_s = [dict_models[key]['train_score'] for key in cls]
    training_t = [dict_models[key]['train_time'] for key in cls]

    df_ = pd.DataFrame(data=np.zeros(shape=(len(cls), 4)),
                       columns=['classifier', 'train_score', 'test_score', 'train_time'])
    for ii in range(0, len(cls)):
        df_.loc[ii, 'classifier'] = cls[ii]
        df_.loc[ii, 'train_score'] = training_s[ii]
        df_.loc[ii, 'test_score'] = test_s[ii]
        df_.loc[ii, 'train_time'] = training_t[ii]

    print(df_)


"""
    This function fetches the training data set 
    and the origin dataset
"""
def get_train_test(df, label_name, x_name, ratio):
    mask = np.random.choice([True, False], size=len(df), p=[ratio, 1-ratio])

    df_train = df[mask]
    df_test = df[~mask]

    label_train = df_train[label_name].values
    label_test = df_test[label_name].values
    x_train = df_train[x_name].values
    x_test = df_test[x_name].values

    return df_train, df_test, x_train, label_train, x_test, label_test



if __name__ == '__main__':

    """
        This section preprocess the missing data or non_numeric data
    """

    df = pd.read_csv("data\\1_3cweka.csv")

    # drop na data at first
    df = df.dropna()

    col_names = df.columns
    print(col_names)
    bad_col_name=[]
    for col_name in col_names:
        if np.issubdtype(df[col_name].dtype, np.number) != True:
            bad_col_name.append(col_name)

    # show_df is only used for shown purpose
    # df is used to remove the non_numeric

    show_df = df.copy(deep = True)
    for col in bad_col_name:
        # starts from 1, uniques is not used now
        labels, uniques = pd.factorize(df[col])
        show_df[col+"_digit"] = pd.Categorical(labels + 1)



    df = show_df.drop(columns = bad_col_name)

    print(show_df)
    print(df)

    label_name = col+'_digit'
    x_name = list(df.columns.values)
    x_name.remove(label_name)

    train_test_ratio = 0.7
    df_train, df_test, X_train, Y_train, X_test, Y_test = get_train_test(df, label_name, x_name,
                                                                         train_test_ratio)

    dict_models = batch_classify(X_train, Y_train, X_test, Y_test, no_classifiers=8)
    display_dict_models(dict_models)
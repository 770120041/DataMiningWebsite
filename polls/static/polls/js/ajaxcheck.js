function ajax_class_change(){
    let method_name = $('#id_method_selection').find(":selected").text();
    class_method_default_parameter(method_name);
}

// default descrption text
function class_method_description_text(method_name) {

    let method_dict = {
             'LogisticRegression': "logistic ",
             "KNeighborsClassifier": "Knn neighbors",
             "SVC": "SVCrs",
             "GradientBoostingClassifier": "GBC",
             "DecisionTreeClassifier": "decision tree",
             "RandomForestClassifier": "randomclassificer",
             "MLPClassifier": "MLPC",
             "GaussianNB": "Gaussian",
        }
      $("#classification_parameter_description").text(method_dict[method_name]);
}
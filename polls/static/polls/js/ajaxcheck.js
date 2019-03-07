

function ajax_class_change() {
    let method_name = $('#id_method_selection').find(":selected").text();
    class_description_text(method_name);
}


function class_description_text(method_name) {

    let method_dict = {
             'LogisticRegression': "logistic parames ",
             "KNeighborsClassifier": "Knn neighbors parames",
             "SVC": "SVCrs parames",
             "GradientBoostingClassifier": "GBC parames",
             "DecisionTreeClassifier": "decision tree parames",
             "RandomForestClassifier": "randomclassificer parames",
             "MLPClassifier": "MLPC parames",
             "GaussianNB": "Gaussian parames",
        }
      $("#classification_parameter_description").text(method_dict[method_name]);
}


function ajax_class_change() {
    let method_name = $('#id_method_selection').find(":selected").text();
    class_description_text(method_name);
    init_classification_parameters(method_name);
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
function init_classification_parameters(method_name){
    let method_init_parma_dict = {
             'LogisticRegression': "logistic init param",
             "KNeighborsClassifier": "Knn neighbors init param",
             "SVC": "SVCrs init param",
             "GradientBoostingClassifier": "GBC init param",
             "DecisionTreeClassifier": "decision tree init param",
             "RandomForestClassifier": "randomclassificer init param",
             "MLPClassifier": "MLPC init param",
             "GaussianNB": "Gaussian init param",
        }
        document.getElementById("id_classification_parameters").value = method_init_parma_dict[method_name];
}
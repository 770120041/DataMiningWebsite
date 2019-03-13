

function ajax_class_change() {
    let method_name = $('#id_method_selection').find(":selected").text();
    class_description_text(method_name);
    init_classification_parameters(method_name);
}


function class_description_text(method_name) {


    let method_dict = {
             'LogisticRegression': logis_params_description_text,
             "KNeighborsClassifier": "Knn neighbors parames",
             "SVC": "SVCrs parames",
             "GradientBoostingClassifier": "GBC parames",
             "DecisionTreeClassifier": "decision tree parames",
             "RandomForestClassifier": "randomclassificer parames",
             "MLPClassifier": "MLPC parames",
             "GaussianNB": "Gaussian parames",
        }
      $("#classification_parameter_description").wrap(method_dict[method_name]);
}
function init_classification_parameters(method_name){
    let method_init_parma_dict = {
             'LogisticRegression': logistic_init_param,
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


let logis_params_description_text =
        "<small>" +
        "*  Classifier is the method used for classification<br>" +
        "*  Lable Name is the name of the label used for training<br>" +
        "*  Train ratio is the Train/Test ratio used for training and testing.<br><br>" +
        "*  Classification parameters:<br>" +
        "*** penalty : str, ‘l1’ or ‘l2’, default: ‘l2’<br>" +
        "*** max_iter : int, default: 100<br>" +
        "*** tol : float, default: 1e-4(Tolerance for stopping criteria.)<br>"  +
        "*** Usage Example: type in <em>{\"penalty\":\"l1\", \"max_iter\":100}</em>, to set parameter \"penalty\" to \"l1\" <br>" +
        "<br>More details can be referenced at " +
        "<a href=\"https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression\">Official Document</a>" +
        "</small> \n";

let logistic_init_param = "{\"penalty\":\"l1\", \"max_iter\":100}"
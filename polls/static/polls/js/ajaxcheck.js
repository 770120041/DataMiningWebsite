

let params_description_head =   "<span>" +
        "*  Classifier is the method used for classification<br>" +
        "*  Lable Name is the name of the label used for training<br>" +
        "*  Train ratio is the Train/Test ratio used for training and testing.<br>"+
        "*  Parameters can be set in field \"Classification parameters\"<br>" +
    "Example: type in <em>{\"penalty\":\"l1\", \"max_iter\":100}</em> in the field of Classification parameters<br>" +
    " to set parameter \"penalty\" to \"l1\",\"max_iter\" to 100 <br><br>";

let logis_params_description_text =
        params_description_head+
        "*   Logistic Regression parameters:<br>" +
        "*** penalty : str, ‘l1’ or ‘l2’, default: ‘l2’<br>" +
        "*** max_iter : int, default: 100<br>" +
        "*** tol : float, default: 1e-4(Tolerance for stopping criteria.)<br>"  +
        "<br>More details can be found at " +
        "<a href=\"https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression\">Official Document</a>" +
        "</span> \n";

let knn_params_description_text =
   params_description_head +
        "*  KNN parameters:<br>" +
        "*** n_neighbors : int, optional (default = 5)<br>" +
        "*** weights : str or callable, optional (default = ‘uniform’)<br>" +
        "*** leaf_size : int, optional (default = 30)<br>"  +
        "<br>More details can be found at " +
        "<a href=\"https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html\">Official Document</a>" +
        "</span> \n";

let SVC_params_description_text =
   params_description_head +
        "*  SVC parameters:<br>" +
        "*** n_neighbors : int, optional (default = 5)<br>" +
        "*** weights : str or callable, optional (default = ‘uniform’)<br>" +
        "*** leaf_size : int, optional (default = 30)<br>"  +
        "<br>More details can be found at " +
        "<a href=\"https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html\">Official Document</a>" +
        "</span> \n";

let GBC_params_description_text =
   params_description_head +
        "*  GBC parameters:<br>" +
        "*** n_neighbors : int, optional (default = 5)<br>" +
        "*** weights : str or callable, optional (default = ‘uniform’)<br>" +
        "*** leaf_size : int, optional (default = 30)<br>"  +
        "<br>More details can be found at " +
        "<a href=\"https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html\">Official Document</a>" +
        "</span> \n";

let DT_params_description_text =
   params_description_head +
        "*  DT parameters:<br>" +
        "*** n_neighbors : int, optional (default = 5)<br>" +
        "*** weights : str or callable, optional (default = ‘uniform’)<br>" +
        "*** leaf_size : int, optional (default = 30)<br>"  +
        "<br>More details can be found at " +
        "<a href=\"https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html\">Official Document</a>" +
        "</span> \n";

let RF_params_description_text =
   params_description_head +
        "*  RF parameters:<br>" +
        "*** n_neighbors : int, optional (default = 5)<br>" +
        "*** weights : str or callable, optional (default = ‘uniform’)<br>" +
        "*** leaf_size : int, optional (default = 30)<br>"  +
        "<br>More details can be found at " +
        "<a href=\"https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html\">Official Document</a>" +
        "</span> \n";

let MLPC_params_description_text =
   params_description_head +
        "*  MLPC parameters:<br>" +
        "*** n_neighbors : int, optional (default = 5)<br>" +
        "*** weights : str or callable, optional (default = ‘uniform’)<br>" +
        "*** leaf_size : int, optional (default = 30)<br>"  +
        "<br>More details can be found at " +
        "<a href=\"https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html\">Official Document</a>" +
        "</span> \n";

GNB_params_description_text = params_description_head +
        "*  GNB parameters:<br>" +
        "*** n_neighbors : int, optional (default = 5)<br>" +
        "*** weights : str or callable, optional (default = ‘uniform’)<br>" +
        "*** leaf_size : int, optional (default = 30)<br>"  +
        "<br>More details can be found at " +
        "<a href=\"https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html\">Official Document</a>" +
        "</span> \n";

let logistic_init_param = "{\"penalty\":\"l1\", \"max_iter\":100}";
let knn_init_param = "{\"n_neighbors\":5}";
let SVC_init_param = "SVC";
let GBC_init_parma =  "GBC init param";
let DCT_init_param =  "decision tree init param";
let RF_init_param =  "randomclassificer init param";
let MLPC_init_param = "MLPC init param";
let Gaussian_init_param = "Gaussian init param";

   let method_init_parma_dict = {
             'LogisticRegression': logistic_init_param,
             "KNeighborsClassifier": knn_init_param,
             "SVC": SVC_init_param,
             "GradientBoostingClassifier": GBC_init_parma,
             "DecisionTreeClassifier": DCT_init_param,
             "RandomForestClassifier": RF_init_param,
             "MLPClassifier": MLPC_init_param,
             "GaussianNB": Gaussian_init_param,
        };


    let method_description_dict = {
             'LogisticRegression': logis_params_description_text,
             "KNeighborsClassifier": knn_params_description_text,
             "SVC": SVC_params_description_text,
             "GradientBoostingClassifier": GBC_params_description_text,
             "DecisionTreeClassifier": DT_params_description_text,
             "RandomForestClassifier": RF_params_description_text,
             "MLPClassifier": MLPC_params_description_text,
             "GaussianNB": GNB_params_description_text,
        };

function class_description_text(method_name) {
    // alert(method_description_dict[method_name])
    $("#classification_parameter_description").wrapInner(method_description_dict[method_name]);
}
function init_classification_parameters(method_name){
// alert(method_init_parma_dict[method_name])
//     alert(method_init_parma_dict[method_name])
    $("#id_classification_parameters").text(method_init_parma_dict[method_name])
}


function ajax_class_change() {
    let method_name = $('#id_Classifier').find(":selected").text();
    // alert(method_name);
    class_description_text(method_name);
    init_classification_parameters(method_name);
}
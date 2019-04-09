

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
        "<br>More details can be found  " +
         "<a target=\"_blank\" href=\"/polls/docs/LOGISTIC_doc/\">Here</a>" +
        "</span> \n";

let knn_params_description_text =
   params_description_head +
        "*  KNN parameters:<br>" +
        "*** n_neighbors : int, optional (default = 5)<br>" +
        "*** weights : str or callable, optional (default = ‘uniform’)<br>" +
        "*** leaf_size : int, optional (default = 30)<br>"  +
        "<br>More details can be found  " +
     "<a target=\"_blank\" href=\"/polls/docs/KNN_doc/\">Here</a>" +
    "</span> \n";

let SVC_params_description_text =
   params_description_head +
        "*  SVC parameters:<br>" +
        "*** C : float, optional (default=1.0)<br>" +
        "*** kernel : string, optional (default=’rbf’)<br>" +
        "*** degree : int, optional (default=3)<br>"  +
        "*** tol : float, optional (default=1e-3)<br>" +
        "<br>More details can be found  " +
     "<a target=\"_blank\" href=\"/polls/docs/SVC_doc/\">Here</a>" +
    "</span> \n";


let DT_params_description_text =
   params_description_head +
        "*  DecisionTreeClassifier parameters:<br>" +
        "*** criterion : string, optional (default=”gini”)<br>" +
        "*** splitter : string, optional (default=”best”)<br>" +
        "*** max_depth : int or None, optional (default=None)<br>"  +
        "<br>More details can be found  " +
        "<a target=\"_blank\" href=\"/polls/docs/DT_doc/\">Here</a>" +
        "</span> \n";

let RF_params_description_text =
   params_description_head +
        "*  RandomForestClassifier parameters:<br>" +
        "*** n_estimators : integer, optional (default=10)<br>" +
        "*** criterion : string, optional (default=”gini”)<br>" +
        "*** max_depth : integer or None, optional (default=None)<br>"  +
        "<br>More details can be found  " +
         "<a target=\"_blank\" href=\"/polls/docs/RF_doc/\">Here</a>" +
    "</span> \n";

let MLPC_params_description_text =
   params_description_head +
        "*  MLPClassifier parameters:<br>" +
        "*** hidden_layer_sizes : tuple, length = n_layers - 2, default (100,)<br>" +
        "*** activation : {‘identity’, ‘logistic’, ‘tanh’, ‘relu’}, default ‘relu’<br>" +
        "*** solver : {‘lbfgs’, ‘sgd’, ‘adam’}, default ‘adam’<br>"  +
        "<br>More details can be found " +
         "<a target=\"_blank\" href=\"/polls/docs/MLPC_doc/\">Here</a>" +
    "</span> \n";

let GNB_params_description_text = params_description_head +
        "*  GaussianNB parameters:<br>" +
        "*** priors : array-like, shape (n_classes,)<br>" +
        "*** var_smoothing : float, optional (default=1e-9)<br>" +
        "<br>More details can be found  " +
         "<a target=\"_blank\" href=\"/polls/docs/GNB_doc/\">Here</a>" +
    "</span> \n";

let logistic_init_param = "{\"penalty\":\"l1\", \"max_iter\":100}";
let knn_init_param = "{\"n_neighbors\":5}";
let SVC_init_param = "{\"tol\":1e-3, \"C\":1.0}";
// let GBC_init_param =  "{\"loss\":\"exponential\", \"n_estimators\":100}";
let DCT_init_param =  "{\"criterion\":\"gini\", \"splitter\":\"best\"}";
let RF_init_param =  "{\"n_estimators\":10, \"criterion\":\"gini\"}";
let MLPC_init_param = "{\"activation\":\"relu\"}";
let GNB_init_param = "{\"var_smoothing\":1e-9}";

   let method_init_parma_dict = {
             'LogisticRegression': logistic_init_param,
             "KNeighborsClassifier": knn_init_param,
             "SVC": SVC_init_param,
             // "GradientBoostingClassifier": GBC_init_param,
             "DecisionTreeClassifier": DCT_init_param,
             "RandomForestClassifier": RF_init_param,
             "MLPClassifier": MLPC_init_param,
             "GaussianNB": GNB_init_param,
        };


    let method_description_dict = {
             'LogisticRegression': logis_params_description_text,
             "KNeighborsClassifier": knn_params_description_text,
             "SVC": SVC_params_description_text,
             // "GradientBoostingClassifier": GBC_params_description_text,
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
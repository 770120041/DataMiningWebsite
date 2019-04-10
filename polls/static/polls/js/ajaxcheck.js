

/*
    Classification description text and Ajax change function

 */

let class_params_description_head =   "<span>" +
        "*  Classifier is the method used for classification<br>" +
        "*  Lable Name is the name of the label used for training<br>" +
        "*  Train ratio is the Train/Test ratio used for training and testing.<br>"+
        "*  Parameters can be set in field \"Classification parameters\"<br>" +
    "Example: type in <em>{\"penalty\":\"l1\", \"max_iter\":100}</em> in the field of Classification parameters<br>" +
    " to set parameter \"penalty\" to \"l1\",\"max_iter\" to 100 <br><br>";

let logis_params_description_text =
        class_params_description_head+
        "*   Logistic Regression parameters:<br>" +
        "*** penalty : str, ‘l1’ or ‘l2’, default: ‘l2’<br>" +
        "*** max_iter : int, default: 100<br>" +
        "*** tol : float, default: 1e-4(Tolerance for stopping criteria.)<br>"  +
        "<br>More details can be found  " +
         "<a target=\"_blank\" href=\"/polls/docs/CF/LOGISTIC_doc/\">Here</a>" +
        "</span> \n";

let knn_params_description_text =
   class_params_description_head +
        "*  KNN parameters:<br>" +
        "*** n_neighbors : int, optional (default = 5)<br>" +
        "*** weights : str or callable, optional (default = ‘uniform’)<br>" +
        "*** leaf_size : int, optional (default = 30)<br>"  +
        "<br>More details can be found  " +
     "<a target=\"_blank\" href=\"/polls/docs/CF/KNN_doc/\">Here</a>" +
    "</span> \n";

let SVC_params_description_text =
   class_params_description_head +
        "*  SVC parameters:<br>" +
        "*** C : float, optional (default=1.0)<br>" +
        "*** kernel : string, optional (default=’rbf’)<br>" +
        "*** degree : int, optional (default=3)<br>"  +
        "*** tol : float, optional (default=1e-3)<br>" +
        "<br>More details can be found  " +
     "<a target=\"_blank\" href=\"/polls/docs/CF/SVC_doc/\">Here</a>" +
    "</span> \n";


let DT_params_description_text =
   class_params_description_head +
        "*  DecisionTreeClassifier parameters:<br>" +
        "*** criterion : string, optional (default=”gini”)<br>" +
        "*** splitter : string, optional (default=”best”)<br>" +
        "*** max_depth : int or None, optional (default=None)<br>"  +
        "<br>More details can be found  " +
        "<a target=\"_blank\" href=\"/polls/docs/CF/DT_doc/\">Here</a>" +
        "</span> \n";

let RF_params_description_text =
   class_params_description_head +
        "*  RandomForestClassifier parameters:<br>" +
        "*** n_estimators : integer, optional (default=10)<br>" +
        "*** criterion : string, optional (default=”gini”)<br>" +
        "*** max_depth : integer or None, optional (default=None)<br>"  +
        "<br>More details can be found  " +
         "<a target=\"_blank\" href=\"/polls/docs/CF/RF_doc/\">Here</a>" +
    "</span> \n";

let MLPC_params_description_text =
   class_params_description_head +
        "*  MLPClassifier parameters:<br>" +
        "*** hidden_layer_sizes : tuple, length = n_layers - 2, default (100,)<br>" +
        "*** activation : {‘identity’, ‘logistic’, ‘tanh’, ‘relu’}, default ‘relu’<br>" +
        "*** solver : {‘lbfgs’, ‘sgd’, ‘adam’}, default ‘adam’<br>"  +
        "<br>More details can be found " +
         "<a target=\"_blank\" href=\"/polls/docs/CF/MLPC_doc/\">Here</a>" +
    "</span> \n";

let GNB_params_description_text = class_params_description_head +
        "*  GaussianNB parameters:<br>" +
        "*** priors : array-like, shape (n_classes,)<br>" +
        "*** var_smoothing : float, optional (default=1e-9)<br>" +
        "<br>More details can be found  " +
         "<a target=\"_blank\" href=\"/polls/docs/CF/GNB_doc/\">Here</a>" +
    "</span> \n";

let logistic_init_param = "{\"penalty\":\"l1\", \"max_iter\":100}";
let knn_init_param = "{\"n_neighbors\":5}";
let SVC_init_param = "{\"tol\":1e-3, \"C\":1.0}";
// let GBC_init_param =  "{\"loss\":\"exponential\", \"n_estimators\":100}";
let DCT_init_param =  "{\"criterion\":\"gini\", \"splitter\":\"best\"}";
let RF_init_param =  "{\"n_estimators\":10, \"criterion\":\"gini\"}";
let MLPC_init_param = "{\"activation\":\"relu\"}";
let GNB_init_param = "{\"var_smoothing\":1e-9}";

   let class_mathod_init_param = {
             'LogisticRegression': logistic_init_param,
             "KNeighborsClassifier": knn_init_param,
             "SVC": SVC_init_param,
             // "GradientBoostingClassifier": GBC_init_param,
             "DecisionTreeClassifier": DCT_init_param,
             "RandomForestClassifier": RF_init_param,
             "MLPClassifier": MLPC_init_param,
             "GaussianNB": GNB_init_param,
        };


    let class_method_descripion_dict = {
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
    // alert(class_method_descripion_dict[method_name])
    $("#classification_parameter_description").wrapInner(class_method_descripion_dict[method_name]);
}
function init_classification_parameters(method_name){
// alert(class_mathod_init_param[method_name])
//     alert(class_mathod_init_param[method_name])
    $("#id_classification_parameters").text(class_mathod_init_param[method_name])
}


function ajax_class_change() {
    let method_name = $('#id_Classifier').find(":selected").text();
    // alert(method_name);
    class_description_text(method_name);
    init_classification_parameters(method_name);
}

/*
    End of Classification
 */



/*
    Start of clustering Ajax change
 */

let cluster_params_description_head =   "<span>" +
        "*  Cluster algo is the algorithm used for clustering. <br>"+
        "*  Parameters can be set in field \"Clustering  parameters\"<br>" +
    "Example: type in <em>{\"penalty\":\"l1\", \"max_iter\":100}</em> in the field of Classification parameters<br>" +
    " to set parameter \"penalty\" to \"l1\",\"max_iter\" to 100 <br><br>";


    let KMeans_description_text =
        cluster_params_description_head +
        "*   KMeans Clustering parameters:<br>" +
        "*** n_clusters  : int, optional, default: 8<br>" +
        "*** init  : {‘k-means++’, ‘random’ or an ndarray}<br>" +
        "*** max_iter  : int, default: 300<br>"  +
        "<br>More details can be found  " +
         "<a target=\"_blank\" href=\"/polls/docs/CR/KMS_doc/\">Here</a>" +
        "</span> \n";

    let MiniBatchKMeans_description_text = cluster_params_description_head +
        "*   MiniBatchKMeans Clustering parameters:<br>" +
        "*** n_clusters  : int, optional, default: 8<br>" +
        "*** batch_size : int, optional, default: 100 <br>" +
        "*** max_iter  : int, default: 300<br>"  +
        "<br>More details can be found  " +
         "<a target=\"_blank\" href=\"/polls/docs/CR/MBKM_doc/\">Here</a>" +
        "</span> \n";
    let AffinityPropagation_description_text =cluster_params_description_head +
        "*   AffinityPropagation Clustering parameters:<br>" +
        "*** damping   : float, optional, default: 0.5<br>" +
        "*** max_iter   : int, optional, default: 200<br>" +
        "*** convergence_iter   : int, optional, default: 15<br>"  +
        "<br>More details can be found  " +
         "<a target=\"_blank\" href=\"/polls/docs/CR/AFP_doc/\">Here</a>" +
        "</span> \n";
    let MeanShift_description_text = cluster_params_description_head +
        "*   MeanShift Clustering parameters:<br>" +
        "*** bandwidth   : float, optional<br>" +
        "*** bin_seeding   : boolean, optional<br>" +
        "*** n_jobs   :  int or None, optional (default=None)<br>"  +
        "<br>More details can be found  " +
         "<a target=\"_blank\" href=\"/polls/docs/CR/MSF_doc/\">Here</a>" +
        "</span> \n";
    let SpectralClustering_description_text =cluster_params_description_head +
        "*   SpectralClustering parameters:<br>" +
        "*** n_clusters  : int, optional, default: 8<br>" +
        "*** eigen_solver   : {None, ‘arpack’, ‘lobpcg’, or ‘amg’}<br>" +
        "*** n_init   :int, optional, default: 10<br>"  +
        "<br>More details can be found  " +
         "<a target=\"_blank\" href=\"/polls/docs/CR/SPECC_doc/\">Here</a>" +
        "</span> \n";
    let AgglomerativeClustering_description_text = cluster_params_description_head +
        "*   AgglomerativeClustering parameters:<br>" +
        "*** n_clusters  :  int, default=2<br>" +
        "*** affinity   :  string or callable, default: “euclidean”<br>" +
        "*** linkage   :  {“ward”, “complete”, “average”, “single”}, optional (default=”ward”)<br>"  +
        "<br>More details can be found  " +
         "<a target=\"_blank\" href=\"/polls/docs/CR/AGC_doc/\">Here</a>" +
        "</span> \n";
    let Birch_description_text = cluster_params_description_head +
        "*   Birch Clustering parameters:<br>" +
        "*** branching_factor    :  int, default 50<br>" +
        "*** threshold  : float, default 0.5<br>" +
        "*** n_clusters   :  int, instance of sklearn.cluster model, default 3<br>"  +
        "<br>More details can be found  " +
         "<a target=\"_blank\" href=\"/polls/docs/CR/BRC_doc/\">Here</a>" +
        "</span> \n";
    let DBSCAN_description_text =cluster_params_description_head +
        "*   DBSCAN Clustering parameters:<br>" +
        "*** eps   :  float, optional<br>" +
        "*** min_samples   :int, optional<br>" +
        "*** algorithm   : {‘auto’, ‘ball_tree’, ‘kd_tree’, ‘brute’}, optional<br>"  +
        "<br>More details can be found  " +
         "<a target=\"_blank\" href=\"/polls/docs/CR/DBSCAN_doc/\">Here</a>" +
        "</span> \n";
   let cluster_method_description_dict ={
        "KMeans": KMeans_description_text,
        "MiniBatchKMeans": MiniBatchKMeans_description_text,
        "AffinityPropagation": AffinityPropagation_description_text,
        "MeanShift": MeanShift_description_text,
        "SpectralClustering" : SpectralClustering_description_text,
        "AgglomerativeClustering" : AgglomerativeClustering_description_text,
        "DBSCAN" : DBSCAN_description_text,
        "Birch" : Birch_description_text,
    };
    let KMeans_init_param = "{\"n_clusters\":8}";
    let MiniBatchKMeans_init_param = "{\"n_clusters\":8}";
    let AffinityPropagation_init_param = "{\"convergence_iter\":15,\"damping\":0.5 }";
    let MeanShift_init_param = "{\"bandwidth\":2,\"bin_seeding\":\"True\"}";
    let SpectralClustering_init_param = "{\"eigen_solver\":\"arpack\"," +
        "\"affinity\":\"nearest_neighbors\"}";
    let AgglomerativeClustering_init_param = "{\"linkage\":\"average\"}";
    let DBSCAN_init_param = "{\"eps\":3,\"leaf_size\":30}";
    let Birch_init_param = "{\"threshold\":0.5,\"branching_factor\":50}";

    let cluster_method_init_parma ={
        "KMeans": KMeans_init_param,
        "MiniBatchKMeans": MiniBatchKMeans_init_param,
        "AffinityPropagation": AffinityPropagation_init_param,
        "MeanShift": MeanShift_init_param,
        "SpectralClustering" : SpectralClustering_init_param,
        "AgglomerativeClustering" : AgglomerativeClustering_init_param,
        "DBSCAN" : DBSCAN_init_param,
        "Birch" : Birch_init_param,
    };




function get_cluster_description_text(method_name) {
    // alert(cluster_method_description_dict[method_name])
    $("#clusterification_parameter_description").wrapInner(cluster_method_description_dict[method_name]);
}
function init_cluster_params(method_name){
// alert(cluster_method_init_parma[method_name])
//     alert(class_mathod_init_param[method_name])
    $("#id_Clustering_Parameters").text(cluster_method_init_parma[method_name])
}
function ajax_cluster_change() {
    let method_name = $('#id_Cluster_Algo').find(":selected").text();
    // alert(method_name);
    get_cluster_description_text(method_name);
    init_cluster_params(method_name);
}
/*

    Clustring parmas
 */
function ajax_class_change(){

    let method_dict = {
             'LogisticREgression': "parameters",
             "KNeighborsClassifier": "x=number of neighbors",
             "SVC": "parameters",
             "GradientBoostingClassifier": "parameters",
             "DecisionTreeClassifier": "parameters",
             "RandomForestClassifier": "parameters",
             "MLPClassifier": "parameters",
             "GaussianNB": "parameters",
        }
    let method_name = $('#id_method_selection').find(":selected").text();
    $("#classification_parameter_description").text(method_dict[method_name]);
    // alert(method_dict[method_name])

}


$("#id_method_selection").change(
    function () {
        alert("hellow");
        var method_name = $('#id_method_selection').find(":selected").text();
        alert(conceptName)
    }
);
"""
    This file provides logic about clustering
"""
import json
import time
import warnings
import numpy as np
from sklearn import cluster


clustering_algorithms = {
        'KMeans': cluster.KMeans,
        'MiniBatchKMeans': cluster.MiniBatchKMeans,
        'AffinityPropagation': cluster.affinity_propagation,
        'MeanShift': cluster.MeanShift,
        'SpectralClustering': cluster.SpectralBiclustering,
        'AgglomerativeClustering': cluster.AgglomerativeClustering,
        'DBSCAN': cluster.dbscan,
        'Birch': cluster.birch,
}

clustering_method_name = {
        "KMS": 'KMeans',
        "MBKM": "MiniBatchKMeans",
        "AFP": "AffinityPropagation",
        # "GB": "GradientBoostingClassifier",
        "MSF": "MeanShift",
        "SPECC" : "SpectralClustering",
        "AGC" : "AgglomerativeClustering",
        "DBSCAN" : "DBSCAN",
        "BRC" : "Birch"
    }

def MyClustering(df, cluster_method, param=""):
    param_literal = json.loads(param)

    t_start = time.process_time()
    param_literal = json.loads(param)
    print(type(param_literal))
    # the cluter method and its param
    cur_cluster_method = clustering_algorithms[clustering_method_name[cluster_method]](**param_literal)


    # catch warnings related to kneighbors_graph
    with warnings.catch_warnings():
        warnings.filterwarnings(
            "ignore",
            message="the number of connected components of the " +
                    "connectivity matrix is [0-9]{1,2}" +
                    " > 1. Completing it to avoid stopping the tree early.",
            category=UserWarning)
        warnings.filterwarnings(
            "ignore",
            message="Graph is not fully connected, spectral embedding" +
                    " may not work as expected.",
            category=UserWarning)
        cur_cluster_method.fit(df)

    t_end = time.process_time()
    t_diff = t_end-t_start
    stat = {'Clusatering_Algorithm': cluster_method,
              'train_time': t_diff}

    if hasattr(cur_cluster_method, 'labels_'):
        y_pred = cur_cluster_method.labels_.astype(np.int)
    else:
        y_pred = cur_cluster_method.predict(df)

    new_df = df.copy(deep=True)
    new_df["clustering_result"] = y_pred
    return new_df, stat



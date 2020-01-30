"""
General comments:
    I feel like the code here should be moved into `train_model.py` since it only
    appears to train the model.

    I recommend folding the current code into a few functions, namely,

        def load_trained_model(path_to_serialized_model: str) -> pd.DataFrame:
            ...

        def preprocess_the_data(data: pd.DataFrame) -> pd.DataFrame:
            ...

        def fit_linear_regression(x_train: np.ndarray, y_train: np.ndarray) -> LinearRegression:
            ...

"""

from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd

# When you're less crunched for time, it might be worth making a
# `definitions.py` module that contains path names used throughout the code. For example,
# import os
# SOURCE_CODE_ROOT = os.path.dirname(os.path.abspath(__file__))
# REPOSITORY_ROOT = os.path.dirname(SOURCE_CODE_ROOT)
# TRAINED_MODELS_DIR = os.path.join(REPOSITORY_ROOT, "models")
# Throughout the repo, the `model_file_name` would just be os.path.join(TRAINED_MODELS_DIR, <name of model>)

# As an aside, the (big) model files would not be checked into Git, but
# instead I recommend providing simple instructions for training the model, e.g.
# To train the model, execute the `train_model` script like so:
# . .venv/bin/activate
# python -m train_model.py

#file_name = '/home/jon/PycharmProjects/jon-insight-project/data/processed/pa_course_database_processed.plk'
file_name = '/home/jon/PycharmProjects/jon-insight-project/jon_insight_project/features/all_courses_database_processed.plk'

df = pd.read_pickle(file_name)


y = df['rating']

tee_type = pd.get_dummies(df['tee_type'])
basket_type = pd.get_dummies(df['basket_type'])
multiple_layouts = pd.get_dummies(df['multiple_layouts'])

attribute_names = ['holes', 'length', 'par', 'sse', 'hills','woods']
x = pd.concat([df[attribute_names], multiple_layouts, tee_type, basket_type], axis=1)

#x.dropna(axis = 0, how = 'any', inplace = True)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=1)


reg = LinearRegression().fit(x_train, y_train)

print('Accuracy on training set:  {:.2f}'.format(reg.score(x_train, y_train)))
print('Accuracy on test set:  {:.2f}'.format(reg.score(x_test, y_test)))

print(reg.score(x, y))

print(reg.coef_)

sklearn.metrics.precision_recall_fscore_support(y_true, y_pred, beta=1.0, labels=None, pos_label=1, average=None,
                                                warn_for=('precision', 'recall', 'f-score'), sample_weight=None,
                                                zero_division='warn')[source]



print('hello')






































# import matplotlib.pyplot as plt
# import osmnx as ox
# from descartes import PolygonPatch
# from shapely.geometry import Polygon, MultiPolygon
# ox.config(log_console=True, use_cache=True)
# ox.__version__
#
#
#
#
# # get the place shape
# #gdf = ox.gdf_from_place('Portland, Maine')
# gdf = ox.project_gdf(gdf)
#
# # get the street network, with retain_all=True to retain all the disconnected islands' networks
# G = ox.graph_from_place('Portland, Maine', network_type='drive', retain_all=True)
# G = ox.project_graph(G)
#
# fig, ax = ox.plot_graph(G, fig_height=10, show=False, close=False, edge_color='#777777')
# plt.show()
#
# plt.close()
#
#
#
# # to this matplotlib axis, add the place shape as descartes polygon patches
# for geometry in gdf['geometry'].tolist():
#     if isinstance(geometry, (Polygon, MultiPolygon)):
#         if isinstance(geometry, Polygon):
#             geometry = MultiPolygon([geometry])
#         for polygon in geometry:
#             patch = PolygonPatch(polygon, fc='#cccccc', ec='k', linewidth=3, alpha=0.1, zorder=-1)
#             ax.add_patch(patch)
#
#
# # optionally set up the axes extents all nicely
# margin = 0.02
# west, south, east, north = gdf.unary_union.bounds
# margin_ns = (north - south) * margin
# margin_ew = (east - west) * margin
# ax.set_ylim((south - margin_ns, north + margin_ns))
# ax.set_xlim((west - margin_ew, east + margin_ew))
# plt.show()
#
# print('hi')
#- * - encoding : utf - 8 - * -
"""
:copyright: 2017 H2O.ai, Inc.
:license:   Apache License Version 2.0 (see LICENSE for details)
"""
import xgboost as xgb
from ..solvers.pogs import Pogs
from ..solvers.elastic_net import ElasticNetH2O
from ..solvers.elastic_net import ElasticNet
from ..solvers.logistic import LogisticRegression
from ..solvers.linear_regression import LinearRegression
from ..solvers.lasso import Lasso
from ..solvers.ridge import Ridge
from ..solvers.kmeans import KMeans
from ..solvers.pca import PCA
from ..solvers.pca import PCAH2O
from ..solvers.xgboost import RandomForestRegressor
from ..solvers.xgboost import RandomForestClassifier
from ..solvers.xgboost import GradientBoostingClassifier
from ..solvers.xgboost import GradientBoostingRegressor
from ..solvers.truncated_svd import TruncatedSVDH2O
from ..solvers.truncated_svd import TruncatedSVD
from ..solvers.daal_solver.regression import LinearRegression as DLR

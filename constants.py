import os

VCD_TABLE_NAME = 'wf-gcp-us-ae-cost-prod.regional_vcd.tbl_final_regional_vcd_estimates_n_regions'#'wf-gcp-us-ae-cost-prod.regional_vcd.tbl_final_regional_vcd_estimates'
VCD_TABLE_NAME_20REGION = 'wf-gcp-us-ae-cost-prod.regional_vcd.tbl_final_regional_vcd_estimates_n_regions_hypothetical' #'wf-gcp-us-ae-cost-prod.regional_vcd_test.tbl_final_regional_vcd_estimates_n_regions_hypothetical_test'

SUBV1_HEDWIG_NAME = 'wf-gcp-us-ae-recsvc-prod.hedwig.single_class_hedwig_recs_v3_49_5regions_v1' # 5 region subs offline pipeline 
SUBV15_HEDWIG_NAME = 'wf-gcp-us-ae-recsvc-prod.hedwig.single_class_hedwig_recs_v3_49_20regions_v1' # 20 region subs offline pipeline 


SHIP_DIST_NAME_5REGION = 'wf-gcp-us-ae-recsvc-prod.sort_optimization.sortoptlens_v1_shipping_distances_5region'
SHIP_DIST_NAME_20REGION = 'wf-gcp-us-ae-recsvc-prod.sort_optimization.sortoptlens_v1_shipping_distances_20region'

NEW_FILE_NAME = 'df_full_geo_max_vcd_less_regional_vcd.pkl'
PROJECT = 'wf-gcp-us-ae-recsvc-prod'
GCS_BUCKET = 'wf-us-ae-recsvc-storage-prod'
GCS_BUCKET_MODEL = 'wf-ae-recsvc-staging'
GCS_FOLDER_PREFIX = 'sort_optimization/counterfactual_estimation/model_artifiacts'


CLASSES_COVERED =  [167,305] 


POSITION_CUTOFFS = [12, 48, 96, 144, 192]

MAX_POS = 100 # Use a positive integer to set a maximum position to which substitutions are made. Use 'None' for to set no upper limit
MAX_SUBS = 4 # Use a positive integer to set a maximum number of substitution skus available for each anchor. Use 'None' for to set no upper limit

CUSTOMER_REGION_MAPPING = {'20region':'region_20',
                          '5region':'region_5'} #change to 'region_5' for 5 geo model
SUPPLIER_REGION_MAPPING = {'20region':'region_7',
                           '5region':'region_5'}

N_GEOS = 20 # enter number of geos
GEOS = []# list of integers
for n in range(1,N_GEOS + 1):
    GEOS.append(n)

SOID = 49
BCLGID = 1
NUM_SAMPLES = 1
ARMS = ['reg20_geosort','control','variationA']
    # control (Winning Variant from Sub V1) - Geosort (ranking) + 5R Substitution 
    # variationA - 20R Substitution + Geosort (ranking) 
    # variationB - Geosort (ranking) + 20R Substitution
    # reg20_geosort - No substitution, 20 regions Geosort (alpha = 0 for just bubblesort)

ALPHAS = [0.0,0.5] # enter a list of float values of alpha for the test variations


# Chose a function: max_vcd_less_regional_vcd was the finalized iteration
FUNCTION = "max_vcd_less_regional_vcd"
COLUMNS = [
    "pos",
    "sku",
    "sort_scores",
    "vcd_values",
    "shipping_values",
    "shipping_savings_values",
    "cvr_scores",
    "normalized_cvr_scores",
    "normalized_scores",
    "alpha",
    "geo",
    "source_type",
    "arm",
]


metrics = [
    "shipping_values",
    "vcd_values",
    "shipping_savings_values",
    "cvr_scores",
    "cf_score",
    "price",
    "num_reviews",
    "avg_rating"
]


# NUMBER_ELVIS_RECS = 72
# RERANKER_THRESHOLD = 0.66
# TOP_N_MIN_PERSONALIZED = 3
# SUPERBROWSE_PAGE_ORDER_RATE = 0.005536153232
# EPSILON = 1e-10


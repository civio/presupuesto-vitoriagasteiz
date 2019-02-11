# -*- coding: UTF-8 -*-
# from django.conf.urls import patterns, url
# from django.conf.urls.i18n import i18n_patterns


MAIN_ENTITY_LEVEL = 'municipio'

# Main entity name. Must be the same used in data/entidades.csv
MAIN_ENTITY_NAME = 'Vitoria-Gasteiz'

# Theme Budget Loader class name. Default: 'SimpleBudgetLoader'
BUDGET_LOADER = 'VitoriaGasteizBudgetLoader'

# Theme Payments Loader class name. Default: 'PaymentsLoader'
PAYMENTS_LOADER = 'VitoriaGasteizPaymentsLoader'


# Show / hide Settings
# ----------------------

# Show Payments section in menu & home options. Default: False.
SHOW_PAYMENTS = True

# Configure 'by area' payment breakdown. Default: ['area', 'payee', 'description']
# PAYMENTS_BREAKDOWN_BY_AREA = ['area', 'payee', 'description']

# Configure 'by payee' payment breakdown. Default: ['payee', 'area', 'description']
# PAYMENTS_BREAKDOWN_BY_PAYEE = ['payee', 'area', 'description']

# Define if payments year slider is a range (True) or a single year (False). Default: True
# PAYMENTS_YEAR_RANGE = False

# Show Tax Receipt section in menu & home options. Default: False.
SHOW_TAX_RECEIPT = True

# Show Counties & Towns links in Policies section in menu & home options. Default: False.
# SHOW_COUNTIES_AND_TOWNS = True

# Search in entity names. Default: False.
# SEARCH_ENTITIES = True


# Budget Settings
# ----------------------

# Show an extra tab with institutional breakdown. Default: True.
# SHOW_INSTITUTIONAL_TAB  = False

# Show section pages. Still under development, see #347. Default: False.
# SHOW_SECTION_PAGES = True

# Are institutional codes consistent along the years. Default: False.
# Important: We need this to be True for the institutional treemap to work properly.
# CONSISTENT_INSTITUTIONAL_CODES = True

# Show an extra treemap in the Policy page, showing institutional breakdown. Default: False.
# Important: insitutional codes must be consistent along the years, see CONSISTENT_INSTITUTIONAL_CODES.
# SHOW_GLOBAL_INSTITUTIONAL_TREEMAP  = True

# Show an extra tab with funding breakdown (only applicable to some budgets). Default: False.
# SHOW_FUNDING_TAB = True

# Show breadcrumbs in policies. Default: False.
# SHOW_BREADCRUMBS = True

# Show an extra column with actual revenues/expenses. Default: True.
# Warning: the execution data still gets shown in the summary chart and in downloads.
# SHOW_ACTUAL = False

# Should we group elements at the economic subheading level, or list all of them,
# grouping by uid?. Default: True. (i.e. group by uid, show all elements)
# BREAKDOWN_BY_UID = False

# Include financial income/expenditures in overview and global policy breakdowns. Default: False
INCLUDE_FINANCIAL_CHAPTERS_IN_BREAKDOWNS = True

# Does the data includes a fifth functional classification level, subprogrammes?. Default: False
# USE_SUBPROGRAMMES = True


# Theme Settings
# ----------------------

# Supported languages. Default: ('es', 'Castellano')
LANGUAGES = (
  ('eu', 'Euskera'),
  ('es', 'Castellano'),
)

# Facebook Aplication ID used in social_sharing temaplate. Default: ''
# In order to get the ID create an app in https://developers.facebook.com/
FACEBOOK_ID = '101568380658287'

# Google Analytics ID. Default: ''
# In order to get the ID create a Google Analytics Acount in https://analytics.google.com/analytics/web/
ANALYTICS_ID = 'UA-28946840-43'

# Setup Data Source Budget link
DATA_SOURCE_BUDGET = 'https://www.vitoria-gasteiz.org/j34-01w/catalogo/portada'

# Setup Data Source Population link
DATA_SOURCE_POPULATION = 'http://www.ine.es/jaxiT3/Tabla.htm?t=2854&L=0'

# Setup Data Source Inflation link
DATA_SOURCE_INFLATION = 'http://www.ine.es/jaxiT3/Tabla.htm?t=22350&L=0'

# Setup Main Entity Web Url
MAIN_ENTITY_WEB_URL = 'https://www.vitoria-gasteiz.org'

# Setup Main Entity Legal Url (if empty we hide the link)
MAIN_ENTITY_LEGAL_URL = 'https://www.vitoria-gasteiz.org/we001/was/we001Action.do?aplicacion=wb021&tabla=contenido&uid=u_1dc1e845_14a0e91afa2__7e40&accion=contenido'

# Setup Main Entity Legal Url (if empty we hide the link)
MAIN_ENTITY_PRIVACY_URL = 'https://www.vitoria-gasteiz.org/we001/was/we001Action.do?aplicacion=wb021&tabla=contenido&uid=u_1dc1e845_14a0e91afa2__7e3e&accion=contenido'

# External URL for Cookies Policy (if empty we use out template page/cookies.html)
COOKIES_URL = 'https://www.vitoria-gasteiz.org/we001/was/we001Action.do?aplicacion=wb021&tabla=contenido&uid=u60c04389_144007bfb26__7fc5'

# We can define additional URLs applicable only to the theme. These will get added
# to the project URL patterns list.
# Must be needed to uncomment 3rd line in order to import i18n_patterns
# EXTRA_URLS = i18n_patterns('presupuesto-base.views',
#     url(r'^visita-guiada$', 'guidedvisit', name="guidedvisit"),
# )


# Welcome Settings
# ----------------------

# Programmes to feature as example in home page.
FEATURED_PROGRAMMES = ['1621', '1711', '3381', '2411', '3111']

# Number of programmes to feature in home page. Default: 3
# NUMBER_OF_FEATURED_PROGRAMMES = 3


# Overview Settings
# ----------------------

# Use new Sankey visualization or the old one. Default: False
OVERVIEW_USE_NEW_VIS = True

OVERVIEW_INCOME_NODES = ['42', '11', '31', '34', '13', '41']

OVERVIEW_EXPENSE_NODES = ['92', '23', '16', '13', '33', '15', '44', '17', '34']

# How much padding between Sankey nodes. Default: 2 (Optional)
# OVERVIEW_NODE_PADDING = 2

# Overview node minimum height to show labels. Default: 16 (Optional)
# OVERVIEW_LABELS_MIN_SIZE = 16

# Overview node labels minimum font size. Default: 11 (Optional)
OVERVIEW_LABELS_FONT_SIZE_MIN = 13

# Overview node labels maximum font size. Default: 11 (Optional)
OVERVIEW_LABELS_FONT_SIZE_MAX = 42

# Nodes ordered by amount by default. If set to True keeps the order defined in nodes array. Default: False (Optional)
# OVERVIEW_FORCE_ORDER = False


# Show Subtotals panel in Overview. Default: False
# SHOW_OVERVIEW_SUBTOTALS = True

# Calculate budget indicators (True), or show/hide the ones hardcoded in HTML (False). Default: True.
CALCULATE_BUDGET_INDICATORS = False


# Treemap Settings
# ----------------------

# Treemaps minimum height or width to show labels. Default: 30 (Optional)
# TREEMAP_LABELS_MIN_SIZE = 30

# Treemap minimum font size. Default: 11 (Optional)
# TREEMAP_LABELS_FONT_SIZE_MIN = 11

# Treemap use max value between tabs to calculate size. Default: True
# TREEMAP_GLOBAL_MAX_VALUE = False

# Allow overriding of default treemap color scheme
# COLOR_SCALE = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#e7969c', '#bcbd22', '#17becf']

# How many levels to show in the global institutional treemap? Default: 1.
# INSTITUTIONAL_MAX_LEVELS = 2

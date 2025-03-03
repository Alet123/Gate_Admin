from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.login, name='login'),

    path('graphs/', views.graph_view, name='graph_view'),
    path('home/', views.home, name='home'),  # Added trailing slash
    path('trade_graph/', views.trade_graph, name='trade_graph'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('trading_accounts/', views.trading_accounts, name='trading_accounts'),
    path('create_trading_accounts/', views.create_trading_accounts, name='create_trading_accounts'),
    path('group_accounts/', views.group_accounts, name='group_accounts'),
    path('create_group_accounts/', views.create_group_accounts, name='create_group_accounts'),
    path('master_accounts/', views.master_accounts, name='master_accounts'),
    path('create_master_accounts/', views.create_master_accounts, name='create_master_accounts'),
    path('api/', views.api, name='api'),
]

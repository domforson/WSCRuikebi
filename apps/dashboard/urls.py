# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present Kyle
"""

from django.urls import path, re_path
from apps.dashboard import views
from apps.dashboard.views import AccountListView, AccountView, FacilityListView, FacilityView, PriceView, PriceListView, LockView, get_lock_info

urlpatterns = [

    path('/account/list', AccountListView.as_view(), name='dashboard_account_list'),
    path('/account', AccountView.as_view()),
    path('/account/<int:id>', AccountView.as_view(), name="dashboard_account"),
    path('/facility/list', FacilityListView.as_view(), name='dashboard_facility_list'),
    path('/facility', FacilityView.as_view()),
    path('/facility/<int:id>', FacilityView.as_view(), name='dashboard_facility'),
    path('/facility/<int:fid>/price/list', PriceListView.as_view(), name='dashboard_facility_price_list'),
    path('/facility/<int:fid>/price', PriceView.as_view()),
    path('/facility/<int:fid>/price/<int:pid>', PriceView.as_view(), name='dashboard_facility_price'),
    path('/facility/<int:fid>/lock', LockView.as_view()),
    path('/facility/<int:fid>/lock/info', get_lock_info, name='dashboard_lock_info'),

    # # Matches any html file
    re_path(r'^.*\.*', views.pages, name='dashboard_pages'),

]
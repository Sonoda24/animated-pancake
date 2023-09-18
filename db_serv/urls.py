# -*- coding: utf-8 -*-
"""
Created on Sat May 30 10:17:22 2020

@author: user
"""
from django.urls import path
#from . import views

from .views import views
from .views import views2
#from .views import func3

from django.conf import settings

from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve  #Debug止める時に追加
from django.urls import re_path

#app_name = 'db_serv' 
#上記を取るとWARNINGS:?: (urls.W005) が消えるが？？？

urlpatterns = [
    path('', views.index, name='index'),
    path('set_shipment/', views.set_shipment, name='set_shipment'),
    path('nlist', views.nlist,name='nlist'),
    path('new_list/', views.new_list, name='new_list'),
    path('new_list_parms/<str:keys>', views.new_list_parms, name='new_list_parms'),
    path('get_new_list/', views.get_new_list, name='get_new_list'),
    path('after_key_change/', views.after_key_change, name='after_key_change'),
    path('get_new_list_first/', views.get_new_list_first, name='get_new_list_first'),    
    path('get_new_page/', views.get_new_page, name='get_new_page'),
    path('new_list_shipment/', views.new_list_shipment, name='new_list_shipment'),
    path('keyindex_change/<str:keys>', views.keyindex_change, name='keyindex_change'),
    path('get_combo/', views.get_combo, name='get_combo'),
    path('get_rec/', views.get_rec, name='get_rec'),
    path('del_rec/', views.del_rec, name='del_rec'),
    path('detail', views.detail, name='detail'),
    path('editor/<str:data_id>/', views.editor, name='editor'),
    path('editor_shipment/<int:data_id>/', views.editor_shipment, name='editor_shipment'),
    path('update/', views.update, name='update'),
    path('update_sys/', views.update_sys, name='update_sys'),
    path('get_timing/', views.get_timing, name='get_timing'),
    path('newrec/', views.newrec, name='newrec'),
    path('copynew/', views.copynew, name='copynew'),
    path('save_cnsvg/', views.save_cnsvg, name='save_cnsvg'),
    path('get_cnsvg/', views.get_cnsvg, name='get_cnsvg'),
    path('upload_csv_todb/', views.upload_csv_todb, name='upload_csv_todb'),
    path('setup_csv_record/', views.setup_csv_record, name='setup_csv_record'),
    path('upload_add_formatcsv/', views.upload_add_formatcsv, name='upload_add_formatcsv'),
    path('upload_create/', views.upload_create, name='upload_create'),
    path('upload_init/', views.upload_init, name='upload_init'),
    path('upload_add/', views.upload_add, name='upload_add'),
    path('collect_rec/', views.collect_rec, name='collect_rec'),
    path('download_from_tocsv/',views.download_from_tocsv, name='download_from_tocsv'),
    path('download_recs/', views.download_recs, name='download_recs'),
    path('sql_download/', views.sql_download, name='sql_download'),
    path('sql_reject_parms/<str:parm>/', views.sql_reject_parms, name='sql_reject_parms'),
    path('sql_extract_parms/<str:parm>/', views.sql_extract_parms, name='sql_extract_parms'),
    #path('prepare_system/', views.prepare_system, name='prepare_system'), 既に不要
    path('save_all/', views.save_all, name='save_all'),
    path('get_page/', views.get_page, name='get_page'),
    path('get_index/', views.get_index, name='get_index'),
    path('mod_index/', views.mod_index, name='mod_index'),
    path('make_index/', views.make_index, name='make_index'),
    path('resolve_index/', views.resolve_index, name='resolve_index'),
    path('ai_image/', views.ai_image, name='ai_image'),
    path('showall/', views.showall, name='showall'),
    path('imageupload/', views.imageupload, name='imageupload'),
    path('imagedownload/', views.imagedownload, name='imagedownload'),
    path('download/<int:data_id>/', views.download, name='download'),
    path('image_down/', views.My_ImageList.as_view(), name='image_down'),
    path('get_mylist/', views.get_mylist, name='get_mylist'),
    path('get_mylist2/', views.get_mylist2, name='get_mylist2'),
    path('get_testchar/', views.get_testchar, name='get_testchar'),
    #path('get/', views.My_ImageList.as_view(), name='get'),
    path('pagenation/', views.pagenation, name='pagenation'),
    path('mail_to/', views2.mail_to, name='mail_to'),
    path('display/', views.display, name='display'),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
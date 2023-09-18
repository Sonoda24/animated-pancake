# -*- coding: utf-8 -*-
"""
Created on Sat May 30 10:17:22 2020

@author: user
"""
# Create your views here.
from django.http import HttpResponseRedirect
from django.template import Context, loader
from django.shortcuts import render, redirect

from django.http import HttpResponse
from django.http import Http404
from django.http import HttpResponseBadRequest, JsonResponse

# -----------------------------------------------------------------
def mail_to(request):
    from django.core.mail import EmailMessage
    #from django.core.mail import EmailMultiAlternatives
    
    doc_type = request.POST.get("type")
    title = request.POST.get("title")
    addr_list = request.POST.get("addr_list")
    text_content=request.POST.get("comment")
    html_dat = request.POST.get("html_dat")
    
    #print(doc_type,title,addr_list)
    fp = open('templates/db_serv/mail_template/sample.html','w',encoding='utf-8')
    fp.write(html_dat)
    fp.close()

    # 表題
    subject = title
    # 送信元
    from_email = "yzr.sonoda@gmail.com"
    # 送信先
    recipient_list=recs_decompose(addr_list)
    print('addr_list=',recipient_list)
    mail = EmailMessage(subject, text_content, from_email, recipient_list)
    mail.attach_file('templates/db_serv/mail_template/sample.html')
    mail.send()
    
    return HttpResponse('mail success')
# ------------------------------------------------------------------
def recs_decompose(tags):
    import re

    spltchar=re.split('[,;]',tags)
    
    return spltchar
#
# ------------------------------------------------------------------
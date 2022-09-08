import os
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['20.168.13.107', 'http://20.168.13.107' ]

DATABASES = {

    'default': {
        'ENGINE': 'mssql',
        'NAME': 'CONTROLCLIENTES2018',
        'HOST': '190.116.178.164',
        'USER': 'usr_solmar_vb',
        'PASSWORD': '11hotelbravo',
        'PORT': '1433',
	'OPTIONS': {
		'driver': 'ODBC Driver 17 for SQL Server',
	}
    }
}

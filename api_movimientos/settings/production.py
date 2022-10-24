import os
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['54.221.148.178', 'http://54.221.148.178' ]

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
    },

    'test_solmar': {
        'ENGINE': 'mssql',
        'NAME': 'TestSolmar',
        'HOST': '190.116.178.164',
        'USER': 'usr_solmar_vb',
        'PASSWORD': '11hotelbravo',
        'PORT': '1433',
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
        }
    },

    'bd_hayduk': {
        'ENGINE': 'mssql',
        'NAME': 'CONTROLHAYDUK_2019',
        'HOST': '190.116.178.164',
        'USER': 'usr_solmar_vb',
        'PASSWORD': '11hotelbravo',
        'PORT': '1433',
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
        }
    },

    'bd_tasa': {
        'ENGINE': 'mssql',
        'NAME': 'CONTROTASA2018',
        'HOST': '190.116.178.164',
        'USER': 'usr_solmar_vb',
        'PASSWORD': '11hotelbravo',
        'PORT': '1433',
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
        }
    },

}

# About
This project is Zhe Liu's thesis of my bachelor's degree for Zhejiang University.<br>
Any use without prior notice is not allowed.

# Running on server
 uwsgi --http :8000 --chdir /root/dataMining/ -w djangoData.wsgi
ALLOWED_HOSTS = ['39.105.54.42']

-STATIC_URL = '/static/'
+STATIC_URL = '/polls/static/'
+STATIC_ROOT = '/root/dataMining/polls/static/'

# TODO
Add file download <br>
Add descirption for Different method

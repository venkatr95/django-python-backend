# Python Django REST API Example
This project explains how to Build and Test A Django CRUD Rest API using SQLite and Pytest.

# Requirements
* Python (3.10.11)

Install the dependencies via the `requirements.txt` using 
```commandline
pip install -r requirements.txt
```


# Run the tests
To run the Unit Tests, from the root of the repo run
```commandline
pytest tests/unit/test_notes.py -v -s
```

# Swagger
```commandline
pip install drf-yasg
```

Add these below lines in settings.py under INSTALLED_APPS
'django.contrib.staticfiles',  # required for serving swagger ui's css/js files
'drf_yasg'

Add this in the notes/urls.py
### Quick Start Example:
```python
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Notes API",
      default_version='v1',
      description="Notes API description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@notes.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/notes/", include('notes_api.urls')),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
]
```

This exposes 4 endpoints:

* A JSON view of your API specification at ``/swagger.json``
* A YAML view of your API specification at ``/swagger.yaml``
* A swagger-ui view of your API specification at ``/swagger/``
* A ReDoc view of your API specification at ``/redoc/``

### Jenkins Integration with Django
```commandline
pip install django-jenkins
```
* Add django_jenkins to INSTALLED_APPS
* Run python manage.py jenkins
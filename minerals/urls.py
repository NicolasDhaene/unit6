from django.conf.urls import url
from . import views
urlpatterns = [
    url(r"upload/", views.add_json_to_db, name="upload"),
    url(r"^$", views.mineral_list, name="index"),
    url(r"(?P<pk>\d+)/$", views.mineral_detail, name="detail"),

]
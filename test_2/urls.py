from django.urls import path
from test_2.views import view_1, view_2, view_3

urlpatterns = [
    path('view1/', view_1),
    path('view2/', view_2),
    path('view3/', view_3)
]

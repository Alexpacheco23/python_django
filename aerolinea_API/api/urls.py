from django.url import patch

urlpatterns=[
    path ('companies/',companyView.as_view(),name='companies_list')
]
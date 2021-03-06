from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url(r'^$',views.home_images,name = 'homePage'),
    url(r'^new/image$',views.new_image,name = 'new_image'),
    url(r'^edit/profile$',  views.profile_edit,name='profile_edit'),
    url(r'^myprofile/$',  views.profilemy,name='profilemy'),
    # url(r'^search/', views.search_results, name='search_results'),
    url(r'^comment/(\d+)/$', views.add_comment, name='comment'),
    url(r'^likes/(?P<id>\d+)',views.likes,name="like"),
    url(r'^search/',  views.search_results,name='search_results'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

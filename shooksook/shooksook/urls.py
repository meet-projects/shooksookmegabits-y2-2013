from django.conf.urls import patterns, include, url
from main import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.home, name='home'),
    url(r'^home$', views.home, name='home'),
    url(r'^stores$', views.stores, name = 'stores'),
    url(r'^maps$', views.maps, name = 'maps'),
    url(r'^restaurants$', views.restaurants, name = 'restaurants'),
    url(r'^introduction$', views.introduction, name = 'introduction'),
    url(r'^media$', views.media, name = 'media'),

    url(r'^login$', views.showlogin, name = 'login'),
    url(r'^submitlogin$', views.submitlogin, name = 'submitlogin'),
    url(r'^profile$', views.profile, name = 'profile'),

    url(r'^register$', views.register, name = 'register'),
    url(r'^log_me_out/$', 'django.contrib.auth.views.logout', {'next_page': '/home'}),

    url(r'^submitBusiness$', views.submitBusiness, name = 'submitBusiness'),
    url(r'^submitBusiness_accepted$', views.submitBusiness_accepted, name = "submitBusiness_accepted"),
    url(r'^success$', views.success, name = "success"),

    url(r'^about$', views.about, name = 'about'),
    url(r'^contact$', views.contact, name = 'contact'),
    #url(r'^shooksook/', include('shooksook.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
)

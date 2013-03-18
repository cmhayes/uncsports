from django.conf.urls.defaults import patterns, url

from basketball import views

urlpatterns = patterns('',
	url(r'^$', views.home, name='sports_home'),
	url(r'^team/(?P<pk>\d+)$', views.team, name='mens_basketball'),
	url(r'^player/(?P<pk>\d+)$', views.player, name='mens_basketball_players'),
	)	
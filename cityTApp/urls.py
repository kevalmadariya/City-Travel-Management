from django.urls import path
from.import views

urlpatterns = [
    path('dummy',views.dummy,name='dummy'),

    path('',views.index,name='index'),
    path('index',views.index,name='index'),
    path('regi',views.registration,name='registration'),
    path('u_regi',views.user_registration,name='user_registration'),
    path('a_regi',views.agent_registration,name='agent_registration'),
    path('u_login',views.user_login,name='user_login'),
    path('a_login',views.agent_login,name='agent_login'),
    path('logout',views.log_out,name='log_out'),
    path('addpack',views.add_trip_plan,name='add_trip_plan'),
    path('pack',views.package_view,name='package_view'),
    path('viewpack',views.package_view,name='package_view'),
    path('trip_details/<int:pack_id>',views.view_trip_details,name='view_trip_details'),
    # path('make_session',views.make_session_for_att,name='make_session_for_att'),
    path('add_att',views.add_att,name='add_att'),
    path('del_att/<int:id>',views.del_att,name='del_att'),
    path('edit_att/<int:id>',views.edit_att,name='edit_att'),

    path('agentspack',views.view_agent_pack,name='view_agent_pack'),
    path('edit_pack/<int:id>',views.edit_pack,name='edit_pack'),
    path('del_pack/<int:id>',views.del_pack,name='del_pack'),    

    path('trip_details/booking/<int:id>',views.booking,name='booking'),
    path('add_passenger',views.add_passenger,name='add_passenger'),
    path('edit_passenger/<int:id>',views.edit_passenger,name='edit_passenger'),
    path('del_passenger/<int:id>',views.del_passenger,name='del_passenger'),

    path('pay',views.pay,name='pay'),
    path('success',views.success,name='succsess'),
    path('ticket_view',views.ticket_view,name='ticket_view'),
    path('download',views.download,name='download'),

    
    path('about',views.about,name='about'),
    path('service',views.service,name='service'),
]
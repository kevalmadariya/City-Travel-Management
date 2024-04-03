from django.contrib import admin
from .models import TripPlan,Agent,User,Passenger,Attraction,Ticket
# Register your models here.

admin.site.register(TripPlan)
admin.site.register(Agent)
admin.site.register(User)
admin.site.register(Attraction)
admin.site.register(Passenger)
admin.site.register(Ticket)
# admin.site.register(tempTicket)
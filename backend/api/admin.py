from django.contrib import admin
from api.models.user import User
from api.models.notification import Notification
from api.models.meal import Meal

admin.site.register(User)
admin.site.register(Notification)
admin.site.register(Meal)

from django.contrib import admin
from .models import UserDetails,RoleDetail,Course,Lesson,Lesson_Topic,CareerCategory,CFP_role,UserContact
# Register your models here.

admin.site.register(UserDetails)
admin.site.register(RoleDetail)
admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Lesson_Topic)
admin.site.register(CareerCategory)
admin.site.register(CFP_role)
admin.site.register(UserContact)

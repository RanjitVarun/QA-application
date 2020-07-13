from django.contrib import admin

from .models import UserDetails,Email,Mobile,Education,EducationRelUser,Course,Board, OfficeAddress,ResAddress,Skillset,skillsetRel

admin.site.register(UserDetails)
admin.site.register(Email)
admin.site.register(Mobile)
admin.site.register(OfficeAddress)
admin.site.register(ResAddress)
admin.site.register(Course)
admin.site.register(Board)
admin.site.register(Education)
admin.site.register(EducationRelUser)
admin.site.register(Skillset)
admin.site.register(skillsetRel)

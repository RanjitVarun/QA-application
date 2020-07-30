from django.contrib import admin
from usereducationskill.models import Education,Board,Course, EducationRelUser,Skillset,skillsetRel

admin.site.register(EducationRelUser)
admin.site.register(Education)
admin.site.register(Board)
admin.site.register(Course)
admin.site.register(skillsetRel)
admin.site.register(Skillset)

from django.contrib import admin
import userdetails.models as userdetailmodels

admin.site.register(userdetailmodels.Email)
admin.site.register(userdetailmodels.Mobile)
admin.site.register(userdetailmodels.OfficeAddress)
admin.site.register(userdetailmodels.ResAddress)

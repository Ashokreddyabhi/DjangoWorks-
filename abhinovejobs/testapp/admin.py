from django.contrib import admin
from testapp.models import HydJobs,BengJobs,ChennaiJobs
class HydJobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','eligibility','address','email','phonenumber']
admin.site.register(HydJobs,HydJobsAdmin)
class BengJobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','eligibility','address','email','phonenumber']
admin.site.register(BengJobs,BengJobsAdmin)
class ChennaiJobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','eligibility','address','email','phonenumber']
admin.site.register(ChennaiJobs,ChennaiJobsAdmin)

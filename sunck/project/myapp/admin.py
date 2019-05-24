from django.contrib import admin

# Register your models here.
from .models import Grades,Students

#注册
class StudentsInfo(admin.TabularInline):
    model = Students
    extra = 2
class GradesAdmin(admin.ModelAdmin):
    #列表属性
    list_display =['pk','gname','gdate','ggirlnum','gboynum']
    list_filter = ['gname']
    list_per_page =5
    search_fields = ['gname']
    # fields = []
    # fieldsets = []


admin.site.register(Grades,GradesAdmin)


admin.site.register(Students)


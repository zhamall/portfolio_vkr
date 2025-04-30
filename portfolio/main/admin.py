from django.contrib import admin
from .models import Tag, Project, ProjectImage, Resume, ResumeImage, ResumeLink

# Register your models here.

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1

class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "link")
    inlines = [ProjectImageInline]
    search_fields = ("title", "description")
    list_filter = ("tags",)

class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

class ResumeImageInline(admin.TabularInline):
    model = ResumeImage
    extra = 1

class ResumeLinkInline(admin.TabularInline):
    model = ResumeLink
    extra = 1
    fields = ('name', 'url')  

class ResumeAdmin(admin.ModelAdmin):
    list_display = ("name", "surname", "email")
    inlines = [ResumeImageInline, ResumeLinkInline]
    search_fields = ("name", "surname", "email")
    
    # Убираем кнопку "Добавить" из списка
    def has_add_permission(self, request):
        return False
    
    # Убираем кнопку "Добавить" из формы редактирования
    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['show_save_and_add_another'] = False
        extra_context['show_save_and_continue'] = False
        return super().change_view(request, object_id, form_url, extra_context)
    
    # Убираем кнопку удаления
    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Tag, TagAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectImage)
admin.site.register(Resume, ResumeAdmin)
admin.site.register(ResumeImage)
admin.site.register(ResumeLink)
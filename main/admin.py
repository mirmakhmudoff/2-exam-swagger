from django.contrib import admin
from .models import About, News, TeamMember, Publication, Review, Search, Service, Contact


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'short_description', 'view_count')
    search_fields = ('title', 'short_description')
    list_filter = ('view_count',)


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'position')
    search_fields = ('first_name', 'last_name', 'position')
    list_filter = ('position',)


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ('title', 'team_member')
    search_fields = ('title',)
    list_filter = ('team_member',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('service_id', 'full_name', 'is_active')
    search_fields = ('full_name', 'description')
    list_filter = ('is_active',)


@admin.register(Search)
class SearchAdmin(admin.ModelAdmin):
    list_display = ('content_type', 'id')
    search_fields = ('content_type',)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'view_count')
    search_fields = ('title',)
    list_filter = ('view_count',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')
    search_fields = ('name', 'email')
    list_filter = ('email',)

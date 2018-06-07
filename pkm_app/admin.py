# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import ugettext_lazy as _
from .models import User,Setupuser
from  .forms import Set_User_Form

@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    """Define admin model for custom User model with no email field."""

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ('email','username','phone_number', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)

class SetupuserAdmin(admin.ModelAdmin):
    form = Set_User_Form
    list_display = ('your_organization', 'email_id', 'your_designation','your_job_level','your_phone_no','your_nickname')#,"emails_for_help")
admin.site.register(Setupuser, SetupuserAdmin)

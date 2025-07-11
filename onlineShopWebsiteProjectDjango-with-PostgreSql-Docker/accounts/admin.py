from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomeUserChangeForm, CustomeUserCreationForm
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomeUserCreationForm
    form = CustomeUserChangeForm
    list_display = ('email', 'username', )

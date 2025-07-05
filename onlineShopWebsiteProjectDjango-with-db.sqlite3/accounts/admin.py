from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomeUserCreationForm, CustomeUserChangeForm
from .models import CustomeUser


@admin.register(CustomeUser)
class CustomUserAdmin(UserAdmin):
    model = CustomeUser
    add_form = CustomeUserCreationForm
    form = CustomeUserChangeForm
    list_display = ('email', 'username')


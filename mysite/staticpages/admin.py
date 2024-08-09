from django.contrib import admin
from .models import RegistroDeUso
from django.contrib.auth.models import User, Group

@admin.register(RegistroDeUso)
class RegistroDeUsoAdmin(admin.ModelAdmin):
    list_display = ('modelo_veiculo', 'placa', 'destino', 'hora_saida', 'km_saida', 'hora_chegada', 'km_chegada')
    search_fields = ('modelo_veiculo', 'placa', 'destino')


def add_users_to_group(modeladmin, request, queryset):
    # Substitua 'group_name' pelo nome do grupo desejado
    group = Group.objects.get(name='Suporte')

    for user in queryset:
        user.groups.add(group)
    modeladmin.message_user(request, f"Usuários adicionados ao grupo '{group.name}' com sucesso.")


add_users_to_group.short_description = 'Adicionar usuários ao grupo'


class UserAdmin(admin.ModelAdmin):
    actions = [add_users_to_group]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin

class UserAdmin(DefaultUserAdmin):
    # Exibindo os campos básicos e a seção de ações
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'email'),
        }),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

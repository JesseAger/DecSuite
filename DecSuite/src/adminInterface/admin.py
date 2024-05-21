from django.contrib import admin

from .models import FirewallRule

@admin.register(FirewallRule)
class FirewallRuleAdmin(admin.ModelAdmin):
    list_display = ('rule_type', 'ip_address', 'created_at')
    search_fields = ('ip_address', 'description')
    list_filter = ('rule_type', 'created_at')

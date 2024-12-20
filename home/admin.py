from django.contrib import admin
from .models import Payment, Team
from django.utils.timezone import now

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        'client_txn_id', 'user', 'amount', 'status', 'transaction_date'
    )
    list_filter = ('status', 'transaction_date')
    search_fields = ('client_txn_id', 'user__username', 'user__email')
    date_hierarchy = 'transaction_date'
    ordering = ('-transaction_date',)

    fieldsets = (
        ("Transaction Details", {
            'fields': ('client_txn_id', 'user', 'amount', 'status')
        }),
        ("Additional Information", {
            'fields': ('transaction_date', 'extra_data'),
            'classes': ('collapse',),
        }),
    )

    readonly_fields = ('transaction_date',)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.select_related('user')

    def save_model(self, request, obj, form, change):
        if not change:
            obj.transaction_date = now()
        super().save_model(request, obj, form, change)

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'team_leader', 'player_two', 'player_three', 'player_four', 'user')  # Fields to display in the list view
    search_fields = ('name', 'team_leader', 'player_two', 'player_three', 'player_four')  # Fields to include in the search bar
    list_filter = ('user',)  # Filter options in the sidebar
    ordering = ('name',)  # Default ordering of the records
    fieldsets = (
        ('Team Information', {
            'fields': ('name', 'user')
        }),
        ('Players', {
            'fields': ('team_leader', 'player_two', 'player_three', 'player_four')
        }),
    )  # Grouping fields into sections

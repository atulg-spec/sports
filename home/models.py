from django.db import models
from accounts.models import CustomUser
from django.utils.timezone import now

class Payment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="payments")
    client_txn_id = models.CharField(max_length=20, unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[("success", "Success"), ("failure", "Failure"), ("pending", "Pending")], default="pending")
    transaction_date = models.DateTimeField(default=now)
    extra_data = models.JSONField(null=True, blank=True)

    def __str__(self):
        return f"Transaction {self.client_txn_id} ({self.status})"

class Team(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="teams")
    name = models.CharField(max_length=255, unique=True)
    team_leader = models.CharField(max_length=255)
    player_two = models.CharField(max_length=255)
    player_three = models.CharField(max_length=255)
    player_four = models.CharField(max_length=255)

    def __str__(self):
        return self.name
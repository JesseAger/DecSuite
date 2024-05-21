from django.db import models

# Create your models here.

class FirewallRule(models.Model):
    RULE_TYPE_CHOICES = [
        ('ALLOW', 'Allow'),
        ('BLOCK', 'Block'),
    ]

    rule_type = models.CharField(max_length=10, choices=RULE_TYPE_CHOICES)
    ip_address = models.GenericIPAddressField()
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.rule_type} - {self.ip_address}"

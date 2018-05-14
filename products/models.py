from django.db import models

class Products(models.Model):
    merchant = models.CharField(max_length=26, null=True)
    #price = models.DecimalField(max_digits=9, decimal_places=2)
    funder = models.CharField(max_length=100, null=True)
    tranDate = models.DateField(auto_now_add = False, null=True)
    fundAmt = models.CharField(max_length=100, null=True)
    broker = models.CharField(max_length=100, null=True)
    lead = models.CharField(max_length=100, null=True)
    note = models.CharField(max_length=100, null=True)

    CONTRACT_OUT = 'CONTRACT OUT'
    SIGNED_CONTRACT = 'SIGNED CONTRACT'
    FUNDED = 'FUNDED'

    DEAL_STATUS = (
        (CONTRACT_OUT, 'contract out'),
        (SIGNED_CONTRACT, 'signed contract'),
        (FUNDED, 'funded'),
    )

    dealStatus = models.CharField(max_length=15, choices=DEAL_STATUS, default=CONTRACT_OUT)

    def __str__(self):
        return self.merchant

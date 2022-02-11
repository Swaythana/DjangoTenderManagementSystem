from django import forms
from contractor.models import Tender

class TenderForm(forms.ModelForm):
    class Meta:
        model=Tender
        fields=['Tendername','ContractorName','Baseprice','Deadline']

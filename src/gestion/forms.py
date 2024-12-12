from django import forms

from .models import Usuario, Transaccion, Informe


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = "__all__"


class TransaccionForm(forms.ModelForm):
    class Meta:
        model = Transaccion
        fields = "__all__"
        widgets = {
            "fecha": forms.DateInput(attrs={"type": "date"}),
        }


class InformeForm(forms.ModelForm):
    class Meta:
        model = Informe
        fields = "__all__"
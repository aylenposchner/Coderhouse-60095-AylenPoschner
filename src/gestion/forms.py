from django import forms

from .models import Usuario, Transaccion, Informe


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = "__all__"
        widgets = {
            "fecha_nacimiento": forms.DateInput(attrs={"type": "date"}),
        }


class TransaccionForm(forms.ModelForm):
    class Meta:
        model = Transaccion
        fields = "__all__"
        widgets = {
            "fecha": forms.DateInput(attrs={"type": "date"}),
        }
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        # Si el usuario no es staff, predefinir el campo 'nombre' con el usuario actual
        if not user.is_staff:
            self.fields['nombre'].initial = user  # Establecer el usuario actual
            self.fields['nombre'].widget.attrs['readonly'] = 'readonly'  # Hacer el campo no editable


class InformeForm(forms.ModelForm):
    class Meta:
        model = Informe
        fields = "__all__"
        
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        # Si el usuario no es staff, predefinir el campo 'nombre' con el usuario actual
        if not user.is_staff:
            self.fields['nombre'].initial = user  # Establecer el usuario actual
            self.fields['nombre'].widget.attrs['readonly'] = 'readonly'  # Hacer el campo no editable
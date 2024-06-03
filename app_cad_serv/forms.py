from django import forms
from .models import Servidor, TarefaRealizada
from django.core.validators import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Usuario, Pessoa

class ServidorForm(forms.ModelForm):

    class Meta:
        model = Servidor
        fields = ['nome', 'matricula', 'tipo_escala', 'escala', 'pontualidade', 'assiduidade', 'execucao_tarefas', 'iniciativa', 'atendimento_servicos', 'tipo_modalidade', 'mes_referencia', 'setor', 'teste_tarefas']
        labels = {
            'execucao_tarefas': 'Execução de Tarefas',
            'atendimento_servicos': 'Atendimento de Serviços',
            'mes_referencia': 'Data de Referencia',
            'teste_tarefas': 'Tarefas Executadas'
        }
        widgets = {
            'nome': forms.TextInput(attrs={'style': 'width: 270px;'}),
            'mes_referencia': forms.DateInput(attrs={'type': 'date'}),
            'teste_tarefas': forms.Textarea(attrs={'rows': 5, 'cols': 55}),
            'matricula': forms.TextInput(attrs={'style': 'width: 80px;'}),
        }
        
        
        

    


class TarefaRealizadaForm(forms.ModelForm):
    class Meta:
        model = TarefaRealizada
        fields = ['diretor_coordenador', 'tarefas']
        labels = {
            'diretor_coordenador': 'Diretor/Coordenador',
        }

    def clean_tarefas(self):
        tarefas = self.cleaned_data.get('tarefas')
        if len(tarefas) < 15:
            raise ValidationError('O campo tarefas deve ter no mínimo 15 caracteres.')
        return tarefas
    
    
class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=150, required=True, label='Nome de Usuario')

    def clean_username(self):
        username = self.cleaned_data['username']
        if Usuario.objects.filter(username=username).exists():
            raise forms.ValidationError('Este nome de usuário já está em uso. Escolha outro.')
        return username
    
    class Meta:
        model = Usuario
        fields = ['username', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user

class LoginForm(AuthenticationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'password']
        password = forms.CharField(label="Senha", widget=forms.PasswordInput)
        
        
class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ['nome', 'pessoa_mat']
        labels = {
            'pessoa_mat': 'Matrícula do Servidor',
        }

    def clean_pessoa(self):
        pessoa = self.cleaned_data.get('pessoa')
        if len(pessoa) < 10:
            raise ValidationError('O Nome do Servidor deve conter no minimo 10 caracteres.')
        return pessoa    
        



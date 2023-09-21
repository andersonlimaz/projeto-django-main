from django import forms
from .models import Doar

class modelform(forms.ModelForm):
    class Meta:
        model = Doar
        fields = ['valor_doacao','nome', 'email', 'sexo', 'data_nascimento', 'telefone', 'cpf' ]

class MeuFormulario(forms.Form):
    transaction_code = forms.CharField(widget=forms.HiddenInput())
    ip = forms.CharField(widget=forms.HiddenInput())
    country = forms.CharField(widget=forms.HiddenInput())
    due_date = forms.CharField(widget=forms.HiddenInput())
    variant = forms.CharField(widget=forms.HiddenInput())
    
    donation_option = forms.ChoiceField(choices=[('1', 'R$ 19,90'), ('2', 'R$ 34,90'), ('3', 'R$ 64,90'), ('4', 'R$ 50,00 - Doar Meia Cesta de Alimentos'), ('5', 'R$ 100,00 - Doar 1 Cesta de Alimentos'), ('6', 'R$ 90,00 - Doar 1 Kit Escolar'), ('-1', 'Outros valores')], widget=forms.Select(attrs={'class': 'form-control form-control--donation_option donation_option input-lg input-not-radius float-label'}))
    periodicity = forms.ChoiceField(choices=[('1', 'Uma Única Vez'), ('2', 'Todos os Meses')], widget=forms.Select(attrs={'class': 'form-control form-control--periodicity periodicity input-lg input-not-radius float-label'}))
    amount = forms.DecimalField(widget=forms.TextInput(attrs={'class': 'form-control form-control--amount amount input-lg input-not-radius float-label', 'placeholder': 'Valor'}))
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control--name name input-lg input-not-radius float-label', 'placeholder': 'Nome Completo'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control form-control--email email input-lg input-not-radius float-label', 'placeholder': 'E-mail'}))
    gender = forms.ChoiceField(choices=[('1', 'Masculino'), ('2', 'Feminino')], widget=forms.Select(attrs={'class': 'form-control form-control--gender gender input-lg input-not-radius float-label'}))
    birthday = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control--birthday birthday input-lg input-not-radius float-label', 'placeholder': 'Data de nascimento'}))
    telephone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control--telephone telephone input-lg input-not-radius float-label', 'placeholder': 'Telefone'}))
    cpf = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control--cpf cpf input-lg input-not-radius float-label', 'placeholder': 'CPF'}))
    payment = forms.ChoiceField(choices=[('', 'Forma de pagamento')], widget=forms.Select(attrs={'class': 'form-control form-control--payment payment input-lg input-not-radius float-label'}))
    credit_card_flag = forms.ChoiceField(choices=[('', 'Bandeira')], widget=forms.Select(attrs={'class': 'form-control form-control--credit_card_flag credit_card_flag input-lg input-not-radius float-label'}))
    credit_card = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control--credit_card credit_card input-lg input-not-radius float-label', 'placeholder': 'Número'}))
    credit_card_holder = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control--credit_card_holder credit_card_holder input-lg input-not-radius float-label', 'placeholder': 'Nome impresso no Cartão'}))
    credit_card_security_code = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control--credit_card_security_code credit_card_security_code input-lg input-not-radius float-label', 'placeholder': 'Código de Segurança'}))
    credit_card_validity_date = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control--credit_card_validity_date credit_card_validity_date input-lg input-not-radius float-label', 'placeholder': 'Validade'}))
    bank = forms.ChoiceField(choices=[('', 'Banco'), ('41', 'Banrisul'), ('237', 'Bradesco'), ('104', 'Caixa Econômica'), ('33', 'Santander'), ('756', 'Sicoob'), ('748', 'Sicredi'), ('341', 'Itaú'), ('1', 'Banco do Brasil')], widget=forms.Select(attrs={'class': 'form-control form-control--bank bank input-lg input-not-radius float-label'}))
    agency = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control--agency agency input-lg input-not-radius float-label', 'placeholder': 'Agência'}))
    account = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control--account account input-lg input-not-radius float-label', 'placeholder': 'Conta'}))
    zipcode = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control--zipcode zipcode input-lg input-not-radius float-label', 'placeholder': 'CEP da fatura'}))
    lgpd = forms.BooleanField(required=True, widget=forms.CheckboxInput(attrs={'name': 'lgpd'}))

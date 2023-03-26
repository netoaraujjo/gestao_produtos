from django.forms import ModelForm
from .models import Produto

class ProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields = ["nome_produto", "quantidade_estoque", "quantidade_critica", "numero_serie", "marca", "modelo", "foto"]
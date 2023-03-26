from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Produto
from .forms import ProdutoForm

# Create your views here.
@login_required
def detalhe_produto(request, id):
    # produto = get_object_or_404(Produto, pk=id)
    produto = Produto.objects.get(pk=id)
    contexto = {"produto": produto}
    return render(request, "produtos/detalhe_produto.html", contexto)


@login_required
def lista_produtos(request):
    produtos = Produto.objects.all()
    contexto = {"produtos": produtos}
    return render(request, "produtos/lista_produtos.html", contexto)


@login_required
def novo_produto(request):
    form = ProdutoForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('produtos:lista_produtos')

    return render(request, "produtos/novo_produto.html", {"form": form})


@login_required
def editar_produto(request, id):
    produto = get_object_or_404(Produto, pk=id)
    form = ProdutoForm(request.POST or None, request.FILES or None, instance=produto)

    if form.is_valid():
        form.save()
        return redirect("produtos:lista_produtos")
    
    return render(request, "produtos/editar_produto.html", {"form": form})


@login_required
def excluir_produto(request, id):
    produto = get_object_or_404(Produto, pk=id)
    if produto:
        produto.delete()
    return redirect("produtos:lista_produtos")
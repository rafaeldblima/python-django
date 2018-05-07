from django.shortcuts import render, redirect
from perfis.models import Perfil, Convite

from django.contrib.auth.decorators import login_required, permission_required


@login_required
def index(request):
    return render(request, 'index.html', {'perfis': Perfil.objects.all(), 'perfil_logado': get_perfil_logado(request)})


@login_required
def exibir(request, id):
    # print('Id: %s' %id)
    if not request.user.has_perm('perfis.add_convite'):
        return HttpResponseForbidden('Acesso negado')
    perfil = Perfil.objects.get(id=id)
    perfil_logado = get_perfil_logado(request)
    ja_eh_contato = perfil in perfil_logado.contatos.all()
    # if id == 1:
    #     perfil = Perfil('Rafael Lima', 'rafaeldblima@gmail.com',
    #                     '987654321', 'FPF Tech')
    return render(request, 'perfil.html', {"perfil": perfil, 'ja_eh_contato': ja_eh_contato, 'perfil_logado': get_perfil_logado(request)})

@permission_required('perfis.add_convite', raise_exception=True)
@login_required
def convidar(request, id):
    perfil_a_convidar = Perfil.objects.get(id=id)
    perfil_logado = get_perfil_logado(request)
    perfil_logado.convidar(perfil_a_convidar)
    return redirect('index')


@login_required
def aceitar(request, convite_id):
    convite = Convite.objects.get(id=convite_id)
    convite.aceitar()
    return redirect('index')


@login_required
def get_perfil_logado(request):
    return request.user.perfil

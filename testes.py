#!/usr/bin/python3
# coding: utf-8
""" Testes das classes camadas TCP/IP """

from camadas import CamadaFisica
from camadas import CamadaInternet
from camadas import CamadaTransporte
from camadas import CamadaAplicacao

mensagem = "oi mundo"
aplicacao = CamadaAplicacao(mensagem)
transporte = CamadaTransporte(aplicacao)
rede = CamadaInternet(transporte)
fisica = CamadaFisica(rede)

# Checar os retornos / desempasulamentos
assert(fisica.desencapsular() == rede)
assert(rede.desencapsular() == transporte)
assert(transporte.desencapsular() == aplicacao)
assert(aplicacao.desencapsular() == mensagem)

# Checar os tipos retornados
assert(type(fisica.desencapsular()) == CamadaInternet)
assert(type(rede.desencapsular()) == CamadaTransporte)
assert(type(transporte.desencapsular()) == CamadaAplicacao)
assert(type(aplicacao.desencapsular()) == type(mensagem))

# Checar as responsabilidades de cada camada
assert(aplicacao.responsabilidade() == "Responsável pela mensagem do processo")
assert(transporte.responsabilidade() == "Responsável pela comunicação processo-processo")
assert(rede.responsabilidade() == "Responsável pelo roteamento")
assert(fisica.responsabilidade() == "Responsável por troca com o meio físico")

# Diferentes tipos recebidos na camada de Aplicação
mensagem = [1, 2, 3]
aplicacao = CamadaAplicacao(mensagem)
assert(aplicacao.desencapsular() == mensagem)
mensagem = (1, 2, 3)
aplicacao = CamadaAplicacao(mensagem)
assert(aplicacao.desencapsular() == mensagem)

# Checar pacotes mal formados
transporte_com_erro = CamadaTransporte(mensagem)
assert(transporte_com_erro.desencapsular() is None)
rede_com_erro = CamadaInternet(mensagem)
assert(rede_com_erro.desencapsular() is None)
fisica_com_erro = CamadaFisica(mensagem)
assert(fisica_com_erro.desencapsular() is None)

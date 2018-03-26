#!/usr/bin/python3
# coding: utf-8
""" Como as camadas TCP/IP funcionam """

from camadas import CamadaFisica
from camadas import CamadaInternet
from camadas import CamadaTransporte
from camadas import CamadaAplicacao


class Host():

    def __init__(self, mensagem=None):
        if mensagem is not None:
            aplicacao = CamadaAplicacao(mensagem)
            transporte = CamadaTransporte(aplicacao)
            rede = CamadaInternet(transporte)
            self.fisica = CamadaFisica(rede)

    def enviar(self):
        dado = self.fisica
        self.fisica = None
        return dado

    def set_camada_fisica(self, camada_fisica):
        self.fisica = camada_fisica

    def receber(self):
        try:
            mensagem = self.fisica.desencapsular().desencapsular()
            mensagem = mensagem.desencapsular().desencapsular()
            self.fisica = None
            print(mensagem)
        except:
            print("Nenhuma mensagem")


cliente = Host("oi mundo")
servidor = Host()
servidor.receber()
servidor.set_camada_fisica(cliente.enviar())
servidor.receber()
servidor.receber()
cliente = Host("oi mundo 2")
servidor.set_camada_fisica(cliente.enviar())
servidor.receber()

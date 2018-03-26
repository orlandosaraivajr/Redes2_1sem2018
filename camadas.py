#!/usr/bin/python3
# coding: utf-8
""" Classes das camadas TCP/IP """


class CamadaAplicacao():

    def __init__(self, camada):
        self.camada = camada
        # print("Camada TCP/IP: Aplicação")

    def desencapsular(self):
        return self.camada

    def responsabilidade(self):
        return "Responsável pela mensagem do processo"


class CamadaTransporte():

    def __init__(self, camada):
        if type(camada) == CamadaAplicacao:
            self.camada = camada
        else:
            self.camada = None

    def desencapsular(self):
        return self.camada

    def responsabilidade(self):
        return "Responsável pela comunicação processo-processo"


class CamadaInternet():

    def __init__(self, camada):
        if type(camada) == CamadaTransporte:
            self.camada = camada
        else:
            self.camada = None

    def desencapsular(self):
        return self.camada

    def responsabilidade(self):
        return "Responsável pelo roteamento"


class CamadaFisica():

    def __init__(self, camada):
        if type(camada) == CamadaInternet:
            self.camada = camada
        else:
            self.camada = None

    def desencapsular(self):
        return self.camada

    def responsabilidade(self):
        return "Responsável por troca com o meio físico"

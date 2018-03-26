# Primeiro Trabalho de Codificação


## Material complementar para o projeto da disciplina Redes de Computadores II na FHO-Uniararas:


O Modelo OSI (acrônimo do inglês Open System Interconnection) é um modelo de rede de
computador referência da ISO dividido em camadas de funções, criado em 1971 e
formalizado em 1983, com objetivo de ser um padrão, para protocolos de comunicação entre
os mais diversos sistemas em uma rede local (Ethernet), garantindo a comunicação entre
dois sistemas computacionais (end-to-end).

Este modelo divide as redes de computadores em 7 camadas, de forma a se obter camadas
de abstração. Cada protocolo implementa uma funcionalidade assinalada a uma determinada camada.
Diferentemente do modelo OSI, que possui sete camadas, o modelo TCP/IP possui quatro camadas, são elas:

### Camada 4: A camada de Aplicação

### Camada 3: A camada de Transporte

### Camada 2: A camada de Internet

### Camada 1: A camada de Acesso a Rede


No primeiro trabalho de codificação, com uso de uma linguagem orientada a objetos, você
e seu grupo devem desenvolver uma classe para cada camada do modelo OSI. Com uso do
conceito de encapsulamento ( de orientação a objetos), as classes precisam se relacionar.

Exemplo: o objeto da classe Enlace é encapsulada no objeto da classe Física.
Investigue as características de cada camada, implementando-as.

Exemplo: o controle do acesso físico via endereço de placa de rede ( endereço MAC) é um
atributo da classe Enlace. Trata-se de uma característica da camada 2 do modelo OSI..

Após a correta implementação das sete camadas do modelo OSI, em um outro projeto, faça
a implementação equivalente das quatro camadas da pilha de protocolos TCP/IP.

Além das corretas relações entre as classes / objetos, lembre-se de usar herança e/ou outras
melhorias que a linguagem de programação de sua escolha disponibilizar.
Um dos integrantes do grupo deverá manter um perfil no github com os códigos desenvolvidos.

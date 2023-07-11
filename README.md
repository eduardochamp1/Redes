# Trabalho final de laboratorio de redes

## Disciplina: Laboratório de Redes (2023/1).

## Membros do grupo: **Breno Soares Gomes** e **José Eduardo Vilela Zouain**.

Desenvolvimento de uma aplicação para realizar uma comunicação cliente-servidor, onde o cliente tem a função de enviar arquivos para o servidor.
Primeiramente instale o docker tanto na maquina que funcionará como cliente tanto na que será o servidor, utilizando o seguinte comando:

```
sudo apt install docker.io
```

Na maquina de sua escolha, faça download da aplicação cliente. Para que seja enviado o arquivo Execute o comando a seguir para construir e executar o docker responsavel pelo cliente.

```
sudo docker run --rm -it --network=host zezouain/server:v1 /bin/bash
```

Na maquina de sua escolha, faça o dowload da aplicação cliente. Para receber o arquivo Execute o comando a seguir para construir e executar o docker responsavel pelo servidor.

```
sudo docker run --rm -it --network=host zezouain/client:v1 /bin/bash
```

Após o download dos containers e inicializado os mesmos, é necessário executar as aplicações do server e do client em suas respectivas máquinas.

Server:

```
python3 servidor-http.py
```

Client:

```
python3 cliente-http.py
```

Com todas as aplicações rodando em suas respectivas máquinas, agora, é necessário informar no algoritmo do client o endereço de IP da maquina onde se localiza o servidor. Após isso é preciso somente informar o nome do arquivo que será enviado para o servidor, onde neste caso será:

```
BRIGA.mp4
```

Feito isso, a transferência de arquivo esta completa e uma mensagem de recebimento do arquivo sera exibida no terminal no server. Para verificar se o arquivo foi enviado corretamente pode ser feito uma listagem dos arquivos locais no servidor.

```
ls -l
```

## Imagens disponiveis nos repositórios do dockerhub:

```
docker pull zezouain/client:v1

docekr pull zezouain/server:v1
```

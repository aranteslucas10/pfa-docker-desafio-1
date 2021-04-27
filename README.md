# Desafio 1

Crie um programa utilizando sua linguagem de programação favorita que faça uma listagem 
simples do nome de alguns módulos do curso Full Cycle os trazendo de um banco de dados MySQL.
Gere a imagem desse container e a publique no DockerHub.

Gere uma imagem do nginx que seja capaz que receber as solicitações http e encaminhá-las para o container.

Crie um repositório no github com todo o fonte do programa e das imagens geradas.

Crie um arquivo README.md especificando quais comandos precisamos executar para que a aplicação 
funcione recebendo as solicitações na porta 8080 de nosso computador. Lembrando que NÃO utilizaremos 
Docker-compose nesse desafio.

## Execução Via Imagem Pronta

1 - Criação da Network

```text
docker network create pfa-desafio-1
```

2 - Execução do Banco de Dados

```text
docker run --rm -d --network=pfa-desafio-1 --name pfa-desafio-1-mysql aranteslucas10/pfa-desafio-1-mysql
```

3 - Execução da Aplicação

```text
docker run --rm -d --name pfa-desafio-1-app --network=pfa-desafio-1 aranteslucas10/pfa-desafio-1-app
```

4 - Execução Proxy Reverso com Ngnix

Após esse passo, a aplicação estará disponível na porta localhost:8080

```text
docker run --rm --name pfa-desafio-1-nginx -p 8080:80 --network=pfa-desafio-1 aranteslucas10/pfa-desafio-1-nginx
```

## Execução Via Clone

Passos a serem executados para resolução do desafio.

* Comandos sendo executados a partir da raiz do projeto.

### Criação da Network

Criação da network para fácil comunicação entre os containers.

```text
docker network create pfa-desafio-1
```

### Criação do Banco de Dados MySQL

Criação de um container rodando o mysql e criação do banco de dados.

* No último comando, aguardar o banco de dados ficar totalmente disponível.

```text
docker build -t pfa-desafio-1-mysql ./mysql
docker run --rm -d --name pfa-desafio-1-mysql --network=pfa-desafio-1 pfa-desafio-1-mysql
docker exec pfa-desafio-1-mysql bash ./init_database.sh
```

Obs.:
Nessa etapa eu confesso que fiquei perdido do "jeito certo" de fazer as coisas.
Eu sei que já foi dito que não se recomenda rodar banco de dados no docker, mas adoraria uma
visão mais robusta de como iniciar banco de dados em um docker.  

### Criação do App com Python e Flask

Aqui foi criado um app com Python e Flask, o mais minimal possível.

```text
docker build -t pfa-desafio-1-app ./app
docker run --rm -d --name pfa-desafio-1-app --network=pfa-desafio-1 pfa-desafio-1-app
```

### Criação do Proxy Reverso com Ngnix

Execução do Nginx com a configuração minima para que ele faça o proxy para o container do app.

```text
docker build -t pfa-desafio-1-nginx ./nginx
docker run --rm --name pfa-desafio-1-nginx -p 8080:80 --network=pfa-desafio-1 pfa-desafio-1-nginx
```

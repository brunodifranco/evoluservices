# Evoluservices download app
Seleciona o período, e baixa o .xlsx do site Evoluservices.


## 1. Pré-requisitos

- Python (de preferência 3.10+).
- Git.

## 2. Instalação

No terminal, clone o repositório com:
```
git clone https://github.com/brunodifranco/evoluservices.git
```
Vá até a pasta local do seu repositório com:
```
cd evoluservices
```
Daqui em diante difere a instalação de Linux e Windows. 


### 2.1. Windows
a) Criando o ambiente virtual dentro da pasta `evoluservices`:

Primeiro entramos no PowerShell como administrador e executamos o comando:

```
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```
Depois (agora já no terminal cmd pelo VSCode) instalamos a biblioteca `virtualenv` do python com:

```
pip install virtualenv
```
  Depois criamos o ambiente virtual com:

```
python -m venv .venv_evoluservices
```
obs: Demos o nome de venv_evoluservices, mas pode ser qualquer outro nome.

Então é so ativar o ambiente virtual com:

```
 .\.venv_evoluservices\Scripts\activate
```
Obs: e se quiser desativar
```
deactivate
```

obs: É possível ver que o ambiente está ativado por conta desse parênteses antes do terminal:

![image](https://github.com/brunodifranco/evoluservices/assets/66283452/eea16bfa-9523-416d-99ba-bb5b7a4a0f76)

b) Buildar o app (com o ambiente ativado):

Depois (com o ambiente ativado) instalamos as bibliotecas necessárias com:

```
pip install -r requirements.txt
```

Então instalamos as dependências necessárias da biblioteca `playwright` utilizando:

```
playwright install --with-deps firefox
```

E está pronto!

### 2.2. Linux
a) Criando o ambiente virtual

```
make venv
```
  Então é só ativar o ambiente com:
```
source .venv_evoluservices/bin/activate
```
  Obs: e se quiser desativar
```
deactivate
```
obs: É possível ver que o ambiente está ativado por conta desse parênteses antes do terminal:

![image](https://github.com/brunodifranco/evoluservices/assets/66283452/eea16bfa-9523-416d-99ba-bb5b7a4a0f76)

b) Buildar o app (com o ambiente ativado):

```
make build
```
E feito!

obs: E se quiser desinstalar as bibliotecas, remover o ambiente e os browsers do playwright:

```
make remove
```

## 3. Executando o app

### 3.1. Windows

Basta rodar o comando no terminal (na pasta do repositório obviamente):

```
streamlit run app.py
```

Obs: Na primeira vez é preciso adicionar um email:

![image](https://github.com/brunodifranco/evoluservices/assets/66283452/ebac8700-2e49-469f-b096-c8e8960f3286)


### 3.2. Linux

```
make run
```

## 4. Como funciona:


![image](https://github.com/brunodifranco/evoluservices/assets/66283452/2d458703-a6e3-4a8b-9207-626ed1ffa099)


- Insira seu usário e senha
- Seleciona o período desejado.
- Clique em "Fazer Download o arquivo"

Obs: 
 - Se por acaso acontecer erro de Timeout o código tentará ser executado outras 2 vezes (ou até ser executado corretamente), já que esse tipo de erro pode acontecer por se tratar de uma biblioteca de automação web.
- Se você selecionar um período que não encontrou resultados um erro será gerada, solicitando a escolha de um novo período.
- O arquivo xlsx será baixado para uma pasta chamada "downloads" dentro do seu repositório local.


## 📝 Licença

Esse projeto está sob licença. Veja o arquivo [LICENÇA](LICENSE.md) para mais detalhes.

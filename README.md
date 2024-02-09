# Evoluservices Download App.

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


  


### 2.2. Linux
a) Criando o ambiente virtual

```
make createvenv
```

  Então é só ativar o ambiente com:
```
make venvup
```
  Obs: e se quiser desativar
```
make venvdown
```
b) Buildar o app:

```
make build
```

E feito!

## 3. Executando o app

### 3.1. Windows

Basta rodar o comando no terminal (na pasta do repositório obviamente):

```
streamlit run app.py
```

### 3.2. Linux

```
make run
```


Quer fazer parte desse projeto? Clique [AQUI](CONTRIBUTING.md) e leia como contribuir.

## 📝 Licença

Esse projeto está sob licença. Veja o arquivo [LICENÇA](LICENSE.md) para mais detalhes.

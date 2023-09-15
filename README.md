# Integra Markeplaces

Aplicativo desenvolvido em Python para integração com marketplaces


## Instalação

Crie um ambiente virtual para instalar as dependências do projeto 

```bash
    python -m venv env
```

Ative seu ambiente virtual

```bash
    # para sistemas opercaionais UNIX (Linux e MacOS)
    source env/bin/activate

    # para sistemas opercaionais DOS (Windows)
    . env\Scripts\activate
```

Instale todas as dependências

```bash
    pip install -r requirements.txt
```


## Primeiros Passos

Acesse a pasta principal do projeto

```bash
    cd src
```

Realize o Migrate do banco de dados

```bash
    python manage.py migrate
```

Crie um Superusuário para administração do aplicativo

```bash
    python manage.py createsuperuser
```

Agora rode o servidor do Django

```bash
    python manage.py runserver
```
# AgroBrain: Aplicativo de Sugestão de Insumos Agrícolas

**AgroBrain** é um aplicativo web desenvolvido para ajudar pequenos agricultores a otimizar o uso de insumos agrícolas, com base na análise do solo. A plataforma permite que o usuário insira dados do solo e receba recomendações personalizadas sobre adubação, ajudando a economizar recursos e melhorar a produtividade das culturas.

## Funcionalidades

- **Análise de Solo**: O usuário pode inserir dados como pH, matéria orgânica, fósforo, potássio, cálcio, magnésio e saturação por bases.
- **Recomendações Personalizadas**: Com base nas análises do solo, o sistema gera recomendações de adubação para o solo, ajudando a otimizar o uso de fertilizantes.
- **Interface Simples**: Uma interface amigável que permite aos usuários inserir facilmente os dados do solo e visualizar as recomendações.

## Tecnologias Utilizadas

- **Django**: Framework utilizado para o desenvolvimento da aplicação web.
- **Python**: Linguagem de programação para o backend, responsável pelo processamento dos dados.
- **PostgreSQL**: Banco de dados utilizado para armazenar informações do solo e recomendações.
- **HTML/CSS**: Tecnologias utilizadas para a construção da interface front-end.
- **JavaScript** (opcional): Para interações mais dinâmicas, caso haja necessidade de mais funcionalidades no front-end.

## Instalação

### Pré-requisitos

- Python 3.x
- PostgreSQL
- Git

### Passos para rodar o projeto localmente

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/OtelmoJr/TCC.git
   cd TCC
   ```

2. **Crie um ambiente virtual**:
   Se estiver utilizando `venv`:
   ```bash
   python -m venv venv
   ```

3. **Ative o ambiente virtual**:
   - No Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - No Linux/Mac:
     ```bash
     source venv/bin/activate
     ```

4. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Configuração do Banco de Dados**:
   Certifique-se de ter o PostgreSQL instalado e crie um banco de dados para o projeto. Edite o arquivo `settings.py` no Django para incluir suas credenciais do banco de dados:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'nome_do_banco',
           'USER': 'usuario',
           'PASSWORD': 'senha',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```

6. **Migrações do Banco de Dados**:
   Execute as migrações para configurar o banco de dados:
   ```bash
   python manage.py migrate
   ```

7. **Rodar o Servidor de Desenvolvimento**:
   Após configurar o banco e as dependências, você pode iniciar o servidor local:
   ```bash
   python manage.py runserver
   ```

8. **Acessar a aplicação**:
   Abra o navegador e vá para `http://127.0.0.1:8000/` para ver a aplicação rodando.

## Contribuição

1. Fork o repositório
2. Crie uma nova branch (`git checkout -b feature/novafuncionalidade`)
3. Faça suas alterações e commit (`git commit -am 'Adiciona nova funcionalidade'`)
4. Envie para a branch principal (`git push origin feature/novafuncionalidade`)
5. Crie um Pull Request

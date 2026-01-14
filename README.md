# 🏖️ Praia & Conforto - Plataforma de Aluguel de Temporada

![Status do Projeto](https://img.shields.io/badge/Status-Desenvolvido-green)
![Python](https://img.shields.io/badge/Python-3.14-blue)
![Django](https://img.shields.io/badge/Django-6.0-green)

Uma aplicação web moderna para gestão e visualização de apartamentos de
temporada. O projeto foca na experiência do usuário, permitindo cálculo de
diárias em tempo real e contato direto via WhatsApp para reservas.

## 🚀 Tecnologias Utilizadas

Este projeto foi construído utilizando versões "bleeding edge" (mais recentes)
da stack Python:

- **Backend:** [Python 3.14](https://www.python.org/) &
  [Django 6.0](https://www.djangoproject.com/)
- **Frontend:** HTML5, Django Templates &
  [Tailwind CSS](https://tailwindcss.com/) (via CDN)
- **Interatividade:** JavaScript Vanilla (Cálculo de datas e Link dinâmico para
  WhatsApp)
- **Banco de Dados:** SQLite (Desenvolvimento)
- **Gerenciamento de Mídia:** Pillow

## 🎯 Funcionalidades

- **Catálogo Visual:** Listagem de apartamentos com cards responsivos e
  modernos.
- **Página de Detalhes:**
  - Galeria de fotos.
  - Descrição completa do imóvel.
- **Calculadora de Reservas (JS):**
  - O usuário seleciona Check-in e Check-out.
  - O sistema calcula automaticamente o total de dias e o valor final baseada na
    diária do imóvel.
- **Integração WhatsApp ("Trava-Zeca"):**
  - O botão de reserva permanece inativo até que datas válidas sejam
    selecionadas.
  - Ao clicar, o usuário é redirecionado para o WhatsApp do proprietário com uma
    mensagem pré-formatada contendo as datas e valores.
- **Painel Administrativo:** Gestão completa de imóveis e fotos via Django
  Admin.

## 📸 Capturas de Tela

_(Você pode adicionar prints do seu site aqui depois)_

## 🛠️ Como rodar o projeto localmente

Siga os passos abaixo para configurar o ambiente de desenvolvimento:

### 1. Clone o repositório

```bash
git clone [https://github.com/leandrotmst/site_para_aluar_aptos.git](https://github.com/leandrotmst/site_para_alugar_aptos.git)
cd site_aptos
```

2. Crie e ative o ambiente virtual Bash

# Linux/Mac

python3.14 -m venv venv source venv/bin/activate

# Windows

python -m venv venv venv\Scripts\activate

3. Instale as dependências Bash

pip install -r requirements.txt

4. Configure o Banco de Dados Bash

python manage.py migrate

5. Crie um Superusuário (Admin) Bash

python manage.py createsuperuser

6. Inicie o Servidor Bash

python manage.py runserver Acesse o projeto em: http://127.0.0.1:8000/

📂 Estrutura do Projeto siteaptos/: Configurações principais do projeto
(Settings, URLS globais).

apartamento/: App principal contendo a lógica dos imóveis (Models, Views).

templates/: Templates globais (como o base.html com o layout Tailwind).

media/: Diretório para upload de imagens dos apartamentos.

📝 Licença Este projeto é destinado a fins de portfólio e estudo.

Desenvolvido por Leandro 🚀

### Como postar no GitHub agora:

1.  Crie um novo repositório no GitHub chamado `site_aptos`.
2.  No seu terminal, execute:
    ```bash
    git init
    git add .
    git commit -m "Primeira versão do Praia e Conforto com Django 6.0"
    git branch -M main
    git remote add origin https://github.com/SEU-USUARIO/site_para_alugar_aptos.git
    git push -u origin main
    ```
    _(Lembre-se de trocar `SEU-USUARIO` pelo seu user real do GitHub)_.

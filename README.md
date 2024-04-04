# Serverest Web Automation - Python

## Objetivo do Framework
Este framework utiliza Python e Selenium WebDriver para automatizar testes de login na aplicação web Serverest. O objetivo é validar a funcionalidade de login, garantindo que os usuários possam acessar a aplicação com suas credenciais.

## Pré-requisitos
- Python: A linguagem de programação utilizada para escrever os testes.
- Selenium WebDriver: Uma biblioteca em Python para automação de navegadores web.

## Instalação das Dependências
- Instale Python a partir do site oficial.
- Instale o Selenium com o comando `pip install selenium`.
- Baixe o ChromeDriver e adicione-o ao PATH do sistema.

## Executando o Teste
Salve o script de teste em um arquivo `.py` e execute-o com o comando `python login_test.py` em um terminal.

## Estrutura do Código
- `login_test.py`: Contém o código do teste automatizado, que realiza a autenticação na página de login e verifica se o login foi bem-sucedido.

## Descrição do Teste
- O teste abre a página de login, preenche os campos de usuário e senha e submete o formulário.
- Verifica se a URL mudou após o login, como indicativo de sucesso.
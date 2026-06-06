# Projeto de Testes Automatizados E2E - Sauce Demo

## 🖥️ Sistema Escolhido
* **Nome do Sistema:** Sauce Demo (Aplicação pública de demonstração da Sauce Labs)
* **Link de Acesso:** [https://www.saucedemo.com/](https://www.saucedemo.com/)
* **Descrição do Sistema:** Simula a interface de um e-commerce completo. Permite a autenticação de diferentes perfis de usuários, listagem e ordenação de produtos, manipulação de um carrinho de compras em tempo real e um fluxo completo de checkout (faturamento e confirmação de pedido).

## 🛠️ Ferramentas Utilizadas
* **Linguagem:** Python 3.x
* **Framework de Testes:** Pytest (responsável pela execução, gerenciamento e relatórios dos cenários)
* **Ferramenta de Automação:** Selenium WebDriver (responsável pela interação simulada com o navegador Google Chrome)
* **Gerenciador de Pacotes:** `uv` (utilizado para gerenciamento rápido e isolado do ambiente virtual e dependências)

## 📦 Como Configurar o Ambiente e Executar os Testes

Para garantir que o projeto execute corretamente, siga os passos abaixo no terminal dentro da pasta raiz do projeto:

1. **Instalar as dependências necessárias:**
   ```bash
   uv pip install pytest selenium
# Simulação de Exchange de Criptomoedas

Um projeto em Python que simula uma exchange de criptomoedas, permitindo operações como cadastro, login, consulta de saldo, depósito, saque, compra e venda de criptomoedas (Bitcoin, Ethereum e Ripple), além de atualização de cotações.

---

## 📋 Sobre o Projeto

Este projeto foi desenvolvido como parte do curso de **Fundamentos de Algoritmos** e tem como objetivo simular o funcionamento básico de uma exchange de criptomoedas. O programa é totalmente interativo, permitindo que os usuários realizem diversas operações financeiras, como:

- Cadastro e login de usuários.
- Consulta de saldo em reais e criptomoedas.
- Visualização de extrato de transações.
- Depósito e saque de reais.
- Compra e venda de criptomoedas (Bitcoin, Ethereum e Ripple).
- Atualização automática das cotações das criptomoedas.

---

## 🚀 Funcionalidades

### 1. **Cadastro e Login**
   - Os usuários podem se cadastrar fornecendo CPF, senha e nome.
   - O sistema valida o CPF (11 dígitos) e a senha (6 dígitos).
   - Caso o usuário tente fazer login sem cadastro, ele é redirecionado para o cadastro.

### 2. **Menu Principal**
   - Após o login, o usuário acessa um menu interativo com as seguintes opções:
     1. Consultar saldo.
     2. Consultar extrato.
     3. Depositar reais.
     4. Sacar reais.
     5. Comprar criptomoedas.
     6. Vender criptomoedas.
     7. Atualizar cotações.
     8. Sair do programa.

### 3. **Consulta de Saldo**
   - Exibe o saldo atual em reais e nas criptomoedas disponíveis (Bitcoin, Ethereum e Ripple).

### 4. **Extrato**
   - Mostra todas as transações realizadas pelo usuário em ordem cronológica, incluindo depósitos, saques, compras e vendas.

### 5. **Depósito e Saque**
   - Permite que o usuário adicione ou retire dinheiro de sua conta.
   - O saque só é permitido se o usuário tiver saldo suficiente.

### 6. **Compra e Venda de Criptomoedas**
   - O usuário pode comprar e vender Bitcoin, Ethereum e Ripple.
   - Cada operação possui taxas específicas:
     - **Compra:** Bitcoin (2%), Ethereum (1%), Ripple (1%).
     - **Venda:** Bitcoin (3%), Ethereum (2%), Ripple (1%).

### 7. **Atualização de Cotações**
   - As cotações das criptomoedas são atualizadas aleatoriamente, variando entre -5% e +5% em relação ao valor anterior.
   - Isso influencia diretamente os preços de compra e venda.

---

## 🛠️ Como Executar o Projeto

### Pré-requisitos
- Python 3.x instalado.

### Passos para Execução
1. Clone o repositório:
   - git clone https://github.com/LucasGalvano/Exchange-Python.git

### Navegue até o diretório do projeto
   - cd Exchange-Python

### Execute o arquivo exchange.py
   - python exchange.py

  ---

## 📊 Exemplo de Uso
Aqui está um exemplo de como o programa funciona:
 ### Cadastro
  Seja bem-vindo(a), você deseja se cadastrar[1] ou fazer login[2]: 1
  Digite seu CPF: 11111111111
  Crie uma senha: 123456
  Digite seu nome: Joaozinho
 ### Login
  Seja bem-vindo(a), você deseja se cadastrar[1] ou fazer login[2]: 2
  Digite seu CPF sem pontos ou traços: 11111111111
  Senha: 123456
  Login realizado com sucesso!
 ### Menu Principal
  1 - Consultar saldo
  2 - Consultar extrato
  3 - Depositar
  4 - Sacar
  5 - Comprar Criptomoedas
  6 - Vender Criptomoedas
  7 - Atualizar Cotações
  8 - Sair
  Escolha uma opção:
  
 ### Consulta de Saldo
  Nome: Joaozinho
  CPF: 111.111.111-11
  Carteira
  Reais: 1000.00
  Bitcoin: 0
  Ethereum: 0
  Ripple: 0

---
  
## 📂 Estrutura do Projeto
 - exchange.py: Código principal do projeto, contendo todas as funcionalidades.

 - exchange.txt: Arquivo de log que registra as operações realizadas pelos usuários.

 ---

##  Vídeo Demonstrativo
  Assista ao vídeo demonstrativo do projeto:
  - https://www.youtube.com/watch?v=wddEWvEVFzM

    ---
    
## 👨‍💻 Autor
  - Lucas Galvano de Paula
  - Desenvolvido como parte do curso de Fundamentos de Algoritmos.

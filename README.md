
# NetecShop — Automação de Testes Web

Projeto acadêmico de automação de testes da aplicação NetecShop utilizando Python, Selenium WebDriver, Pytest e Selenium IDE.

O repositório reúne testes de login, catálogo de produtos, carrinho de compras e checkout, além de exemplos de organização de testes com o padrão Page Object Model (POM).

> **Atenção:** durante a execução dos testes, foram identificados problemas de compatibilidade e execução relacionados ao ambiente de automação e às versões atuais dos navegadores. Os cenários precisam ser revisados e validados individualmente antes de serem considerados funcionais.

## Objetivos

- Praticar a automação de testes de interface web.
- Verificar comportamentos esperados e situações de erro.
- Utilizar Selenium WebDriver para interagir com elementos HTML.
- Executar e organizar cenários automatizados com Pytest.
- Explorar testes gravados no Selenium IDE.
- Aplicar o padrão Page Object Model para facilitar a manutenção dos testes.

## Tecnologias utilizadas

- **Python:** linguagem utilizada nos testes automatizados.
- **Selenium WebDriver:** automação do navegador.
- **Pytest:** execução e organização dos testes.
- **Mozilla Firefox:** navegador configurado no projeto.
- **Selenium IDE:** gravação e reprodução de interações com a aplicação.
- **Page Object Model (POM):** padrão para organizar os elementos e as ações das páginas.

## Funcionalidades contempladas

### Login
- Autenticação com credenciais válidas e inválidas.
- Verificação de mensagens de erro.
- Validação de comportamentos relacionados à autenticação.

### Catálogo de produtos
- Listagem e pesquisa de produtos.
- Verificação de resultados da pesquisa.
- Testes de inscrição na newsletter e interação com iframe.

### Carrinho de compras
- Adição de produtos.
- Verificação da quantidade de itens.
- Remoção de produtos e confirmação de ações.

### Checkout
- Testes organizados para o fluxo de checkout.
- Separação das ações da página e dos cenários de teste por meio do POM.

A presença de um cenário no repositório não significa que ele esteja funcionando na versão atual do navegador.

## Estrutura do projeto

```text
netecshop/
├── paginas/
├── conftest.py
├── netecshop.side
├── test_login.py
├── test_catalogo.py
├── test_carrinho.py
├── test_gravado.py
├── test_login_pom.py
├── test_catalogo_pom.py
├── test_checkout_pom.py
└── README.md
```

- `conftest.py`: configuração compartilhada do navegador e das fixtures do Pytest.
- `test_login.py`: testes relacionados ao login.
- `test_catalogo.py`: testes do catálogo e da newsletter.
- `test_carrinho.py`: testes das operações do carrinho.
- `test_gravado.py`: exemplo de teste relacionado à gravação de interações.
- `test_login_pom.py`: testes de login com Page Object Model.
- `test_catalogo_pom.py`: testes do catálogo com Page Object Model.
- `test_checkout_pom.py`: testes relacionados ao checkout com POM.
- `paginas/`: classes e operações relacionadas às páginas.
- `netecshop.side`: arquivo do projeto do Selenium IDE.

## Pré-requisitos

- Python 3 instalado.
- Mozilla Firefox instalado, conforme a configuração do projeto.
- Git instalado.
- Acesso à internet para instalação de dependências e, quando necessário, obtenção do driver.
- Selenium e Pytest instalados no ambiente Python.

## Instalação

Clone o repositório:

```bash
git clone https://github.com/Matheus-Sill/netecshop.git
cd netecshop
```

Crie um ambiente virtual.

**Windows:**

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

**Linux ou macOS:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Instale as dependências:

```bash
python -m pip install --upgrade pip
python -m pip install selenium pytest
```

> Para reproduzir um ambiente de testes de maneira consistente, recomenda-se registrar as versões das dependências em um arquivo `requirements.txt`, depois de validar quais versões funcionam com o projeto.

## Execução dos testes com Pytest

Execute todos os testes:

```bash
python -m pytest
```

Execute um arquivo específico:

```bash
python -m pytest test_login.py -v
```

Outros exemplos:

```bash
python -m pytest test_catalogo.py -v
python -m pytest test_carrinho.py -v
python -m pytest test_login_pom.py -v
python -m pytest test_catalogo_pom.py -v
python -m pytest test_checkout_pom.py -v
```

Execute um teste pelo nome:

```bash
python -m pytest -k "login" -v
```

### Interpretando os resultados

- `PASSED`: o teste passou.
- `FAILED`: uma verificação do teste falhou.
- `ERROR`: ocorreu um erro durante a preparação ou execução.

Se houver falhas, consulte a mensagem de erro apresentada pelo Pytest antes de alterar o código ou as versões das dependências.

## Compatibilidade com navegadores atuais

As atualizações dos navegadores podem exigir ajustes no ambiente de automação, nos drivers, nos seletores e nas interações utilizadas pelos testes.

### Selenium WebDriver

O Selenium Manager, incluído nas versões modernas do Selenium, pode gerenciar automaticamente os drivers necessários quando eles não são fornecidos manualmente.

Atualize a biblioteca, se necessário:

```bash
python -m pip install --upgrade selenium
```

Essa atualização não garante que todos os testes passarão: erros nos seletores, nas esperas ou na lógica dos cenários também precisam ser corrigidos.

### Selenium IDE

O arquivo `netecshop.side` contém o projeto utilizado pelo Selenium IDE.

Para investigar falhas na reprodução dos testes gravados:

1. Verifique se está utilizando uma versão atual do Selenium IDE.
2. Confira se os comandos gravados ainda são reconhecidos pela versão utilizada.
3. Revise os seletores dos elementos da página.
4. Verifique se os elementos estão carregados antes da execução dos comandos.
5. Regrave ou ajuste os passos que dependem de elementos que foram modificados.

A extensão antiga do Selenium IDE, versão 3, não é mais mantida. Prefira verificar a versão atual e as instruções oficiais de instalação antes de atribuir o problema exclusivamente ao navegador.

## Problemas conhecidos e limitações

Durante a validação do projeto, foram observadas falhas de execução no Pytest e no Selenium IDE.

As causas específicas ainda precisam ser identificadas por meio das mensagens de erro. Entre os pontos que devem ser investigados estão:

- Compatibilidade entre o Selenium, o navegador e o driver.
- Mudanças nos elementos e seletores da aplicação.
- Falta de esperas adequadas durante o carregamento.
- Comandos ou recursos incompatíveis com a versão do Selenium IDE.
- Dependências instaladas em versões diferentes das utilizadas originalmente.

Não é recomendado instalar versões antigas do navegador ou desativar atualizações de segurança como primeira solução. O ideal é corrigir os testes e manter um ambiente reproduzível.

## Referências

- [Repositório NetecShop](https://github.com/Matheus-Sill/netecshop)
- [Documentação do Selenium](https://www.selenium.dev/documentation/)
- [Selenium Manager](https://www.selenium.dev/documentation/selenium_manager/)
- [Documentação do Pytest](https://docs.pytest.org/)
- [Selenium IDE](https://www.selenium.dev/selenium-ide/)

## Autor

Matheus Sill e wiltienem

Projeto acadêmico para estudo de automação de testes de software.

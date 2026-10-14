# Análise do teste gravado da NetecShop

### 1. Quantas linhas de espera há no arquivo exportado? O que isso provoca?

Possui zero linhas de espera. Após clicar no botão Entrar, o teste tenta verificar imediatamente a mensagem de saudação. Como o processamento do login leva cerca de 900 ms, o elemento ainda pode estar vazio, provocando um `AssertionError`.

### 2. Por que o teste passava dentro do IDE e falha no pytest?

Dentro do IDE, o motor da ferramenta realiza esperas automaticamente entre os comandos. Ao exportar o teste para Python, essas esperas não são incluídas no código. Com isso, o pytest verifica mensagem antes do login terminar de ser processado.

### 3. O que acontece com o seletor `xpath=//div[2]/input` se um desenvolvedor inserir um aviso acima do formulário?

O seletor pode passar a identificar outro elemento ou deixar de funcionar, porque depende da posição do campo na estrutura HTML. A inserção de um aviso pode alterar essa estrutura. Por isso, é preferível utilizar seletores estáveis, como `id=usuario`.

### 4. O login está pronto para ser reaproveitado em outros testes, ou teria de ser copiado e colado?

O código exportado não está organizado como uma função ou método reutilizável de login. Para utilizá-lo em outros testes, seria necessário copiar e colar as ações ou refatorar o código para criar um método reutilizável, evitando duplicação.

### 5. Em uma frase: para que serve a gravação, e para que ela não serve?

A gravação serve como ponto de partida para criar testes automatizados e observar as interações com a aplicação, mas não substitui a análise, a implementação de esperas adequadas, a validação dos resultados e a organização do código para reutilização.


### Etapa 08
Fiz o comentario das 3 linhas e substituí a espera pela busca direta usando find_element(). O teste falhou com AssertionError, pois a saudação foi encontrada, mas seu texto ainda estava vazio. Isso demonstra que encontrar um elemento não significa que o conteúdo já esteja pronto para ser verificado.

### Etapa 10
Todos os processos foram executados de forma correta

### Etapa 13
Localizar e acessar um iframe. Preencher e enviar o formulário interno. Ver o que ocorreu quando a troca de contexto foi removida. Por que é necessário usar switch_to.default_content() para voltar à página principal.
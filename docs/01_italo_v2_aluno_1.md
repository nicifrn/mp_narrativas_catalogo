# Plano de desenvolvimento - Aluno 1: validador da planilha de narrativas

**Aluno:** Aluno 1 (@aluno1) - Técnico Integrado em Informática

**Orientador:** Prof. Bruno Gomes (@brunogomesifrn) - NIC/IFRN

**Trabalho do qual você participa:** catálogo estruturado de narrativas do RN, do Ítalo (@italogomees). O plano dele está em [`docs/01_italo_v2_narrativas_desenvolvimento.md`](01_italo_v2_narrativas_desenvolvimento.md).

**Repositório:** https://github.com/nicifrn/mp_narrativas_catalogo

**Período:** 23/11/2026 a 10/12/2026. **A sua entrega principal é na quinta, 03/12.**

> Leia este documento inteiro antes de começar. Ele tem tudo o que você precisa: o que programar, em que ordem, com quais comandos e onde pesquisar.

---

## Sumário

- [1. O que você vai fazer](#ideia)
- [2. O formato da planilha](#formato)
- [3. Cronograma](#cronograma)
- [4. Como trabalhar no repositório](#fluxo-git)
- [Sprint 1 - Ambiente, arquivo de teste e primeira versão](#sprint-1)
- [Sprint 2 - Validador completo](#sprint-2)
- [Sprint 3 - Ajustes](#sprint-3)

---

<a id="ideia"></a>
## 1. O que você vai fazer

O Ítalo está montando uma planilha com narrativas populares do Rio Grande do Norte (lendas, contos, causos) para o acervo da plataforma Narrativas, do IFRN. Planilha preenchida à mão sempre tem erro: campo esquecido, ano escrito por extenso, tipo digitado errado.

**Você vai programar o validador:** um programa em Python que lê a planilha (em CSV), confere cada linha e mostra todos os erros que encontrou, dizendo **em que linha** e **em que coluna** está cada um. Ele também grava os erros em um arquivo, para o Ítalo usar nos resultados do trabalho dele.

Você roda assim:

```
python scripts\validar.py dados\teste_validador.csv
```

E ele responde mais ou menos assim:

```
Linha 3, coluna titulo: vazio
Linha 4, coluna ano_fonte: nao_inteiro
Linha 6, coluna tipo: fora_da_lista
Linha 8, coluna id: repetido

Linhas lidas: 10
Erros encontrados: 4
Relatório gravado em resultados\erros_teste_validador.csv
```

**O que você só usa:** Python e os módulos `csv`, `sys` e `os`, que já vêm com ele. Você **não instala nada**.

**O que fica de fora:** corrigir a planilha (o validador só aponta), interface gráfica, `pandas`. O validador **não** confere se o município existe: isso é um extra, só se sobrar tempo (Sprint 3).

**Você não depende de ninguém para começar.** O formato está fechado na [seção 2](#formato), e você mesmo cria o arquivo de teste.

### Quem faz o quê na equipe

| Quem | Faz | Arquivos |
|---|---|---|
| Ítalo | Planilha com narrativas reais, conversor para JSON, estatísticas, integração e o RCC | os do plano dele |
| **Você (Aluno 1)** | **Validador** | **`scripts/validar.py` e `dados/teste_validador.csv`** |
| Aluno 2 | Gerador de narrativas fictícias, com erros de propósito | `scripts/gerar_fake.py` |

**Mexa só nos seus dois arquivos.** Assim ninguém atrapalha ninguém no Git. Se precisar de outra coisa no repositório, peça ao Ítalo.

No fim, o Ítalo roda o gerador do Aluno 2 (que cria planilhas com erros conhecidos) e o seu validador em cima delas, para medir **quantos erros o seu validador encontra**. Por isso o formato da saída precisa ser exatamente o da [seção 2.3](#formato).

---

<a id="formato"></a>
## 2. O formato da planilha

Este formato é o **contrato** da equipe: você, o Ítalo e o Aluno 2 usam exatamente estes nomes, nesta ordem. Ele não muda. O Ítalo publica a explicação detalhada de cada coluna em `docs/formato_planilha.md` até 24/11, mas você já pode começar com a tabela abaixo.

### 2.1 As colunas

| # | Coluna | Obrigatória | Tipo | Regra |
|---|---|---|---|---|
| 1 | `id` | sim | número inteiro | 1, 2, 3..., sem repetir |
| 2 | `titulo` | sim | texto | |
| 3 | `tipo` | sim | lista | `lenda`, `conto`, `causo`, `mito`, `cordel` |
| 4 | `publico` | sim | lista | `infantil`, `juvenil`, `adulto`, `livre` |
| 5 | `municipio` | sim | texto | |
| 6 | `mesorregiao` | sim | lista | `oeste`, `central`, `agreste`, `leste` |
| 7 | `texto` | sim | texto | de 2 a 3 trechos, cada um entre aspas, separados por ` \| ` |
| 8 | `palavras_chave` | não | texto | |
| 9 | `fonte` | sim | texto | |
| 10 | `url_fonte` | não | texto | |
| 11 | `ano_fonte` | não | número inteiro | entre 1500 e 2026 |
| 12 | `licenca` | sim | lista | `dominio_publico`, `cc_by`, `cc_by_sa`, `direitos_reservados`, `desconhecida` |

### 2.2 Regras do arquivo

- CSV, codificação UTF-8, separado por vírgula.
- A primeira linha é o cabeçalho.
- **Numeração das linhas:** o cabeçalho é a **linha 1**; a primeira narrativa é a **linha 2**. É a mesma numeração que aparece no Google Planilhas.
- Uma coluna opcional vazia **não é erro**.
- Espaços sobrando no começo ou no fim de um valor (`" lenda "`) não são erro: tire os espaços antes de conferir.
- **A coluna `texto`** tem de 2 a 3 trechos curtos copiados de uma fonte, separados pelo caractere `|`. Cada trecho começa com aspas e termina com aspas. Valem as aspas retas (`"`) e as curvas (`“` para abrir, `”` para fechar). Exemplo de valor certo: `"Primeiro trecho." | "Segundo trecho."`

### 2.3 Os erros que o validador procura

| Código | Quando acontece | Em quais colunas |
|---|---|---|
| `vazio` | coluna obrigatória sem valor | as 9 obrigatórias |
| `nao_inteiro` | o valor não é número inteiro | `id` e `ano_fonte` (só se não estiverem vazios) |
| `fora_da_faixa` | ano menor que 1500 ou maior que 2026 | `ano_fonte` |
| `fora_da_lista` | valor que não está na lista | `tipo`, `publico`, `mesorregiao`, `licenca` |
| `repetido` | `id` que já apareceu em uma linha anterior | `id` |
| `quantidade_trechos` | menos de 2 ou mais de 3 trechos | `texto` |
| `sem_aspas` | algum trecho não começa ou não termina com aspas | `texto` |

**Um erro por coluna, no máximo.** Se a coluna obrigatória está vazia, o erro é só `vazio`: não confira mais nada nela. Se o ano não é inteiro, o erro é só `nao_inteiro`: não confira a faixa. Se o `texto` não tem de 2 a 3 trechos, o erro é só `quantidade_trechos`: não confira as aspas. Se mais de um trecho estiver sem aspas, o erro aparece **uma vez só** para a coluna.

**O relatório de erros** é um CSV gravado em `resultados/erros_<nome do arquivo>.csv` (por exemplo, `dados/teste_validador.csv` gera `resultados/erros_teste_validador.csv`), com este formato:

```
linha,coluna,erro
3,titulo,vazio
4,ano_fonte,nao_inteiro
6,tipo,fora_da_lista
8,id,repetido
```

Os códigos são exatamente os da tabela: minúsculas, sem acento, com `_`. O gerador do Aluno 2 grava o gabarito no mesmo formato, e o Ítalo compara os dois arquivos linha por linha. **Se você escrever `Vazio` ou `campo vazio`, a comparação falha.**

---

<a id="cronograma"></a>
## 3. Cronograma

| Sprint | Período | O que você faz | *Issue* |
|---|---|---|---|
| 1 | 23/11 a 26/11 | Ambiente, Git, estudo do módulo `csv`, arquivo de teste e primeira versão (confere só campo vazio) | #7 |
| 2 | 27/11 a 03/12 | Validador completo, com as 7 regras e o relatório em CSV. **Entrega: 03/12** | #8 |
| 3 | 04/12 a 10/12 | Ajustes que o Ítalo ou eu pedirmos depois da integração | #9 |

---

<a id="fluxo-git"></a>
## 4. Como trabalhar no repositório

### 4.1 As *branches*

| *Branch* | Para que serve |
|---|---|
| `develop` | onde o trabalho aprovado dos três se junta. Ninguém envia direto: só entra por *pull request* (PR) aprovado |
| `main` | versão final. Só eu mexo |
| a sua *branch* | onde você trabalha |

As suas *branches*:

| Sprint | *Branch* | *Issue* |
|---|---|---|
| 1 | `feature/validador-base` | #7 |
| 2 | `feature/validador-completo` | #8 |
| 3 | `fix/validador-ajustes` | #9 |

### 4.2 Os comandos do dia a dia

**Começo de cada sprint:** pegue a `develop` atualizada e crie a *branch* da semana:

```
git checkout develop
git pull
git checkout -b nome-da-branch
```

**Fim de cada dia:** envie o que fez. O que fica só no computador do laboratório não conta como entregue.

```
git status
git add scripts/validar.py dados/teste_validador.csv
git commit -m "feat: confere campos obrigatórios vazios"
git push
```

Repare que o `git add` leva **só os seus dois arquivos**. Assim você não envia sem querer arquivos de outras pessoas ou pastas como `__pycache__`.

Na primeira vez que der `git push` em uma *branch* nova, o Git responde com um erro e mostra o comando certo, algo como `git push --set-upstream origin feature/validador-base`. Copie e rode exatamente o comando que ele mostrar.

### 4.3 Mensagens de *commit*

Em português, curtas, com o verbo no presente e um prefixo:

| Prefixo | Quando | Exemplo |
|---|---|---|
| `feat:` | algo novo funcionando | `feat: confere valores fora da lista` |
| `fix:` | correção | `fix: corrige numeração das linhas` |
| `test:` | arquivo de teste | `test: adiciona planilha de teste com erros conhecidos` |

**Proibido:** `ajustes`, `mudanças`, `update`, `correções`. Faça pelo menos **2 *commits* por semana**.

### 4.4 O *pull request* (PR)

1. `git status` deve dizer `nothing to commit, working tree clean`.
2. No GitHub, abra o repositório. Clique em **Compare & pull request** na faixa amarela. Se não aparecer: aba **Pull requests → New pull request**, com **base: `develop`** e **compare: a sua *branch***.
3. Preencha o modelo: **Objetivo**, **O que foi feito**, **Como testar** (o comando e a saída do terminal, copiada e colada) e, em **Issue**, `Closes #N` com o número da sua *issue*.
4. Em **Reviewers**, marque `brunogomesifrn` e `italogomees`.
5. Na *issue*, comente: `@brunogomesifrn @italogomees PR #X pronto para revisão`.

**Você não faz o *merge*.** Se pedirmos ajustes, faça na mesma *branch*: o PR se atualiza sozinho.

### 4.5 Quando travar

**Travou mais de 40 minutos no mesmo erro? Pare e peça ajuda.** Comente na sua *issue*, me marcando, com: o que você estava tentando fazer, o comando que rodou e **a mensagem de erro inteira, copiada e colada**.

---

<a id="sprint-1"></a>
# Sprint 1: 23/11 a 26/11 - Ambiente, arquivo de teste e primeira versão

**Branch:** `feature/validador-base` · **Issue:** #7 · **PR até:** quinta, 26/11

**O que você vai entregar:** o arquivo de teste com erros conhecidos e uma primeira versão do validador que lê o CSV, confere o cabeçalho e encontra as colunas obrigatórias vazias.

### Passo a passo

**Segunda, 23/11: ambiente**

1. Aceite o convite do repositório: https://github.com/nicifrn/mp_narrativas_catalogo/invitations

2. Abra o VS Code e o terminal (**Terminal → New Terminal**). Se for a primeira vez nesta máquina, configure o Git com o seu nome e o e-mail da sua conta do GitHub:

   ```
   git config --global user.name "Seu Nome"
   git config --global user.email "seu-email@exemplo.com"
   ```

3. Clone o repositório e abra no VS Code:

   ```
   cd $HOME\Documents
   git clone https://github.com/nicifrn/mp_narrativas_catalogo.git
   cd mp_narrativas_catalogo
   code .
   ```

   Se o Git pedir login, vai abrir uma janela do navegador: entre com a sua conta do GitHub e autorize. Daqui em diante, use o terminal da janela do VS Code que abriu.

4. Confira o Python e crie a sua *branch*:

   ```
   python --version
   git branch
   git checkout -b feature/validador-base
   ```

   O `python --version` deve mostrar `Python 3.` alguma coisa. O `git branch` deve mostrar `* develop`.

5. Crie as pastas `scripts`, `dados` e `resultados`, se ainda não existirem (no explorador do VS Code, à esquerda: botão direito → **New Folder**).

**Segunda e terça, 23 e 24/11: estudar**

6. Leia e teste os exemplos destas páginas, **digitando** os códigos (não copie e cole: digitando você aprende):
   - Leitura e escrita de arquivos: https://docs.python.org/pt-br/3/tutorial/inputoutput.html#reading-and-writing-files
   - O módulo `csv`, principalmente o `csv.DictReader` e o `csv.writer`: https://docs.python.org/pt-br/3/library/csv.html
   - Conjuntos (`set`), que você vai usar para achar `id` repetido: https://docs.python.org/pt-br/3/tutorial/datastructures.html#sets
   - Tratamento de exceções (`try` e `except`), que você vai usar para conferir se um texto é número: https://docs.python.org/pt-br/3/tutorial/errors.html#handling-exceptions

   Se preferir vídeo, procure no YouTube por "python csv DictReader" e "python try except".

**Terça, 24/11: o arquivo de teste**

7. Crie o arquivo de teste `dados/teste_validador.csv`. É uma planilha pequena, feita à mão, em que **você já sabe** onde está cada erro. É com ela que você vai testar o validador o tempo todo.

   Monte a planilha no **Google Planilhas**, que cuida sozinho das aspas e das vírgulas do CSV:

   1. Abra https://sheets.google.com → **Em branco**. Nome: `Teste do validador`.
   2. Na linha 1, digite os 12 nomes das colunas, um por célula, de A a L, exatamente como na [seção 2.1](#formato).
   3. Na linha 2, digite uma narrativa **sem nenhum erro**, uma coluna por célula:

      | Coluna | Valor |
      |---|---|
      | `id` | `1` |
      | `titulo` | `A lenda de teste` |
      | `tipo` | `lenda` |
      | `publico` | `livre` |
      | `municipio` | `Natal` |
      | `mesorregiao` | `leste` |
      | `texto` | `"Primeiro trecho de teste." \| "Segundo trecho de teste."` |
      | `palavras_chave` | `teste; lenda` |
      | `fonte` | `SOBRENOME. Obra de teste.` |
      | `url_fonte` | *(deixe vazia)* |
      | `ano_fonte` | `1950` |
      | `licenca` | `dominio_publico` |

      A `url_fonte` vazia **não** é erro, porque ela é opcional.

   4. Agora acrescente **mais 9 linhas, cada uma com exatamente um erro diferente**. Copie a linha 2 (selecione a linha pelo número, `Ctrl + C`, clique na linha de baixo, `Ctrl + V`), troque o `id` e estrague uma coluna:

      | Linha da planilha | O erro que você coloca | O validador deve dizer |
      |---|---|---|
      | 3 | `titulo` vazio | `3,titulo,vazio` |
      | 4 | `ano_fonte` = `mil novecentos` | `4,ano_fonte,nao_inteiro` |
      | 5 | `ano_fonte` = `3000` | `5,ano_fonte,fora_da_faixa` |
      | 6 | `tipo` = `historia` | `6,tipo,fora_da_lista` |
      | 7 | `licenca` vazia | `7,licenca,vazio` |
      | 8 | `id` igual ao da linha 2 | `8,id,repetido` |
      | 9 | `mesorregiao` = `seridó` | `9,mesorregiao,fora_da_lista` |
      | 10 | `texto` com um trecho só: `"Único trecho de teste."` | `10,texto,quantidade_trechos` |
      | 11 | `texto` com o segundo trecho sem aspas: `"Primeiro trecho de teste." \| Segundo trecho de teste.` | `11,texto,sem_aspas` |

      Lembre: o cabeçalho é a linha 1, então a primeira narrativa (a certa) é a linha 2. Copie esta tabela para a descrição do PR: é a "resposta esperada" do seu teste.

   5. Baixe como CSV: **Arquivo → Fazer download → Valores separados por vírgula (.csv)**. Mova o arquivo baixado para a pasta `dados` do repositório e renomeie para `teste_validador.csv`.

   > **Nunca abra nem salve o CSV no Excel.** O Excel do Windows estraga os acentos. Para ver o arquivo, abra no VS Code.

   Abra o `dados/teste_validador.csv` no VS Code. A linha 2 aparece assim:

   ```
   1,A lenda de teste,lenda,livre,Natal,leste,"""Primeiro trecho de teste."" | ""Segundo trecho de teste.""",teste; lenda,SOBRENOME. Obra de teste.,,1950,dominio_publico
   ```

   Repare em duas coisas: a `url_fonte` vazia virou duas vírgulas seguidas (`,,`); e o `texto` ficou entre aspas, com cada aspa de dentro **dobrada** (`""`). É assim que o CSV guarda um valor que tem aspas. O módulo `csv` do Python desfaz isso sozinho na leitura: no seu programa, o valor chega como `"Primeiro trecho de teste." | "Segundo trecho de teste."`.

8. Confira que o Python consegue ler o arquivo. No terminal, digite `python` e, dentro dele:

   ```python
   import csv
   with open("dados/teste_validador.csv", encoding="utf-8") as arquivo:
       for linha in csv.DictReader(arquivo):
           print(linha["id"], linha["titulo"], linha["texto"])
   ```

   Devem aparecer as 10 narrativas (a da linha 3 com o título vazio), com o `texto` mostrando as aspas normais, sem as aspas dobradas. Para sair do Python: `exit()`.

   Faça o *commit*: `git add dados/teste_validador.csv` e `git commit -m "test: adiciona planilha de teste com erros conhecidos"`.

**Quarta e quinta, 25 e 26/11: a primeira versão do validador**

9. Crie `scripts/validar.py`. Nesta sprint, ele faz **quatro coisas**:

   1. pega o nome do arquivo que veio no comando;
   2. confere se o cabeçalho tem as 12 colunas certas, na ordem certa. Se não tiver, avisa e para;
   3. percorre as linhas e, para cada coluna obrigatória vazia, mostra `Linha N, coluna X: vazio`;
   4. no fim, mostra quantas linhas leu e quantos erros encontrou.

10. **As peças que você vai usar.**

    O nome do arquivo que vem no comando fica na lista `sys.argv` (https://docs.python.org/pt-br/3/library/sys.html#sys.argv). A posição 0 é o próprio programa:

    ```python
    import sys

    # python scripts\validar.py dados\teste_validador.csv
    # sys.argv[0] -> "scripts\validar.py"
    # sys.argv[1] -> "dados\teste_validador.csv"

    if len(sys.argv) != 2:
        print("Uso: python scripts\\validar.py ARQUIVO.csv")
        sys.exit(1)

    caminho = sys.argv[1]
    ```

    As colunas, em listas, no começo do programa (é aqui que o formato da [seção 2](#formato) vira código):

    ```python
    COLUNAS = ["id", "titulo", "tipo", "publico", "municipio", "mesorregiao",
               "texto", "palavras_chave", "fonte", "url_fonte", "ano_fonte", "licenca"]

    OBRIGATORIAS = ["id", "titulo", "tipo", "publico", "municipio",
                    "mesorregiao", "texto", "fonte", "licenca"]
    ```

    O `DictReader` guarda os nomes do cabeçalho em `leitor.fieldnames`. Compare com a sua lista:

    ```python
    leitor = csv.DictReader(arquivo)
    if leitor.fieldnames != COLUNAS:
        print("Cabeçalho diferente do formato.")
        print("Esperado:", COLUNAS)
        print("Encontrado:", leitor.fieldnames)
        sys.exit(1)
    ```

    Para numerar as linhas a partir de 2 (lembre: a linha 1 é o cabeçalho), use o `enumerate` com `start=2` (https://docs.python.org/pt-br/3/library/functions.html#enumerate):

    ```python
    for numero, linha in enumerate(leitor, start=2):
        # numero é 2, 3, 4...  linha é um dicionário: linha["titulo"]
        ...
    ```

    Para saber se um valor está vazio, tire os espaços com `.strip()` e veja se sobrou alguma coisa:

    ```python
    valor = linha["titulo"].strip()
    if valor == "":
        ...
    ```

    Não escreva um `if` para cada coluna: percorra a lista `OBRIGATORIAS` com um `for` e use `linha[coluna]`.

11. **Guarde os erros em uma lista**, e não só mostre na tela. Na Sprint 2, essa mesma lista vai ser gravada no relatório. Cada erro é uma tupla com três partes:

    ```python
    erros = []
    ...
    erros.append((numero, coluna, "vazio"))
    ...
    for numero, coluna, erro in erros:
        print(f"Linha {numero}, coluna {coluna}: {erro}")
    ```

12. Organize o programa em funções. Um esqueleto (os comentários dizem o que fazer; o código é seu):

    ```python
    import csv
    import sys

    COLUNAS = [...]
    OBRIGATORIAS = [...]


    def conferir_vazios(numero, linha, erros):
        """Acrescenta em erros um ("vazio") para cada coluna obrigatória vazia da linha."""
        ...


    def validar(caminho):
        """Lê o CSV, confere o cabeçalho, confere cada linha e devolve (total_de_linhas, erros)."""
        ...


    # aqui: conferir o sys.argv, chamar validar, mostrar cada erro e os totais
    ```

13. Rode com o arquivo de teste:

    ```
    python scripts\validar.py dados\teste_validador.csv
    ```

    Nesta sprint, ele deve encontrar **só os 2 erros de campo vazio** (linhas 3 e 7). Os outros (número, lista, repetido, trechos e aspas) são da Sprint 2.

    Teste também o cabeçalho: copie o arquivo de teste para um arquivo temporário, troque `titulo` por `Titulo` no cabeçalho e rode. O validador deve avisar e parar. Apague o arquivo temporário depois.

14. *Commit*, envio e PR com `Closes #7` até **quinta, 26/11**. Em **Como testar**, cole a saída do terminal.

### Como saber que deu certo

- `python scripts\validar.py dados\teste_validador.csv` mostra os 2 erros de `vazio`, `Linhas lidas: 10` e `Erros encontrados: 2`.
- Com o cabeçalho errado, o programa avisa e para, sem mostrar erros de linha.
- Rodar sem o nome do arquivo mostra a mensagem de uso, sem erro do Python.

### Entrega da sprint

- [ ] `dados/teste_validador.csv` com 10 narrativas e 9 erros conhecidos
- [ ] `scripts/validar.py` conferindo cabeçalho e campos vazios
- [ ] PR para a `develop` com `Closes #7` e a saída do terminal, até **26/11**

### Erros comuns

- **`FileNotFoundError`**: você não está na raiz do repositório, ou digitou o caminho errado. Rode `pwd` para ver onde está; se estiver dentro de `scripts`, volte com `cd ..`.
- **`KeyError: 'titulo'`**: o nome da coluna no cabeçalho está diferente (maiúscula, espaço, acento). Confira a primeira linha do CSV.
- **Acentos estranhos (`Ã§`)**: faltou `encoding="utf-8"` no `open`.
- **A numeração das linhas começa em 1 ou em 0**: faltou o `start=2` no `enumerate`.

---

<a id="sprint-2"></a>
# Sprint 2: 27/11 a 03/12 - Validador completo

**Branch:** `feature/validador-completo` · **Issue:** #8 · **PR até:** quinta, 03/12

**O que você vai entregar:** o validador com as 7 regras da [seção 2.3](#formato) e o relatório de erros gravado em CSV.

### Passo a passo

1. Atualize a `develop` (o seu PR da Sprint 1 já deve ter sido integrado) e crie a *branch*:

   ```
   git checkout develop
   git pull
   git checkout -b feature/validador-completo
   ```

2. **Regra `nao_inteiro` (colunas `id` e `ano_fonte`).** Só confira se o valor **não estiver vazio** (o `id` vazio já é `vazio`; o `ano_fonte` vazio não é erro, porque é opcional). Para saber se um texto é número inteiro, tente converter com `int()`: se não der, o Python lança um `ValueError`:

   ```python
   try:
       ano = int(valor)
   except ValueError:
       # não é inteiro: registre o erro "nao_inteiro"
       ...
   ```

   Teste no terminal do Python, digitando `int("1950")`, `int("mil")` e `int("19.5")`, para ver o que acontece em cada caso.

3. **Regra `fora_da_faixa` (só `ano_fonte`).** Só confira se o ano **é** inteiro. Se for menor que 1500 ou maior que 2026, é `fora_da_faixa`. Guarde os limites em constantes no começo do programa (`ANO_MINIMO = 1500`, `ANO_MAXIMO = 2026`), e não espalhados no meio do código.

4. **Regra `fora_da_lista` (`tipo`, `publico`, `mesorregiao`, `licenca`).** Guarde as listas em um dicionário no começo do programa. A chave é a coluna; o valor é o conjunto de valores aceitos:

   ```python
   LISTAS = {
       "tipo": {"lenda", "conto", "causo", "mito", "cordel"},
       "publico": {...},
       "mesorregiao": {...},
       "licenca": {...},
   }
   ```

   Para conferir, percorra o dicionário com `for coluna, aceitos in LISTAS.items():` e use o operador `not in`. De novo: só confira se o valor não estiver vazio.

5. **Regra `repetido` (`id`).** Use um conjunto com os `id` já vistos, criado **antes** do `for` das linhas:

   ```python
   ids_vistos = set()
   ...
   if valor in ids_vistos:
       # repetido
       ...
   else:
       ids_vistos.add(valor)
   ```

   Pense na ordem: a primeira vez que um `id` aparece não é erro; só a segunda.

6. **Regras do `texto` (`quantidade_trechos` e `sem_aspas`).** Só confira se o `texto` não estiver vazio.

   Primeiro, separe os trechos pelo `|` e tire os espaços de cada um (isso se chama *list comprehension*; pesquise "list comprehension python" se não conhecer):

   ```python
   trechos = [t.strip() for t in valor.split("|")]
   ```

   Experimente no terminal do Python com `'"Um." | "Dois."'.split("|")` para ver o que o `split` devolve.

   **Quantidade:** se `len(trechos)` for menor que 2 ou maior que 3, registre `quantidade_trechos` e **não confira as aspas** (regra "um erro por coluna").

   **Aspas:** cada trecho tem de começar com uma aspa de abrir e terminar com uma aspa de fechar. Guarde as aspas aceitas em constantes no começo do programa:

   ```python
   ABRE_ASPAS = ('"', "“")
   FECHA_ASPAS = ('"', "”")
   ```

   O `startswith` e o `endswith` aceitam uma tupla e respondem `True` se o texto começar (ou terminar) com **qualquer um** dos itens. Teste no terminal do Python:

   ```python
   '"Era uma vez."'.startswith(('"', "“"))   # True
   'Era uma vez."'.startswith(('"', "“"))    # False
   ```

   Um trecho que é só uma aspa (`"`) começa e termina com aspas, mas não é um trecho: exija também `len(trecho) >= 2`. Se **algum** trecho falhar, registre **um** `sem_aspas` para a coluna, mesmo que vários trechos estejam sem aspas. Uma variável que começa `True` e vira `False` dentro do `for` resolve isso (ou pesquise a função `all()` do Python).

   Para digitar as aspas curvas no código, copie daqui: `“` e `”`.

7. **Uma função por regra.** Siga o modelo da `conferir_vazios` da Sprint 1: `conferir_inteiros`, `conferir_listas`, `conferir_repetido`, `conferir_texto`. A função `validar` chama todas para cada linha. Para cumprir a regra "um erro por coluna, no máximo", cada função ignora as colunas vazias.

8. **O relatório em CSV.** No fim, grave a lista de erros em `resultados/erros_<nome do arquivo>.csv`. Para montar o nome, use o `os.path` (https://docs.python.org/pt-br/3/library/os.path.html):

   ```python
   import os

   nome = os.path.basename(caminho)          # "teste_validador.csv"
   nome_sem_extensao = os.path.splitext(nome)[0]   # "teste_validador"
   saida = os.path.join("resultados", f"erros_{nome_sem_extensao}.csv")
   ```

   Crie a pasta, caso não exista, e grave com o `csv.writer`:

   ```python
   os.makedirs("resultados", exist_ok=True)
   with open(saida, "w", encoding="utf-8", newline="") as arquivo:
       escritor = csv.writer(arquivo)
       escritor.writerow(["linha", "coluna", "erro"])
       for erro in erros:
           escritor.writerow(erro)
   ```

   O `newline=""` é obrigatório no Windows: sem ele, o arquivo sai com uma linha em branco entre cada linha.

   O relatório é gravado **mesmo quando não há erro** (só com o cabeçalho). Assim, quem rodar sabe que a validação aconteceu.

9. **Ordem dos erros.** Mostre e grave os erros na ordem das linhas (2, 3, 4...). Dentro da mesma linha, a ordem não importa: o Ítalo compara o seu relatório com o gabarito como conjuntos, sem olhar a ordem.

10. Rode com o arquivo de teste:

   ```
   python scripts\validar.py dados\teste_validador.csv
   ```

   Agora ele deve encontrar **os 9 erros** da tabela da Sprint 1, passo 7. Abra o `resultados\erros_teste_validador.csv` no VS Code e confira que ele é igual à coluna "O validador deve dizer" daquela tabela, com o cabeçalho `linha,coluna,erro`.

11. **Teste os casos de borda.** Acrescente na planilha `Teste do validador`, no Google Planilhas, mais 5 linhas, baixe de novo o CSV por cima do `dados/teste_validador.csv` e atualize a tabela de resposta esperada:
    - uma linha com **dois erros** em colunas diferentes (por exemplo, `titulo` vazio e `tipo` = `fabula`): devem sair os dois;
    - uma linha com `ano_fonte` = `-5`: o `int` aceita, então deve sair `fora_da_faixa`;
    - uma linha com `tipo` = ` lenda ` (com espaços): **não** é erro;
    - uma linha com **3 trechos** e **aspas curvas**: `“Um.” | “Dois.” | “Três.”`: **não** é erro;
    - uma linha com **4 trechos**: `"Um." | "Dois." | "Três." | "Quatro."`: deve sair `quantidade_trechos`.

12. **Se o gerador do Aluno 2 já estiver na `develop`**, teste com ele também (se ainda não estiver, pule este passo):

    ```
    git checkout develop
    git pull
    git checkout feature/validador-completo
    git merge develop
    python scripts\gerar_fake.py 100
    python scripts\validar.py dados\fake\fake_100.csv
    ```

    Abra o gabarito do gerador (`dados\fake\fake_100_gabarito.csv`) e o seu relatório (`resultados\erros_fake_100.csv`) lado a lado no VS Code (botão direito na aba → **Split Right**). Devem ser iguais. **Não envie para o Git** os arquivos de `dados/fake` nem de `resultados/`: o seu `git add` leva só os seus dois arquivos.

13. *Commit* a cada regra que funcionar (`feat: confere números inteiros e faixa do ano`, `feat: confere valores das listas`, `feat: confere trechos e aspas do texto`...), envio e PR com `Closes #8` até **quinta, 03/12**. Em **Como testar**, cole a saída do terminal e a tabela de resposta esperada.

### Como saber que deu certo

- Com o arquivo de teste, a saída na tela e o `resultados\erros_teste_validador.csv` batem, erro por erro, com a tabela de resposta esperada.
- Uma linha certa não gera erro nenhum.
- Um valor com espaços sobrando não gera erro.

### Entrega da sprint

- [ ] As 7 regras: `vazio`, `nao_inteiro`, `fora_da_faixa`, `fora_da_lista`, `repetido`, `quantidade_trechos`, `sem_aspas`
- [ ] Relatório em `resultados/erros_<nome>.csv`, com o cabeçalho `linha,coluna,erro`
- [ ] `dados/teste_validador.csv` com os casos de borda e a tabela de resposta esperada no PR
- [ ] PR para a `develop` com `Closes #8`, até **03/12**

### Erros comuns

- **Linha em branco entre as linhas do relatório:** faltou `newline=""` no `open` de escrita.
- **O `id` da primeira linha aparece como repetido:** você está conferindo o conjunto **depois** de acrescentar o `id` nele. Confira antes, acrescente depois.
- **`fora_da_lista` para valores certos:** você esqueceu o `.strip()`, ou a lista tem um valor digitado diferente do formato (com acento, com maiúscula).
- **Erro `vazio` e `nao_inteiro` na mesma coluna:** a função de inteiros não está ignorando os valores vazios.
- **`sem_aspas` para um texto certo:** faltou o `.strip()` em cada trecho depois do `split`, e o espaço antes da aspa faz o `startswith` falhar.
- **Dois `sem_aspas` na mesma linha:** você está registrando um erro por trecho. A regra é um erro por coluna.

---

<a id="sprint-3"></a>
# Sprint 3: 04/12 a 10/12 - Ajustes

**Branch:** `fix/validador-ajustes` · **Issue:** #9

Na sexta, 04/12, o Ítalo roda o seu validador na planilha real dele e nas planilhas do gerador do Aluno 2. Se aparecer algum problema (um erro que o validador deixou passar, um erro apontado que não existia, uma mensagem confusa), ele comenta na sua *issue* #9.

### Passo a passo

1. Acompanhe a *issue* #9 de sexta a terça. Se não houver nenhum pedido de ajuste até **terça, 08/12**, comente na *issue*: `Nenhum ajuste pedido` e eu fecho.

2. Se houver pedido de ajuste:

   ```
   git checkout develop
   git pull
   git checkout -b fix/validador-ajustes
   ```

   Corrija, acrescente na planilha `Teste do validador` uma linha que reproduza o problema (assim ele não volta), baixe de novo o CSV por cima do `dados/teste_validador.csv`, rode, faça o *commit* e abra o PR com `Closes #9` até **terça, 08/12**.

3. **Extra, só se sobrar tempo e a *issue* #9 já estiver resolvida:** conferir se o município existe no RN.
   - Abra no navegador https://servicodados.ibge.gov.br/api/v1/localidades/estados/RN/municipios e salve a página como `dados/municipios_rn.json` (**Ctrl + S**).
   - Leia o arquivo com o módulo `json` (`json.load`), monte um conjunto com os nomes (`municipio["nome"]`) e confira a coluna `municipio`.
   - Use o código de erro `municipio_inexistente`, na coluna `municipio`. O gerador do Aluno 2 só usa municípios que existem, então esse erro não aparece nas bases fictícias nem atrapalha a comparação do Ítalo; ele só aparece na planilha real, se houver um município escrito errado.
   - Acrescente uma linha à planilha de teste com `municipio` = `Natall` e a resposta esperada `N,municipio,municipio_inexistente` (N é o número da linha), e abra um PR separado com `Refs #9`.

### Entrega da sprint

- [ ] Ajustes pedidos na *issue* #9 resolvidos, com PR e `Closes #9`, até **08/12**; ou comentário `Nenhum ajuste pedido`

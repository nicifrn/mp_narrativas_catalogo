# Plano de desenvolvimento - Samuel: conversor de CSV para JSON e verificador

**Aluno:** Samuel (@samuelmarinho10) - Técnico Integrado em Informática

**Orientador:** Prof. Bruno Gomes (@brunogomesifrn) - NIC/IFRN

**Trabalho do qual você participa:** catálogo estruturado de narrativas do RN, do Ítalo (@italogomees). O plano dele está em [`docs/01_italo_v2_narrativas_desenvolvimento.md`](01_italo_v2_narrativas_desenvolvimento.md).

**Repositório:** https://github.com/nicifrn/mp_narrativas_catalogo

**Período:** 23/11/2026 a 10/12/2026. **A sua entrega principal é na quinta, 03/12.**

> Leia este documento inteiro antes de começar. Ele tem tudo o que você precisa: o que programar, em que ordem, com quais comandos e onde pesquisar. **Não há *issues* no GitHub: este documento é o seu roteiro.** Siga as sprints na ordem e marque as caixas da "Entrega da sprint" à medida que for terminando.

---

## Sumário

- [1. O que você vai fazer](#ideia)
- [2. O formato da planilha e as regras da conversão](#formato)
- [3. Cronograma](#cronograma)
- [4. Como trabalhar no repositório](#fluxo-git)
- [Sprint 1 - Ambiente, arquivo de teste e primeira versão do conversor](#sprint-1)
- [Sprint 2 - Conversor completo e verificador](#sprint-2)
- [Sprint 3 - Ajustes](#sprint-3)

---

<a id="ideia"></a>
## 1. O que você vai fazer

O Ítalo está montando uma planilha com narrativas populares do Rio Grande do Norte (lendas, contos, causos) para o acervo da plataforma Narrativas, do IFRN. Planilha é ótima para preencher, mas um sistema web não carrega planilha: ele carrega **JSON**, um formato em que cada valor tem um **tipo** (texto, número, lista, nulo).

**Você vai programar duas coisas:**

1. **o conversor (`scripts/converter.py`)**: lê a planilha em CSV e grava a mesma informação em JSON, convertendo cada coluna para o tipo certo (o `id` vira número, as palavras-chave viram lista, o que estiver vazio vira nulo);
2. **o verificador (`scripts/verificar_json.py`)**: lê o CSV e o JSON e confere, narrativa por narrativa e coluna por coluna, se o JSON saiu **igual** ao CSV. É ele que prova que o conversor não perdeu nem estragou nada.

Você roda assim:

```
python scripts\converter.py dados\teste_conversor.csv dados\teste_conversor.json
python scripts\verificar_json.py dados\teste_conversor.csv dados\teste_conversor.json
```

E eles respondem mais ou menos assim:

```
Narrativas convertidas: 5
JSON gravado em dados\teste_conversor.json

Narrativas no CSV: 5
Narrativas no JSON: 5
Diferenças: 0
```

**O que você só usa:** Python e os módulos `csv`, `json` e `sys`, que já vêm com ele. Você **não instala nada**.

**O que fica de fora:** conferir se a planilha tem erros (isso é o validador do Ítalo, que roda **antes** do conversor), interface gráfica, `pandas`, banco de dados.

**Você não depende de ninguém para começar.** O formato está fechado na [seção 2](#formato), e você mesmo cria o arquivo de teste.

### Quem faz o quê na equipe

| Quem | Faz | Arquivos |
|---|---|---|
| Ítalo | Planilha com narrativas reais, validador, estatísticas, integração e o RCC | os do plano dele |
| **Você (Samuel)** | **Conversor e verificador** | **`scripts/converter.py`, `scripts/verificar_json.py`, `dados/teste_conversor.csv`, `dados/teste_conversor.json` e `dados/teste_conversor_estragado.json`** |
| Gleidson | Gerador de narrativas fictícias, com erros de propósito | `scripts/gerar_fake.py` |

**Mexa só nos seus arquivos.** Assim ninguém atrapalha ninguém no Git. Se precisar de outra coisa no repositório, peça ao Ítalo.

Na sexta, 04/12, o Ítalo roda o seu conversor na planilha real dele, já corrigida, e o seu verificador em cima do resultado. O `dados/narrativas.json` que sai daí é o catálogo que a plataforma vai carregar.

---

<a id="formato"></a>
## 2. O formato da planilha e as regras da conversão

Este formato é o **contrato** da equipe: você, o Ítalo e o Gleidson usam exatamente estes nomes, nesta ordem. Ele não muda. O Ítalo publica a explicação detalhada de cada coluna em `docs/formato_planilha.md` até 24/11, mas você já pode começar com a tabela abaixo.

### 2.1 As colunas e o que vira cada uma no JSON

| # | Coluna | Obrigatória | No CSV | No JSON |
|---|---|---|---|---|
| 1 | `id` | sim | `7` | número inteiro: `7` |
| 2 | `titulo` | sim | texto | texto |
| 3 | `tipo` | sim | `lenda`, `conto`, `causo`, `mito` ou `cordel` | texto |
| 4 | `publico` | sim | `infantil`, `juvenil`, `adulto` ou `livre` | texto |
| 5 | `municipio` | sim | texto | texto |
| 6 | `mesorregiao` | sim | `oeste`, `central`, `agreste` ou `leste` | texto |
| 7 | `texto` | sim | de 2 a 3 trechos, cada um entre aspas, separados por ` \| ` | texto, **do jeito que está** (não separe os trechos) |
| 8 | `palavras_chave` | não | `lobisomem; sertão` (separadas por `;`) | lista: `["lobisomem", "sertão"]`. Vazia vira lista vazia: `[]` |
| 9 | `fonte` | sim | texto | texto |
| 10 | `url_fonte` | não | texto ou vazio | texto, ou `null` se estiver vazia |
| 11 | `ano_fonte` | não | `1952` ou vazio | número inteiro: `1952`, ou `null` se estiver vazio |
| 12 | `licenca` | sim | `dominio_publico`, `cc_by`, `cc_by_sa`, `direitos_reservados` ou `desconhecida` | texto |

### 2.2 Regras do arquivo e da conversão

- O CSV é UTF-8, separado por vírgula, com o cabeçalho na primeira linha. **Numeração das linhas:** o cabeçalho é a **linha 1**; a primeira narrativa é a **linha 2**, igual ao Google Planilhas.
- O JSON é **uma lista** de objetos, um por narrativa, **na mesma ordem** do CSV. Cada objeto tem as **12 chaves**, com os mesmos nomes e na mesma ordem das colunas.
- Tire os espaços sobrando no começo e no fim de todo valor (`" lenda "` vira `"lenda"`), e de cada palavra-chave.
- Os acentos ficam legíveis no arquivo: `"Caicó"`, e não `"Caicó"`.
- O conversor **não procura erros**: o validador do Ítalo roda antes. Mas, se encontrar um `id` ou um `ano_fonte` que não é número, ele não pode "quebrar" com uma mensagem do Python: mostra em que linha está o problema e para (Sprint 2, passo 5).

Um exemplo. Esta linha do CSV:

```
3,O Boi Tatá,mito,livre,Apodi,oeste,"""Primeiro trecho."" | ""Segundo trecho.""",,SOBRENOME. Obra.,,,desconhecida
```

vira este objeto no JSON:

```json
{
  "id": 3,
  "titulo": "O Boi Tatá",
  "tipo": "mito",
  "publico": "livre",
  "municipio": "Apodi",
  "mesorregiao": "oeste",
  "texto": "\"Primeiro trecho.\" | \"Segundo trecho.\"",
  "palavras_chave": [],
  "fonte": "SOBRENOME. Obra.",
  "url_fonte": null,
  "ano_fonte": null,
  "licenca": "desconhecida"
}
```

No CSV, as aspas de dentro do `texto` aparecem **dobradas** (`""`); no JSON, aparecem como `\"`. São só os jeitos diferentes de cada formato guardar aspas dentro de um valor: o módulo `csv` e o módulo `json` cuidam disso sozinhos.

---

<a id="cronograma"></a>
## 3. Cronograma

| Sprint | Período | O que você faz |
|---|---|---|
| 1 | 23/11 a 26/11 | Ambiente, Git, estudo dos módulos `csv` e `json`, arquivo de teste e primeira versão do conversor (tudo como texto). **PR até 26/11** |
| 2 | 27/11 a 03/12 | Conversor completo (tipos, listas e nulos) e verificador. **Entrega: 03/12** |
| 3 | 04/12 a 10/12 | Ajustes que o Ítalo ou eu pedirmos depois da integração |

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

| Sprint | *Branch* |
|---|---|
| 1 | `feature/conversor-base` |
| 2 | `feature/conversor-verificador` |
| 3 | `fix/conversor-ajustes` |

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
git add scripts/converter.py dados/teste_conversor.csv dados/teste_conversor.json
git commit -m "feat: converte o CSV em uma lista de objetos JSON"
git push
```

Repare que o `git add` leva **só os seus arquivos** (na Sprint 2, acrescente o `scripts/verificar_json.py` e o `dados/teste_conversor_estragado.json`). Assim você não envia sem querer arquivos de outras pessoas ou pastas como `__pycache__`.

Na primeira vez que der `git push` em uma *branch* nova, o Git responde com um erro e mostra o comando certo, algo como `git push --set-upstream origin feature/conversor-base`. Copie e rode exatamente o comando que ele mostrar.

### 4.3 Mensagens de *commit*

Em português, curtas, com o verbo no presente e um prefixo:

| Prefixo | Quando | Exemplo |
|---|---|---|
| `feat:` | algo novo funcionando | `feat: converte palavras-chave em lista` |
| `fix:` | correção | `fix: mantém os acentos no JSON` |
| `test:` | arquivo de teste | `test: adiciona planilha de teste do conversor` |

**Proibido:** `ajustes`, `mudanças`, `update`, `correções`. Faça pelo menos **2 *commits* por semana**.

### 4.4 O *pull request* (PR)

1. `git status` deve dizer `nothing to commit, working tree clean`.
2. No GitHub, abra o repositório. Clique em **Compare & pull request** na faixa amarela. Se não aparecer: aba **Pull requests → New pull request**, com **base: `develop`** e **compare: a sua *branch***.
3. Preencha o modelo: **Sprint**, **Objetivo**, **O que foi feito** e **Como testar** (os comandos e a saída do terminal, copiada e colada).
4. Em **Reviewers**, marque `brunogomesifrn` e `italogomees`.
5. No grupo da equipe, avise: `PR #X pronto para revisão`.

**Você não faz o *merge*.** Se pedirmos ajustes (nos comentários do PR), faça na mesma *branch*: o PR se atualiza sozinho.

### 4.5 Quando travar

**Travou mais de 40 minutos no mesmo erro? Pare e peça ajuda.** Mande mensagem no grupo da equipe, me marcando, com: o que você estava tentando fazer, o comando que rodou e **a mensagem de erro inteira, copiada e colada**.

---

<a id="sprint-1"></a>
# Sprint 1: 23/11 a 26/11 - Ambiente, arquivo de teste e primeira versão do conversor

**Branch:** `feature/conversor-base` · **PR até:** quinta, 26/11

**O que você vai entregar:** o arquivo de teste com 5 narrativas e uma primeira versão do conversor, que grava o JSON com **todos os valores como texto**, acentos legíveis e as 12 chaves em cada narrativa.

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
   git checkout -b feature/conversor-base
   ```

   O `python --version` deve mostrar `Python 3.` alguma coisa. O `git branch` deve mostrar `* develop`.

5. Crie as pastas `scripts` e `dados`, se ainda não existirem (no explorador do VS Code, à esquerda: botão direito → **New Folder**).

**Segunda e terça, 23 e 24/11: estudar**

6. Leia e teste os exemplos destas páginas, **digitando** os códigos (não copie e cole: digitando você aprende):
   - Leitura e escrita de arquivos: https://docs.python.org/pt-br/3/tutorial/inputoutput.html#reading-and-writing-files
   - O módulo `csv`, principalmente o `csv.DictReader`: https://docs.python.org/pt-br/3/library/csv.html
   - O módulo `json`, principalmente o `json.dump` e o `json.load`: https://docs.python.org/pt-br/3/library/json.html
   - Dicionários e listas: https://docs.python.org/pt-br/3/tutorial/datastructures.html

   Se preferir vídeo, procure no YouTube por "python csv DictReader" e "python json dump".

7. Experimente o `json` no terminal. Digite `python` e, dentro dele:

   ```python
   import json
   narrativa = {"id": 1, "municipio": "Caicó", "palavras_chave": ["sertão"], "ano_fonte": None}
   print(json.dumps(narrativa))
   print(json.dumps(narrativa, ensure_ascii=False, indent=2))
   ```

   Compare as duas saídas: na primeira, `Caicó` aparece como `Caicó`; na segunda, com o acento, uma chave por linha. Repare também que o `None` do Python vira `null` no JSON, e que o `1` sai sem aspas (é número), enquanto `"Caicó"` sai com aspas (é texto). Para sair do Python: `exit()`.

**Terça, 24/11: o arquivo de teste**

8. Crie o arquivo de teste `dados/teste_conversor.csv`: uma planilha pequena, **sem erros**, em que cada narrativa testa um caso diferente da conversão. Monte no **Google Planilhas**, que cuida sozinho das aspas e das vírgulas do CSV:

   1. Abra https://sheets.google.com → **Em branco**. Nome: `Teste do conversor`.
   2. Na linha 1, digite os 12 nomes das colunas, um por célula, de A a L, exatamente como na [seção 2.1](#formato).
   3. Preencha 5 narrativas (linhas 2 a 6). Invente os valores, mas siga o formato. Cada uma testa um caso:

      | Linha | `id` | O que ela testa |
      |---|---|---|
      | 2 | 1 | narrativa **completa**: todas as colunas preenchidas, `municipio` = `Caicó`, `palavras_chave` = `lobisomem; sertão`, `ano_fonte` = `1952` |
      | 3 | 2 | `url_fonte` e `ano_fonte` **vazios** (no JSON: `null` e `null`) |
      | 4 | 3 | `palavras_chave` **vazia** (no JSON: `[]`) |
      | 5 | 4 | `palavras_chave` com **espaços sobrando e `;` no fim**: ` rio ;  encantamento; ` (no JSON: `["rio", "encantamento"]`) |
      | 6 | 5 | `titulo` com **vírgula** (`A Cobra, o Rio e a Lua`), `texto` com **aspas curvas** (`“Um.” \| “Dois.”`) e `tipo` com espaços: ` lenda ` (no JSON: `"lenda"`) |

   4. Baixe como CSV: **Arquivo → Fazer download → Valores separados por vírgula (.csv)**. Mova para a pasta `dados` do repositório e renomeie para `teste_conversor.csv`.

   > **Nunca abra nem salve o CSV no Excel.** O Excel do Windows estraga os acentos. Para ver o arquivo, abra no VS Code.

   Abra o `dados/teste_conversor.csv` no VS Code e confira: o cabeçalho na linha 1, os acentos certos, o título com vírgula entre aspas e as aspas retas do `texto` **dobradas** (`""`). Está certo: é assim que o CSV guarda esses valores.

   Copie a tabela acima para a descrição do PR: é a "resposta esperada" do seu teste.

   Faça o *commit*: `git add dados/teste_conversor.csv` e `git commit -m "test: adiciona planilha de teste do conversor"`.

**Quarta e quinta, 25 e 26/11: a primeira versão do conversor**

9. Crie `scripts/converter.py`. Nesta sprint, ele faz **quatro coisas**:

   1. pega os dois nomes de arquivo que vieram no comando (o CSV de entrada e o JSON de saída);
   2. lê o CSV, cada linha como um dicionário, e tira os espaços sobrando de cada valor;
   3. grava a lista de dicionários no JSON, com acentos legíveis e uma chave por linha;
   4. mostra quantas narrativas converteu e onde gravou.

   Nesta sprint, **todos os valores ficam como texto** (`"id": "1"`). Os tipos entram na Sprint 2.

10. **As peças que você vai usar.**

    Os nomes de arquivo que vêm no comando ficam na lista `sys.argv` (https://docs.python.org/pt-br/3/library/sys.html#sys.argv). A posição 0 é o próprio programa:

    ```python
    import sys

    # python scripts\converter.py dados\teste_conversor.csv dados\teste_conversor.json
    # sys.argv[0] -> "scripts\converter.py"
    # sys.argv[1] -> "dados\teste_conversor.csv"
    # sys.argv[2] -> "dados\teste_conversor.json"

    if len(sys.argv) != 3:
        print("Uso: python scripts\\converter.py ENTRADA.csv SAIDA.json")
        sys.exit(1)
    ```

    Ler o CSV com cada linha como dicionário:

    ```python
    with open(caminho_csv, encoding="utf-8") as arquivo:
        for linha in csv.DictReader(arquivo):
            # linha é um dicionário: linha["titulo"], linha["ano_fonte"]...
            ...
    ```

    Tirar os espaços de todos os valores de uma vez (isso se chama *dict comprehension*; pesquise "dict comprehension python" se não conhecer):

    ```python
    limpa = {coluna: valor.strip() for coluna, valor in linha.items()}
    ```

    Gravar o JSON com acentos legíveis e identado:

    ```python
    with open(caminho_json, "w", encoding="utf-8") as arquivo:
        json.dump(narrativas, arquivo, ensure_ascii=False, indent=2)
    ```

    Rode uma vez **sem** o `ensure_ascii=False`, abra o JSON e tire um print; depois rode com ele e tire outro. A diferença (`Caicó` e `Caicó`) é uma boa figura para o RCC do Ítalo.

11. Organize em funções. Um esqueleto (os comentários dizem o que fazer; o código é seu):

    ```python
    import csv
    import json
    import sys


    def ler_csv(caminho):
        """Devolve a lista de narrativas (dicionários) do CSV, com os espaços tirados."""
        ...


    def gravar_json(narrativas, caminho):
        ...


    # aqui: conferir o sys.argv, chamar ler_csv, chamar gravar_json e mostrar o total
    ```

12. Rode com o arquivo de teste:

    ```
    python scripts\converter.py dados\teste_conversor.csv dados\teste_conversor.json
    ```

    Abra o `dados\teste_conversor.json` no VS Code e confira:
    - o arquivo começa com `[` e termina com `]` (é uma lista);
    - são 5 objetos, cada um com as 12 chaves, na ordem das colunas;
    - `Caicó` aparece com acento;
    - o título com vírgula está inteiro (`A Cobra, o Rio e a Lua`);
    - o `tipo` da narrativa 5 é `"lenda"`, sem os espaços.

    Teste também: rodar sem os nomes de arquivo (deve mostrar a mensagem de uso, sem erro do Python).

13. *Commit* (`feat: converte o CSV em uma lista de objetos JSON`), envio e PR até **quinta, 26/11**. Leve no `git add` o `dados/teste_conversor.json` também. Em **Como testar**, cole a saída do terminal e a primeira narrativa do JSON.

### Como saber que deu certo

- O JSON abre no VS Code sem nenhuma marcação vermelha (se o VS Code sublinhar algo de vermelho, o JSON está quebrado).
- São 5 narrativas, com as 12 chaves cada, acentos certos e sem espaços sobrando.
- Rodar sem os nomes de arquivo mostra a mensagem de uso.

### Entrega da sprint

- [ ] `dados/teste_conversor.csv` com 5 narrativas, uma para cada caso da tabela do passo 8
- [ ] `scripts/converter.py` gravando o JSON (ainda tudo como texto)
- [ ] `dados/teste_conversor.json` gerado pelo conversor
- [ ] PR para a `develop` com a saída do terminal, até **26/11**

### Erros comuns

- **`FileNotFoundError`**: você não está na raiz do repositório, ou digitou o caminho errado. Rode `pwd` para ver onde está; se estiver dentro de `scripts`, volte com `cd ..`.
- **`KeyError: 'titulo'`**: o nome da coluna no cabeçalho está diferente (maiúscula, espaço, acento). Confira a primeira linha do CSV.
- **Acentos estranhos (`Ã§`) no JSON**: faltou `encoding="utf-8"` em um dos dois `open`.
- **`Caicó` no JSON**: faltou o `ensure_ascii=False` no `json.dump`.
- **O JSON todo em uma linha só**: faltou o `indent=2`.

---

<a id="sprint-2"></a>
# Sprint 2: 27/11 a 03/12 - Conversor completo e verificador

**Branch:** `feature/conversor-verificador` · **PR até:** quinta, 03/12

**O que você vai entregar:** o conversor com todos os tipos da [seção 2.1](#formato) e o verificador, que confere se o JSON saiu igual ao CSV e aponta cada diferença.

### Passo a passo

1. Atualize a `develop` (o seu PR da Sprint 1 já deve ter sido integrado) e crie a *branch*:

   ```
   git checkout develop
   git pull
   git checkout -b feature/conversor-verificador
   ```

**O conversor completo**

2. **Uma função que converte uma narrativa.** Ela recebe o dicionário de textos que veio do CSV (já sem os espaços) e devolve o dicionário convertido:

   ```python
   def converter_linha(linha):
       """Recebe um dicionário com os textos do CSV e devolve o dicionário convertido."""
       narrativa = dict(linha)            # uma cópia, para não mexer no original
       narrativa["id"] = int(linha["id"])
       # ano_fonte: inteiro, ou None se estiver vazio
       # url_fonte: o texto, ou None se estiver vazio
       # palavras_chave: lista de textos, ou [] se estiver vazia
       return narrativa
   ```

   Texto vazio em Python é "falso". Isso ajuda nas conversões:

   ```python
   ano = int(linha["ano_fonte"]) if linha["ano_fonte"] else None
   ```

   Separar as palavras-chave e tirar os espaços de cada uma, jogando fora as vazias (isso se chama *list comprehension*; pesquise "list comprehension python" se não conhecer):

   ```python
   partes = linha["palavras_chave"].split(";")
   palavras = [p.strip() for p in partes if p.strip()]
   ```

   Teste no terminal do Python com `" rio ;  encantamento; ".split(";")` para ver o que o `split` devolve e por que o `if p.strip()` é necessário.

   O `texto` fica **como está**: não separe os trechos. A coluna foi pensada para receber, no futuro, o texto completo das narrativas cujos direitos permitirem.

3. Troque a `ler_csv` para chamar a `converter_linha` em cada linha. Rode com o arquivo de teste e confira o JSON contra a tabela da Sprint 1, passo 8:

   - `"id": 1` **sem aspas** (é número);
   - na narrativa 1, `"ano_fonte": 1952` sem aspas e `"palavras_chave": ["lobisomem", "sertão"]`;
   - na narrativa 2, `"url_fonte": null` e `"ano_fonte": null`;
   - na narrativa 3, `"palavras_chave": []`;
   - na narrativa 4, `"palavras_chave": ["rio", "encantamento"]`.

   Faça o *commit*: `feat: converte id, ano, url e palavras-chave para os tipos certos`.

4. **A ordem das chaves.** Como a `converter_linha` parte de uma cópia da linha do CSV, as chaves ficam na ordem das colunas. Confira no JSON: a primeira chave de cada objeto é `id` e a última é `licenca`.

5. **Número que não é número.** O validador do Ítalo roda antes do conversor, então a planilha não deveria ter erro. Mas, se alguém esquecer de validar, o conversor não pode parar com uma mensagem do Python que ninguém entende. Experimente: copie o arquivo de teste para `dados\temp.csv`, troque um `ano_fonte` por `mil novecentos` e rode o conversor nele. Ele para com `ValueError`.

   Trate isso com `try` e `except` (https://docs.python.org/pt-br/3/tutorial/errors.html#handling-exceptions): em volta da conversão de cada linha, pegue o `ValueError`, mostre a linha da planilha e pare:

   ```python
   for numero, linha in enumerate(csv.DictReader(arquivo), start=2):
       try:
           narrativas.append(converter_linha(limpa))
       except ValueError:
           print(f"Linha {numero}: id ou ano_fonte não é número inteiro.")
           print("Rode antes o validador: python scripts\\validar.py ARQUIVO.csv")
           sys.exit(1)
   ```

   O `enumerate` com `start=2` numera as linhas como no Google Planilhas (o cabeçalho é a linha 1). Rode de novo no `dados\temp.csv`: agora aparece a sua mensagem. **Apague o `dados\temp.csv`** depois.

   Faça o *commit*: `feat: mostra a linha quando id ou ano não é número`.

**O verificador (`scripts/verificar_json.py`)**

6. **O que o verificador faz.** Ele recebe o CSV e o JSON:

   ```
   python scripts\verificar_json.py dados\teste_conversor.csv dados\teste_conversor.json
   ```

   E confere:

   1. se o **número de narrativas** é o mesmo nos dois. Se não for, mostra os dois números e para;
   2. para cada narrativa, se o objeto do JSON tem **as 12 chaves**, com os nomes certos. Se não tiver, mostra `Linha N: chaves diferentes das 12 colunas`, conta uma diferença e não confere os valores dessa narrativa;
   3. para cada coluna de cada narrativa, se o valor do JSON é o **esperado**, pelas regras da [seção 2.1](#formato): o `id` é o número inteiro do CSV, o `ano_fonte` é o número ou `null`, e assim por diante;
   4. no fim, mostra quantas narrativas leu de cada lado e quantas diferenças encontrou.

   Cada diferença aparece assim:

   ```
   Linha 3, coluna ano_fonte: esperado 1950, encontrado "1950"
   ```

   Repare no exemplo: o valor está "certo", mas veio como **texto** (`"1950"`, com aspas) e deveria ser **número** (`1950`). É exatamente esse tipo de erro que o verificador existe para pegar.

7. **As peças do verificador.**

   Ler o JSON de volta para o Python:

   ```python
   with open(caminho_json, encoding="utf-8") as arquivo:
       narrativas = json.load(arquivo)    # uma lista de dicionários
   ```

   Ler o CSV como lista: `linhas = list(csv.DictReader(arquivo))`. Com as duas listas na mão, compare o tamanho com `len()` e percorra as duas juntas com o `zip` (https://docs.python.org/pt-br/3/library/functions.html#zip):

   ```python
   for numero, (linha, narrativa) in enumerate(zip(linhas, narrativas), start=2):
       ...
   ```

   O **valor esperado** de cada coluna: escreva uma função `valor_esperado(coluna, texto)` que recebe o nome da coluna e o texto do CSV (já com `.strip()`) e devolve o que deveria estar no JSON. Ela é parecida com a `converter_linha`, mas é **escrita de novo, no verificador**: se você importar a função do conversor, um erro no conversor passa despercebido, porque o verificador repete o mesmo erro.

   Para mostrar o valor com o tipo visível (texto com aspas, número sem), use o próprio `json`:

   ```python
   print(f"Linha {numero}, coluna {coluna}: esperado {json.dumps(esperado, ensure_ascii=False)}, "
         f"encontrado {json.dumps(encontrado, ensure_ascii=False)}")
   ```

   Compare com `!=`: em Python, `1950 != "1950"` dá `True` (número e texto são diferentes), e é isso que faz o verificador pegar um número gravado como texto.

   Organize em funções:

   ```python
   def valor_esperado(coluna, texto): ...
   def verificar(caminho_csv, caminho_json): ...   # devolve (total_csv, total_json, diferencas)

   # aqui: conferir o sys.argv, chamar verificar, mostrar as diferenças e os totais
   ```

8. Rode com o seu arquivo de teste. Deve dar **`Diferenças: 0`**.

9. **Teste o verificador com um JSON estragado.** Um verificador que sempre diz "0 diferenças" não prova nada: é preciso ver que ele **encontra** os erros. Copie o `dados\teste_conversor.json` para `dados\teste_conversor_estragado.json` e, no VS Code, estrague **à mão** quatro coisas:

   | O que você muda no JSON estragado | O verificador deve dizer |
   |---|---|
   | na narrativa 1, `"id": 1` vira `"id": "1"` | `Linha 2, coluna id: esperado 1, encontrado "1"` |
   | na narrativa 2, troque uma letra do `titulo` | `Linha 3, coluna titulo: ...` |
   | na narrativa 3, `"palavras_chave": []` vira `"palavras_chave": null` | `Linha 4, coluna palavras_chave: esperado [], encontrado null` |
   | na narrativa 4, apague a linha da chave `"fonte"` (cuidado com a vírgula: o JSON tem de continuar válido, sem marcação vermelha) | `Linha 5: chaves diferentes das 12 colunas` |

   Rode `python scripts\verificar_json.py dados\teste_conversor.csv dados\teste_conversor_estragado.json` e confira que saem as 4 diferenças.

   Teste também a quantidade: faça uma cópia temporária do JSON, apague a última narrativa inteira e rode. O verificador deve mostrar `Narrativas no CSV: 5` e `Narrativas no JSON: 4` e parar. Apague a cópia temporária depois.

   Copie a tabela acima para a descrição do PR: é a "resposta esperada" do verificador. O `teste_conversor_estragado.json` vai para o Git, para quem revisar poder repetir o teste.

10. **Teste com o gerador do Gleidson.** O primeiro PR dele (Sprint 1) deve estar na `develop` desde sexta, 27/11: ele gera 20 narrativas fictícias **sem erros**. Traga para a sua *branch* e teste:

    ```
    git checkout develop
    git pull
    git checkout feature/conversor-verificador
    git merge develop
    python scripts\gerar_fake.py
    python scripts\converter.py dados\fake\fake_20.csv dados\fake\fake_20.json
    python scripts\verificar_json.py dados\fake\fake_20.csv dados\fake\fake_20.json
    ```

    (Se o gerador já estiver na versão da Sprint 2, o primeiro comando é `python scripts\gerar_fake.py 20`. Se ele inserir erros, o conversor pode parar na linha de um `ano_fonte` errado: é a sua mensagem do passo 5 funcionando. Nesse caso, peça ao Gleidson para gerar com `TAXA_ERRO = 0`.) Se o gerador ainda não estiver na `develop`, pule este passo.

    **Não envie para o Git** os arquivos de `dados/fake`: o `.gitignore` do Ítalo já deixa essa pasta de fora.

11. *Commit* a cada parte que funcionar (`feat: verifica a quantidade e as chaves do JSON`, `feat: compara cada valor com o esperado`, `test: adiciona JSON estragado para testar o verificador`...), envio e PR até **quinta, 03/12**. Em **Como testar**, cole a saída do conversor, a do verificador com o JSON certo (0 diferenças) e com o estragado (4 diferenças), e a tabela do passo 9.

### Como saber que deu certo

- O JSON do arquivo de teste tem os tipos certos: números sem aspas, `null` onde estava vazio, listas entre colchetes.
- O verificador dá `Diferenças: 0` para o JSON certo e encontra as 4 diferenças do JSON estragado.
- Com um `ano_fonte` que não é número, o conversor mostra a linha da planilha, e não um erro do Python.

### Entrega da sprint

- [ ] `scripts/converter.py` com `id` e `ano_fonte` como número, `url_fonte` e `ano_fonte` vazios como `null` e `palavras_chave` como lista
- [ ] Mensagem com a linha da planilha quando `id` ou `ano_fonte` não é número
- [ ] `scripts/verificar_json.py` conferindo a quantidade, as chaves e cada valor
- [ ] `dados/teste_conversor.json` gerado de novo e `dados/teste_conversor_estragado.json` com as 4 diferenças
- [ ] PR para a `develop`, até **03/12**

### Erros comuns

- **`"id": "1"` com aspas no JSON**: a conversão com `int()` não está sendo aplicada, ou você grava a linha original no lugar da convertida.
- **`"palavras_chave": [""]`** (uma lista com um texto vazio): faltou o `if p.strip()` na *list comprehension*.
- **`TypeError: Object of type ... is not JSON serializable`**: você colocou no dicionário algo que o JSON não conhece (por exemplo, um conjunto `set`). Use lista.
- **O verificador acusa diferença em todas as linhas**: você está comparando com o texto do CSV sem converter (`"1"` com `1`), ou esqueceu o `.strip()`.
- **O verificador dá 0 diferenças até no JSON estragado**: ele está usando a mesma função do conversor, ou não está comparando de verdade. Confira com um `print` o esperado e o encontrado de uma coluna.
- **`JSONDecodeError`** ao rodar o verificador no estragado: a edição à mão quebrou o JSON (vírgula sobrando ou faltando). Corrija até sumir a marcação vermelha no VS Code.

---

<a id="sprint-3"></a>
# Sprint 3: 04/12 a 10/12 - Ajustes

**Branch:** `fix/conversor-ajustes`

Na sexta, 04/12, o Ítalo roda o seu conversor na planilha real dele, já corrigida pelo validador, e o seu verificador em cima do resultado. Se aparecer algum problema (uma diferença que o verificador apontou, um valor convertido errado, uma mensagem confusa), ele avisa você no grupo da equipe.

### Passo a passo

1. Acompanhe o grupo da equipe de sexta a terça. Se não houver nenhum pedido de ajuste até **terça, 08/12**, avise: `Nenhum ajuste pedido no conversor`.

2. Se houver pedido de ajuste:

   ```
   git checkout develop
   git pull
   git checkout -b fix/conversor-ajustes
   ```

   Corrija, acrescente na planilha `Teste do conversor` uma linha que reproduza o problema (assim ele não volta), baixe de novo o CSV por cima do `dados/teste_conversor.csv`, gere de novo o `dados/teste_conversor.json`, rode o verificador, faça o *commit* e abra o PR até **terça, 08/12**.

3. **Extra, só se sobrar tempo e não houver ajuste pendente:** teste em volume. O gerador do Gleidson tem uma constante `TAXA_ERRO` no começo do programa. Mude para `0` **sem fazer *commit***, gere 1.000 narrativas sem erros, converta e verifique:

   ```
   python scripts\gerar_fake.py 1000
   python scripts\converter.py dados\fake\fake_1000.csv dados\fake\fake_1000.json
   python scripts\verificar_json.py dados\fake\fake_1000.csv dados\fake\fake_1000.json
   git checkout scripts/gerar_fake.py
   ```

   O último comando desfaz a sua mudança no gerador. Mande ao Ítalo a saída dos dois programas: ela mostra que o conversor funciona com um acervo 50 vezes maior que o catálogo atual.

### Entrega da sprint

- [ ] Ajustes pedidos resolvidos, com PR, até **08/12**; ou aviso `Nenhum ajuste pedido no conversor` no grupo

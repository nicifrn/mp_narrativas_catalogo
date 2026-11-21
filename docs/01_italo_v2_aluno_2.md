# Plano de desenvolvimento - Aluno 2: gerador de narrativas fictícias

**Aluno:** Aluno 2 (@aluno2) - Técnico Integrado em Informática

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
- [Sprint 1 - Ambiente e gerador de narrativas corretas](#sprint-1)
- [Sprint 2 - Erros de propósito e gabarito](#sprint-2)
- [Sprint 3 - Ajustes](#sprint-3)

---

<a id="ideia"></a>
## 1. O que você vai fazer

O Ítalo está montando uma planilha com 20 narrativas populares reais do Rio Grande do Norte para o acervo da plataforma Narrativas, do IFRN. O Aluno 1 está programando um **validador**, que confere a planilha e aponta os erros.

Para saber se o validador funciona de verdade, é preciso testá-lo com **muitas** planilhas, e com erros que a gente **já sabe onde estão**. Com 20 narrativas reais isso não dá. **É aí que entra você.**

**Você vai programar o gerador:** um programa em Python que cria planilhas (em CSV) com quantas narrativas **fictícias** a gente pedir (100, 1.000...), no mesmo formato da planilha real. Em cerca de 10% das linhas, ele coloca **um erro de propósito** e anota cada erro em um segundo arquivo, o **gabarito**. Depois, o Ítalo roda o validador na sua planilha e compara o que o validador encontrou com o seu gabarito.

Você roda assim:

```
python scripts\gerar_fake.py 100
```

E ele responde mais ou menos assim:

```
Narrativas geradas: 100
Erros inseridos: 9
Planilha: dados\fake\fake_100.csv
Gabarito: dados\fake\fake_100_gabarito.csv
```

**O que você só usa:** Python e os módulos `random`, `csv`, `sys` e `os`, que já vêm com ele. Você **não instala nada**.

**O que fica de fora:** gerar texto realista, usar a biblioteca Faker ou qualquer outra biblioteca externa. Os textos podem ser bem simples, como `"Trecho fictício 1 da narrativa 7."`. O que importa é o **formato** estar certo e os **erros** estarem anotados.

**Você não depende de ninguém para começar.** O formato está fechado na [seção 2](#formato).

### Quem faz o quê na equipe

| Quem | Faz | Arquivos |
|---|---|---|
| Ítalo | Planilha com narrativas reais, conversor para JSON, estatísticas, integração e o RCC | os do plano dele |
| Aluno 1 | Validador | `scripts/validar.py` e `dados/teste_validador.csv` |
| **Você (Aluno 2)** | **Gerador de narrativas fictícias** | **`scripts/gerar_fake.py`** |

**Mexa só no seu arquivo.** Assim ninguém atrapalha ninguém no Git. Se precisar de outra coisa no repositório, peça ao Ítalo.

---

<a id="formato"></a>
## 2. O formato da planilha

Este formato é o **contrato** da equipe: você, o Ítalo e o Aluno 1 usam exatamente estes nomes, nesta ordem. Ele não muda. O Ítalo publica a explicação detalhada de cada coluna em `docs/formato_planilha.md` até 24/11, mas você já pode começar com a tabela abaixo.

### 2.1 As colunas

| # | Coluna | Obrigatória | Tipo | Regra |
|---|---|---|---|---|
| 1 | `id` | sim | número inteiro | 1, 2, 3..., sem repetir |
| 2 | `titulo` | sim | texto | |
| 3 | `tipo` | sim | lista | `lenda`, `conto`, `causo`, `mito`, `cordel` |
| 4 | `publico` | sim | lista | `infantil`, `juvenil`, `adulto`, `livre` |
| 5 | `municipio` | sim | texto | nome de um município do RN |
| 6 | `mesorregiao` | sim | lista | `oeste`, `central`, `agreste`, `leste` |
| 7 | `texto` | sim | texto | de 2 a 3 trechos, cada um entre aspas, separados por ` \| ` |
| 8 | `palavras_chave` | não | texto | separadas por ponto e vírgula: `lobisomem; sertão` |
| 9 | `fonte` | sim | texto | |
| 10 | `url_fonte` | não | texto | |
| 11 | `ano_fonte` | não | número inteiro | entre 1500 e 2026 |
| 12 | `licenca` | sim | lista | `dominio_publico`, `cc_by`, `cc_by_sa`, `direitos_reservados`, `desconhecida` |

### 2.2 Regras do arquivo

- CSV, codificação UTF-8, separado por vírgula.
- A primeira linha é o cabeçalho, com os 12 nomes acima, nesta ordem.
- **Numeração das linhas:** o cabeçalho é a **linha 1**; a primeira narrativa é a **linha 2**. Como o `id` começa em 1, **a narrativa de `id` N está na linha N + 1**. Isso é importante para o gabarito.
- Coluna opcional sem valor fica vazia.
- **A coluna `texto`** tem de 2 a 3 trechos curtos, separados por ` | ` (barra vertical com um espaço de cada lado). Cada trecho começa e termina com aspas retas (`"`). Exemplo: `"Trecho fictício 1 da narrativa 7." | "Trecho fictício 2 da narrativa 7."`

### 2.3 Os erros que o gerador insere

O seu gerador insere **quatro tipos** de erro, sempre **um erro só por linha**:

| Código | O que o gerador faz | Em quais colunas |
|---|---|---|
| `vazio` | apaga o valor de uma coluna obrigatória | sorteia uma entre `titulo`, `tipo`, `publico`, `municipio`, `mesorregiao`, `texto`, `fonte`, `licenca` (o `id` fica de fora) |
| `nao_inteiro` | coloca um texto que não é número no ano | `ano_fonte` |
| `fora_da_lista` | coloca um valor que não está na lista | sorteia uma entre `tipo`, `publico`, `mesorregiao`, `licenca` |
| `sem_aspas` | tira as aspas dos trechos | `texto` |

**O gabarito** é um CSV com este formato, uma linha por erro inserido:

```
linha,coluna,erro
5,titulo,vazio
9,ano_fonte,nao_inteiro
12,tipo,fora_da_lista
```

Os códigos são exatamente os da tabela: minúsculas, sem acento, com `_`. O validador do Aluno 1 grava o relatório dele no mesmo formato, e o Ítalo compara os dois arquivos. **Se você escrever `Vazio` ou `campo vazio`, a comparação falha.**

---

<a id="cronograma"></a>
## 3. Cronograma

| Sprint | Período | O que você faz | *Issue* |
|---|---|---|---|
| 1 | 23/11 a 26/11 | Ambiente, Git, estudo dos módulos `random` e `csv`, gerador de narrativas **corretas** | #10 |
| 2 | 27/11 a 03/12 | Quantidade pelo comando, semente, erros de propósito e gabarito. **Entrega: 03/12** | #11 |
| 3 | 04/12 a 10/12 | Ajustes que o Ítalo ou eu pedirmos depois da integração | #12 |

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
| 1 | `feature/gerador-base` | #10 |
| 2 | `feature/gerador-erros` | #11 |
| 3 | `fix/gerador-ajustes` | #12 |

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
git add scripts/gerar_fake.py
git commit -m "feat: gera narrativas com colunas sorteadas"
git push
```

Repare que o `git add` leva **só o seu arquivo**. As planilhas que o gerador cria (`dados/fake/`) **nunca** vão para o Git: elas podem ter milhares de linhas, e qualquer pessoa gera de novo com um comando.

Na primeira vez que der `git push` em uma *branch* nova, o Git responde com um erro e mostra o comando certo, algo como `git push --set-upstream origin feature/gerador-base`. Copie e rode exatamente o comando que ele mostrar.

### 4.3 Mensagens de *commit*

Em português, curtas, com o verbo no presente e um prefixo:

| Prefixo | Quando | Exemplo |
|---|---|---|
| `feat:` | algo novo funcionando | `feat: insere erros de propósito e grava gabarito` |
| `fix:` | correção | `fix: corrige número da linha no gabarito` |
| `refactor:` | reorganizar sem mudar o que faz | `refactor: separa a geração de uma narrativa em função` |

**Proibido:** `ajustes`, `mudanças`, `update`, `correções`. Faça pelo menos **2 *commits* por semana**.

### 4.4 O *pull request* (PR)

1. `git status` deve dizer `nothing to commit, working tree clean` (os arquivos de `dados/fake/` podem aparecer como *untracked*; tudo bem, eles não vão).
2. No GitHub, abra o repositório. Clique em **Compare & pull request** na faixa amarela. Se não aparecer: aba **Pull requests → New pull request**, com **base: `develop`** e **compare: a sua *branch***.
3. Preencha o modelo: **Objetivo**, **O que foi feito**, **Como testar** (o comando, a saída do terminal e as primeiras linhas do arquivo gerado) e, em **Issue**, `Closes #N` com o número da sua *issue*.
4. Em **Reviewers**, marque `brunogomesifrn` e `italogomees`.
5. Na *issue*, comente: `@brunogomesifrn @italogomees PR #X pronto para revisão`.

**Você não faz o *merge*.** Se pedirmos ajustes, faça na mesma *branch*: o PR se atualiza sozinho.

### 4.5 Quando travar

**Travou mais de 40 minutos no mesmo erro? Pare e peça ajuda.** Comente na sua *issue*, me marcando, com: o que você estava tentando fazer, o comando que rodou e **a mensagem de erro inteira, copiada e colada**.

---

<a id="sprint-1"></a>
# Sprint 1: 23/11 a 26/11 - Ambiente e gerador de narrativas corretas

**Branch:** `feature/gerador-base` · **Issue:** #10 · **PR até:** quinta, 26/11

**O que você vai entregar:** um gerador que cria `dados/fake/fake_20.csv` com 20 narrativas fictícias **sem nenhum erro**, no formato da [seção 2](#formato).

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
   git checkout -b feature/gerador-base
   ```

   O `python --version` deve mostrar `Python 3.` alguma coisa. O `git branch` deve mostrar `* develop`.

5. Crie a pasta `scripts`, se ainda não existir (no explorador do VS Code, à esquerda: botão direito → **New Folder**).

**Segunda e terça, 23 e 24/11: estudar**

6. Leia e teste os exemplos destas páginas, **digitando** os códigos (não copie e cole: digitando você aprende):
   - O módulo `random`, principalmente `random.choice`, `random.random`, `random.randint`, `random.sample` e `random.seed`: https://docs.python.org/pt-br/3/library/random.html
   - O módulo `csv`, principalmente o `csv.DictWriter`: https://docs.python.org/pt-br/3/library/csv.html
   - Dicionários: https://docs.python.org/pt-br/3/tutorial/datastructures.html#dictionaries
   - *f-strings* (textos com variáveis dentro): https://docs.python.org/pt-br/3/tutorial/inputoutput.html#formatted-string-literals

   Se preferir vídeo, procure no YouTube por "python random choice" e "python csv DictWriter".

7. Experimente o `random` no terminal. Digite `python` e, dentro dele:

   ```python
   import random
   random.choice(["lenda", "conto", "causo"])   # rode várias vezes: muda a cada vez
   random.randint(1900, 2026)                    # um número inteiro entre os dois, incluindo os dois
   random.random()                               # um número entre 0 e 1
   random.sample(["a", "b", "c", "d"], 2)        # 2 itens diferentes da lista
   ```

   Agora experimente a **semente**:

   ```python
   random.seed(42)
   random.randint(1, 100)
   random.randint(1, 100)
   random.seed(42)
   random.randint(1, 100)
   random.randint(1, 100)
   ```

   Os dois números depois de cada `seed(42)` são **iguais**. Com a semente fixa, o "sorteio" sai sempre igual, e isso permite que o Ítalo gere exatamente a mesma planilha quando precisar. Para sair do Python: `exit()`.

**Quarta e quinta, 25 e 26/11: o gerador de narrativas corretas**

8. Crie `scripts/gerar_fake.py`. Comece pelo **material do sorteio**, em constantes no começo do programa:

   ```python
   COLUNAS = ["id", "titulo", "tipo", "publico", "municipio", "mesorregiao",
              "texto", "palavras_chave", "fonte", "url_fonte", "ano_fonte", "licenca"]

   TIPOS = ["lenda", "conto", "causo", "mito", "cordel"]
   PUBLICOS = [...]
   LICENCAS = [...]

   # município -> mesorregião
   MUNICIPIOS = {
       "Natal": "leste",
       "Parnamirim": "leste",
       "Ceará-Mirim": "leste",
       "Mossoró": "oeste",
       "Pau dos Ferros": "oeste",
       "Apodi": "oeste",
       "Caicó": "central",
       "Currais Novos": "central",
       "Macau": "central",
       "Santa Cruz": "agreste",
       "Nova Cruz": "agreste",
   }

   SERES = ["do Lobisomem", "da Mula sem Cabeça", "do Boi Tatá", "da Cobra Grande",
            "do Vaqueiro Encantado", "da Moça da Pedra"]

   PALAVRAS = ["sertão", "assombração", "lua cheia", "vaqueiro", "rio", "encantamento"]
   ```

   Complete as listas que ficaram com `...` usando a tabela da [seção 2](#formato). Acrescente mais 4 municípios ao dicionário: para saber a mesorregião de cada um, abra https://servicodados.ibge.gov.br/api/v1/localidades/estados/RN/municipios, use `Ctrl + F` para achar o município e veja o `"nome"` dentro de `"mesorregiao"` (Oeste Potiguar é `oeste`, Central Potiguar é `central`, e assim por diante). Confira também os 11 que já estão na lista.

9. **Uma função que gera uma narrativa.** Ela recebe o número da narrativa e devolve um dicionário com as 12 colunas. Esqueleto (os comentários dizem o que fazer; o código é seu):

   ```python
   def gerar_narrativa(numero):
       tipo = random.choice(TIPOS)
       municipio = random.choice(list(MUNICIPIOS.keys()))

       return {
           "id": numero,
           "titulo": ...,          # ex.: "A lenda do Boi Tatá de Caicó" (use o tipo, um SER e o município)
           "tipo": tipo,
           "publico": ...,
           "municipio": municipio,
           "mesorregiao": ...,     # pegue no dicionário MUNICIPIOS, para combinar com o município
           "texto": ...,           # de 2 a 3 trechos fictícios, cada um entre aspas, juntos com " | "
           "palavras_chave": ..., # de 1 a 3 PALAVRAS, juntas com "; "  (pesquise "python join")
           "fonte": f"Fonte fictícia número {numero}.",
           "url_fonte": ...,       # metade das vezes vazio "", metade f"https://exemplo.com/narrativa/{numero}"
           "ano_fonte": ...,       # um inteiro entre 1900 e 2026, ou vazio "" de vez em quando
           "licenca": ...,
       }
   ```

   Dicas para as partes com `...`:
   - **"metade das vezes":** `if random.random() < 0.5:`;
   - **juntar palavras:** `"; ".join(["sertão", "rio"])` dá `"sertão; rio"`;
   - **quantidade sorteada de palavras:** `random.sample(PALAVRAS, random.randint(1, 3))`;
   - **um trecho com aspas dentro do texto:** como o trecho precisa das aspas duplas (`"`), escreva a *f-string* com aspas **simples** por fora: `f'"Trecho fictício {i} da narrativa {numero}."'`. Teste no terminal do Python com `i = 1` e `numero = 7`: o resultado é `"Trecho fictício 1 da narrativa 7."`, com as aspas fazendo parte do texto;
   - **o `texto` inteiro:** sorteie quantos trechos (`random.randint(2, 3)`), monte uma lista com um trecho para cada `i` de 1 até essa quantidade e junte com `" | ".join(...)`, do mesmo jeito das palavras-chave.

   Cuidado com os valores: **tudo o que o gerador produz nesta sprint tem de estar certo** pelas regras da [seção 2](#formato). Ano entre 1500 e 2026; valores de lista exatamente como na tabela; município e mesorregião combinando.

10. **Gravar a planilha.** Monte uma lista com as narrativas e grave com o `csv.DictWriter`:

    ```python
    import csv
    import os

    os.makedirs("dados/fake", exist_ok=True)

    with open(caminho, "w", encoding="utf-8", newline="") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=COLUNAS)
        escritor.writeheader()
        for narrativa in narrativas:
            escritor.writerow(narrativa)
    ```

    O `newline=""` é obrigatório no Windows: sem ele, o arquivo sai com uma linha em branco entre cada linha. O `os.makedirs` cria a pasta `dados/fake` se ela não existir.

    Nesta sprint, a quantidade fica fixa no código: `QUANTIDADE = 20`, e o arquivo é `dados/fake/fake_20.csv`.

11. Rode:

    ```
    python scripts\gerar_fake.py
    ```

    Abra o `dados\fake\fake_20.csv` no VS Code e confira:
    - a primeira linha é o cabeçalho, com as 12 colunas na ordem;
    - são 21 linhas (cabeçalho + 20);
    - os acentos aparecem certos (`Caicó`, `sertão`);
    - os títulos com vírgula, se houver, estão entre aspas (o `csv` faz sozinho);
    - a coluna `texto` aparece com as aspas **dobradas**, assim: `"""Trecho fictício 1 da narrativa 7."" | ""Trecho fictício 2 da narrativa 7."""`. É assim que o CSV guarda um valor que tem aspas dentro: está certo. O módulo `csv` desfaz isso sozinho quando alguém lê o arquivo;
    - os `id` vão de 1 a 20.

    > **Não abra o CSV no Excel.** O Excel do Windows estraga os acentos. Para ver como tabela, faça o upload no Google Planilhas (**Arquivo → Importar → Upload**).

12. Se o validador do Aluno 1 já estiver na `develop`, teste com ele (se ainda não estiver, pule): `python scripts\validar.py dados\fake\fake_20.csv`. Ele deve dizer **0 erros**. Se apontar algum, abra a linha indicada no `fake_20.csv` e compare o valor com as regras da [seção 2](#formato): se o valor estiver fora das regras, corrija o gerador; se estiver dentro das regras, comente na *issue* #8 do Aluno 1 com o número da linha, a coluna e o valor.

13. *Commit*, envio e PR com `Closes #10` até **quinta, 26/11**. Em **Como testar**, cole a saída do terminal e as 5 primeiras linhas do `fake_20.csv`.

### Como saber que deu certo

- `dados\fake\fake_20.csv` tem 21 linhas, cabeçalho certo e acentos certos.
- Rodando duas vezes, os arquivos saem **diferentes** (ainda não há semente; ela entra na Sprint 2).
- Nenhum valor fora das regras.

### Entrega da sprint

- [ ] `scripts/gerar_fake.py` gerando 20 narrativas corretas em `dados/fake/fake_20.csv`
- [ ] Listas completas, com 15 municípios conferidos no IBGE
- [ ] PR para a `develop` com `Closes #10`, até **26/11**

### Erros comuns

- **`FileNotFoundError`**: você não está na raiz do repositório. Rode `pwd`; se estiver dentro de `scripts`, volte com `cd ..`.
- **`ValueError: dict contains fields not in fieldnames`**: alguma chave do dicionário da narrativa está escrita diferente de `COLUNAS` (por exemplo, `"título"` com acento).
- **Linha em branco entre as linhas do CSV:** faltou `newline=""`.
- **Acentos estranhos:** faltou `encoding="utf-8"`, ou o arquivo foi aberto no Excel.

---

<a id="sprint-2"></a>
# Sprint 2: 27/11 a 03/12 - Erros de propósito e gabarito

**Branch:** `feature/gerador-erros` · **Issue:** #11 · **PR até:** quinta, 03/12

**O que você vai entregar:** o gerador completo: recebe a quantidade no comando, usa semente fixa, insere erros em cerca de 10% das linhas e grava o gabarito.

### Passo a passo

1. Atualize a `develop` (o seu PR da Sprint 1 já deve ter sido integrado) e crie a *branch*:

   ```
   git checkout develop
   git pull
   git checkout -b feature/gerador-erros
   ```

2. **A quantidade vem do comando.** Troque o `QUANTIDADE = 20` pela lista `sys.argv` (https://docs.python.org/pt-br/3/library/sys.html#sys.argv). A posição 0 é o próprio programa; a posição 1 é o que vem depois dele:

   ```python
   import sys

   # python scripts\gerar_fake.py 100
   # sys.argv[0] -> "scripts\gerar_fake.py"
   # sys.argv[1] -> "100"   (é texto! converta com int)

   if len(sys.argv) != 2:
       print("Uso: python scripts\\gerar_fake.py QUANTIDADE")
       sys.exit(1)
   ```

   Os nomes dos arquivos passam a depender da quantidade: `dados/fake/fake_100.csv` e `dados/fake/fake_100_gabarito.csv`. Monte com *f-string*.

3. **Semente e taxa de erro**, em constantes no começo do programa:

   ```python
   SEMENTE = 42
   TAXA_ERRO = 0.1   # 10% das linhas recebem um erro
   ```

   Chame `random.seed(SEMENTE)` **uma vez**, no começo da execução, antes de gerar a primeira narrativa. Rode duas vezes com a mesma quantidade e confira que os arquivos saem **iguais** (no VS Code: selecione os dois arquivos no explorador com `Ctrl + clique`, botão direito → **Compare Selected**).

   O Ítalo vai mudar a `TAXA_ERRO` para `0` em um teste dele: com `0`, o gerador tem de gerar a planilha **sem nenhum erro** e o gabarito só com o cabeçalho. Deixe o programa funcionando para qualquer valor entre 0 e 1.

4. **Os valores errados**, também em constantes:

   ```python
   OBRIGATORIAS_PARA_APAGAR = ["titulo", "tipo", "publico", "municipio",
                               "mesorregiao", "texto", "fonte", "licenca"]

   COLUNAS_DE_LISTA = ["tipo", "publico", "mesorregiao", "licenca"]

   ANOS_INVALIDOS = ["mil novecentos", "19 50", "1950a", "s/d"]

   VALORES_FORA_DA_LISTA = ["historia", "fabula", "outro", "todos"]
   ```

   Confira que **nenhum** dos `VALORES_FORA_DA_LISTA` existe em alguma lista do formato. Se existir, o erro não é erro, e o gabarito fica errado.

5. **Uma função que estraga uma narrativa.** Ela recebe a narrativa (o dicionário) e devolve qual coluna estragou e qual o código do erro:

   ```python
   def inserir_erro(narrativa):
       tipo_erro = random.choice(["vazio", "nao_inteiro", "fora_da_lista", "sem_aspas"])

       if tipo_erro == "vazio":
           coluna = random.choice(OBRIGATORIAS_PARA_APAGAR)
           narrativa[coluna] = ""
       elif tipo_erro == "nao_inteiro":
           ...
       elif tipo_erro == "fora_da_lista":
           ...
       else:
           # sem_aspas: tire todas as aspas do texto (pesquise o método replace)
           ...

       return coluna, tipo_erro
   ```

   Para o `sem_aspas`, o método `replace` resolve em uma linha: `'"Um." | "Dois."'.replace('"', "")` dá `Um. | Dois.`. Teste no terminal do Python. Os dois trechos ficam sem aspas, e o validador registra **um** erro para a coluna `texto`, que é exatamente o que vai no gabarito.

   O dicionário é alterado "por dentro" da função: quando ela termina, a narrativa que estava na lista já está estragada. Pesquise "python dicionário mutável função" se isso parecer estranho.

6. **O laço principal.** Para cada narrativa: gere; sorteie se ela vai receber erro (`random.random() < TAXA_ERRO`); se sim, estrague e anote no gabarito:

   ```python
   narrativas = []
   gabarito = []

   for numero in range(1, quantidade + 1):
       narrativa = gerar_narrativa(numero)
       if random.random() < TAXA_ERRO:
           coluna, erro = inserir_erro(narrativa)
           linha = ...   # a narrativa de id N está na linha N + 1 (seção 2.2)
           gabarito.append((linha, coluna, erro))
       narrativas.append(narrativa)
   ```

   **Atenção à linha:** o número da linha no gabarito é o número da linha **na planilha**, contando o cabeçalho como linha 1. A narrativa 1 está na linha 2. Se você gravar o `id` no lugar da linha, todos os erros do gabarito ficam "uma linha acima" e a comparação do Ítalo dá zero acertos.

7. **Gravar o gabarito.** Igual à planilha, mas com o `csv.writer` (lista, não dicionário) e o cabeçalho `linha,coluna,erro`:

   ```python
   with open(caminho_gabarito, "w", encoding="utf-8", newline="") as arquivo:
       escritor = csv.writer(arquivo)
       escritor.writerow(["linha", "coluna", "erro"])
       for item in gabarito:
           escritor.writerow(item)
   ```

8. **A mensagem final.** Mostre quantas narrativas foram geradas, quantos erros foram inseridos e os nomes dos dois arquivos (veja o exemplo da [seção 1](#ideia)).

9. Organize o programa em funções. Uma sugestão:

   ```python
   def gerar_narrativa(numero): ...        # Sprint 1
   def inserir_erro(narrativa): ...        # passo 5
   def gravar_planilha(narrativas, caminho): ...
   def gravar_gabarito(gabarito, caminho): ...

   # aqui: conferir sys.argv, random.seed, laço principal, gravar os dois arquivos, mensagem final
   ```

10. **Teste à mão.** Gere 20 narrativas:

    ```
    python scripts\gerar_fake.py 20
    ```

    Abra `dados\fake\fake_20_gabarito.csv`. Para **cada** erro do gabarito, vá até a linha indicada no `fake_20.csv` (no VS Code, `Ctrl + G` e o número da linha) e confira que o erro está lá, na coluna indicada. Confira também que as linhas **fora** do gabarito estão certas. Com 20 narrativas e 10%, devem sair uns 2 erros: se sair 0, mude a `SEMENTE` só para este teste, ou teste com 50.

11. **Teste em volume.** Gere 100 e 1.000:

    ```
    python scripts\gerar_fake.py 100
    python scripts\gerar_fake.py 1000
    ```

    Na base de 1.000, o número de erros deve ficar **perto de 100** (10%). Não precisa ser exatamente 100: é sorteio. Se der muito longe (30 ou 300), há algo errado na conta.

12. **Se o validador do Aluno 1 já estiver na `develop`**, teste com ele (se ainda não estiver, pule):

    ```
    git checkout develop
    git pull
    git checkout feature/gerador-erros
    git merge develop
    python scripts\gerar_fake.py 100
    python scripts\validar.py dados\fake\fake_100.csv
    ```

    Abra o seu gabarito e o relatório do validador (`resultados\erros_fake_100.csv`) lado a lado (botão direito na aba → **Split Right**). Devem ser iguais. Se não forem, abra a linha da diferença no `fake_100.csv` e compare o valor com as regras da [seção 2](#formato): se o valor gerado estiver fora das regras e não estiver no gabarito, o erro é do gerador, e você corrige; se o gabarito estiver certo e o validador não encontrou o erro (ou encontrou um que não existe), comente na *issue* #8 do Aluno 1 com o número da linha, a coluna e o valor.

13. *Commit* a cada parte que funcionar (`feat: recebe a quantidade pelo comando`, `feat: insere erros de propósito e grava gabarito`...), envio e PR com `Closes #11` até **quinta, 03/12**. Em **Como testar**, cole a saída do terminal para 100 e 1.000 narrativas e o resultado da conferência à mão do passo 10.

### Como saber que deu certo

- `python scripts\gerar_fake.py 100` cria os dois arquivos e mostra o resumo.
- Rodando duas vezes com a mesma quantidade, os arquivos saem iguais.
- Todo erro do gabarito está na linha e na coluna indicadas, e nenhuma outra linha tem erro.
- Com `TAXA_ERRO = 0`, o gabarito sai só com o cabeçalho.

### Entrega da sprint

- [ ] Quantidade recebida pelo comando, com mensagem de uso
- [ ] `SEMENTE` e `TAXA_ERRO` em constantes, com o resultado repetível
- [ ] Os 4 tipos de erro: `vazio`, `nao_inteiro`, `fora_da_lista`, `sem_aspas`
- [ ] Gabarito em `dados/fake/fake_<N>_gabarito.csv`, com a numeração de linhas certa
- [ ] Conferência à mão do gabarito com 20 narrativas
- [ ] PR para a `develop` com `Closes #11`, até **03/12**

### Erros comuns

- **Todos os erros do gabarito "uma linha acima":** você gravou o `id` no lugar da linha. A linha é `id + 1`.
- **O gabarito tem erros que não aparecem na planilha:** você estragou uma **cópia** da narrativa, ou gravou a planilha **antes** de estragar.
- **`ValueError: invalid literal for int()`**: o `sys.argv[1]` não é número (por exemplo, `python scripts\gerar_fake.py cem`). Pode deixar o erro acontecer, ou trate com `try` e mostre a mensagem de uso.
- **Os arquivos saem diferentes a cada execução:** o `random.seed` não está sendo chamado, ou está sendo chamado depois do primeiro sorteio.

---

<a id="sprint-3"></a>
# Sprint 3: 04/12 a 10/12 - Ajustes

**Branch:** `fix/gerador-ajustes` · **Issue:** #12

Na sexta, 04/12, o Ítalo roda o seu gerador e o validador do Aluno 1 e compara o gabarito com o relatório. Se aparecer algum problema (linha errada no gabarito, valor "errado" que na verdade está certo, valor "certo" que na verdade está errado), ele comenta na sua *issue* #12.

### Passo a passo

1. Acompanhe a *issue* #12 de sexta a terça. Se não houver nenhum pedido de ajuste até **terça, 08/12**, comente na *issue*: `Nenhum ajuste pedido` e eu fecho.

2. Se houver pedido de ajuste:

   ```
   git checkout develop
   git pull
   git checkout -b fix/gerador-ajustes
   ```

   Corrija, gere de novo, confira à mão como na Sprint 2 (passo 10), faça o *commit* e abra o PR com `Closes #12` até **terça, 08/12**.

### Entrega da sprint

- [ ] Ajustes pedidos na *issue* #12 resolvidos, com PR e `Closes #12`, até **08/12**; ou comentário `Nenhum ajuste pedido`

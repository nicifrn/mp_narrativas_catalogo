# Plano de desenvolvimento - Catálogo estruturado de narrativas do RN

**Aluno:** Ítalo (@italogomees) - Técnico Integrado em Informática

**Orientador:** Prof. Bruno Gomes (@brunogomesifrn) - NIC/IFRN

**Colaboradores no desenvolvimento:** Samuel (@samuelmarinho10), responsável pelo conversor para JSON e pelo verificador do JSON, e Gleidson (@gleidsonxsz), responsável pelo gerador de narrativas fictícias.

**Repositório:** https://github.com/nicifrn/mp_narrativas_catalogo

**Período:** 23/11/2026 a 10/12/2026, em 3 sprints

**Plano de escrita correspondente:** [`docs/01_italo_v2_narrativas_escrita.md`](01_italo_v2_narrativas_escrita.md)

**Projeto pai:** Narrativas, plataforma digital para registro, organização e difusão das narrativas populares do Rio Grande do Norte (resumo em [`docs/projeto_narrativas.md`](projeto_narrativas.md)).

> **Leia este documento inteiro na segunda-feira, 23/11, antes de começar.** Ele diz tudo o que você vai programar, sprint por sprint. **Não há *issues* no GitHub: este documento é o seu roteiro.** Siga as sprints na ordem e marque as caixas da "Entrega da sprint" à medida que for terminando.

---

## Sumário

- [1. A ideia do trabalho](#ideia)
- [2. Quem faz o quê](#equipe)
- [3. Decisões já tomadas](#decisoes)
- [4. O formato da planilha (o contrato da equipe)](#formato)
- [5. Cronograma](#cronograma)
- [6. Como trabalhar no repositório](#fluxo-git)
- [7. A estrutura de pastas](#estrutura)
- [Sprint 1 - Formato da planilha e estrutura do repositório](#sprint-1)
- [Sprint 2 - Catálogo, validador e estatísticas](#sprint-2)
- [Sprint 3 - Integração e fechamento](#sprint-3)
- [8. Riscos e planos B](#riscos)

---

<a id="ideia"></a>
## 1. A ideia do trabalho

A plataforma Narrativas foi pensada para guardar centenas de narrativas populares do RN, mas **o acervo ainda está vazio**: o cadastro de narrativas nem existe no sistema. Todos os outros trabalhos do projeto (PDF, áudio, busca) precisaram inventar a sua própria base de teste, cada um de um jeito.

O seu trabalho resolve isso. Você vai construir o **primeiro conjunto de dados estruturado** do projeto: um catálogo de **20 narrativas populares reais do RN**, cada uma com título, tipo, público, município, mesorregião, de 2 a 3 trechos curtos citados da fonte original, fonte e licença, organizado em uma planilha com formato definido por você, conferido por um validador automático e convertido para **JSON**, que é o formato que a equipe vai usar para carregar o banco da plataforma.

A pergunta que o trabalho responde é:

> **Como organizar e validar um conjunto de dados de narrativas populares do RN para que ele sirva de base confiável ao acervo digital do projeto Narrativas?**

O RCC é um **relato do que você fez no projeto**. Nos Resultados, você mostra o que foi produzido, com números simples:

| O que você relata | De onde vem |
|---|---|
| O formato da planilha | `docs/formato_planilha.md` (você) |
| Quantas narrativas, de quantos municípios, e como ficaram por tipo e por mesorregião | `estatisticas.py` (você) |
| Quantos erros a planilha real tinha antes da correção, e quais | `validar.py` (você) rodado na sua planilha |
| Se o validador encontrou os erros inseridos de propósito nas bases fictícias | `gerar_fake.py` (Gleidson) + `validar.py` (você) |
| O catálogo em JSON, conferido | `converter.py` e `verificar_json.py` (Samuel) |

Guarde esta frase, porque ela vale para o código e para o texto:

> O seu trabalho **não é** "fiz uma planilha de narrativas". O seu trabalho é **"defini o formato, construí e validei o primeiro conjunto de dados do acervo do projeto Narrativas"**.

---

<a id="equipe"></a>
## 2. Quem faz o quê

| Quem | Faz | Arquivos que só ele mexe |
|---|---|---|
| **Ítalo** | Define o formato, monta a planilha com narrativas reais, programa o validador e as estatísticas, integra o trabalho dos colegas e escreve o RCC | `docs/formato_planilha.md`, `dados/modelo.csv`, `dados/narrativas.csv`, `dados/narrativas.json`, `dados/teste_validador.csv`, `scripts/validar.py`, `scripts/estatisticas.py`, `README.md`, `.gitignore`, `requirements.txt` |
| **Samuel** | Programa o conversor de CSV para JSON e o verificador, que confere se o JSON saiu igual ao CSV | `scripts/converter.py`, `scripts/verificar_json.py`, `dados/teste_conversor.csv`, `dados/teste_conversor.json`, `dados/teste_conversor_estragado.json` |
| **Gleidson** | Programa o gerador de narrativas fictícias | `scripts/gerar_fake.py` |

**Cada um mexe só nos seus arquivos.** Assim ninguém atrapalha ninguém e não há conflito no Git.

**Você não depende dos colegas.** O formato já está fechado na [seção 4](#formato), então os três começam no mesmo dia. Se o conversor ou o gerador atrasarem, o seu trabalho continua (veja a [seção 8](#riscos)).

Os planos dos colegas estão em [`docs/01_italo_v2_aluno_1.md`](01_italo_v2_aluno_1.md) e [`docs/01_italo_v2_aluno_2.md`](01_italo_v2_aluno_2.md). **Leia os dois** na Sprint 1: você vai integrar o que eles fizerem, então precisa saber o que cada programa recebe e o que devolve.

---

<a id="decisoes"></a>
## 3. Decisões já tomadas

| Item | Decisão |
|---|---|
| Linguagem | **Python 3** |
| Editor | **VS Code** |
| Planilha | **Google Planilhas**, baixada como CSV para o repositório |
| Leitura e escrita de CSV | módulo `csv`, que já vem com o Python |
| JSON | módulo `json`, que já vem com o Python |
| Contagens | `collections.Counter`, que já vem com o Python |
| Gráficos | `matplotlib`, instalada com `pip` (a única biblioteca que você instala) |
| Tamanho do catálogo | **20 narrativas reais**. Se sobrar tempo, até 30 |
| Conteúdo de cada narrativa | **de 2 a 3 trechos curtos copiados da fonte original, entre aspas**. Nada de resumo nem de texto completo |
| O que **não** entra | Django, banco de dados, interface web, `pandas`, texto completo das narrativas. Tudo isso vira "trabalho futuro" no RCC |

### Por que trechos curtos e não o texto completo?

Muitas das melhores fontes sobre narrativas do RN (por exemplo, as obras de Luís da Câmara Cascudo) **ainda não estão em domínio público**. Copiar o texto inteiro delas para um repositório seria violar direito autoral, **mesmo indicando a fonte**: indicar a fonte não autoriza a reprodução da obra.

O que a lei permite é **citar trechos**. A Lei de Direitos Autorais (Lei nº 9.610/1998), no **art. 46, inciso III**, diz que não constitui ofensa aos direitos autorais a citação, em qualquer meio de comunicação, de passagens de qualquer obra, para fins de estudo, crítica ou polêmica, na medida justificada para o fim a atingir, indicando-se o nome do autor e a origem da obra. Por isso, o catálogo guarda **de 2 a 3 trechos curtos de cada narrativa, copiados exatamente como estão na fonte, entre aspas**, junto com a **referência completa da fonte**.

O **art. 41** da mesma lei diz quando uma obra entra em domínio público: 70 anos contados de 1º de janeiro do ano seguinte ao da morte do autor. As obras em domínio público poderão ter o texto completo incluído no futuro, e a coluna `texto` foi pensada para isso: hoje ela guarda os trechos; depois, poderá guardar a narrativa inteira quando os direitos permitirem.

**Você vai citar a lei no RCC** (Referencial e Metodologia) para justificar essa escolha. O plano de escrita diz onde.

Leia a lei na fonte oficial, os dois artigos inteiros: http://www.planalto.gov.br/ccivil_03/leis/l9610.htm

---

<a id="formato"></a>
## 4. O formato da planilha (o contrato da equipe)

Este é o formato que os três vão usar. Você preenche e valida este formato, o conversor do Samuel lê este formato e o gerador do Gleidson escreve neste formato. **Os nomes das colunas, a ordem e as listas de valores não mudam depois de 24/11.** Se você mudar uma coluna, os dois colegas refazem o trabalho.

O que você pode fazer na Sprint 1 é **documentar** este formato (explicar e justificar cada coluna) e **acrescentar colunas opcionais no fim**, se achar necessário depois de olhar o protótipo da plataforma.

### 4.1 As colunas

| # | Coluna | Obrigatória | Tipo | Regra |
|---|---|---|---|---|
| 1 | `id` | sim | número inteiro | 1, 2, 3..., sem repetir |
| 2 | `titulo` | sim | texto | o título da narrativa |
| 3 | `tipo` | sim | lista | `lenda`, `conto`, `causo`, `mito`, `cordel` |
| 4 | `publico` | sim | lista | `infantil`, `juvenil`, `adulto`, `livre` |
| 5 | `municipio` | sim | texto | nome do município do RN, escrito como no IBGE (com acento) |
| 6 | `mesorregiao` | sim | lista | `oeste`, `central`, `agreste`, `leste` |
| 7 | `texto` | sim | texto | de 2 a 3 trechos curtos copiados da fonte original, **cada um entre aspas**, separados por ` \| ` (barra vertical com um espaço de cada lado) |
| 8 | `palavras_chave` | não | texto | separadas por ponto e vírgula: `lobisomem; sertão; lua cheia` |
| 9 | `fonte` | sim | texto | a referência da fonte, no formato da ABNT |
| 10 | `url_fonte` | não | texto | o endereço da fonte, se ela estiver na internet |
| 11 | `ano_fonte` | não | número inteiro | ano de publicação da fonte, entre 1500 e 2026 |
| 12 | `licenca` | sim | lista | `dominio_publico`, `cc_by`, `cc_by_sa`, `direitos_reservados`, `desconhecida` |

### 4.2 Regras comuns

- O arquivo é **CSV**, codificação **UTF-8**, separado por **vírgula**.
- A **primeira linha é o cabeçalho**, com os nomes das colunas exatamente como na tabela (minúsculas, sem acento), nesta ordem.
- **Numeração das linhas:** o cabeçalho é a linha 1 e a primeira narrativa é a **linha 2**, igual ao que aparece no Google Planilhas. Validador e gerador usam essa mesma numeração.
- Os valores das colunas do tipo **lista** são escritos **exatamente** como na tabela: minúsculas, sem acento, com `_` no lugar do espaço.
- Coluna opcional sem informação fica **vazia** (nada entre as vírgulas). Não escreva `-`, `N/A` nem `sem informação`.
- **A coluna `texto`:**
  - cada trecho começa com aspas e termina com aspas. Valem as aspas retas (`"`) e as curvas (`“` para abrir e `”` para fechar);
  - os trechos são separados por ` | `. Um trecho não pode ter o caractere `|` dentro;
  - exemplo do que se digita na célula: `"Primeiro trecho copiado da fonte." | "Segundo trecho copiado da fonte."`
- Textos com vírgula ou com aspas (os trechos, a fonte) são guardados de um jeito especial no CSV: o valor inteiro fica entre aspas, e cada aspa de dentro aparece **dobrada** (`""`). O Google Planilhas e o módulo `csv` fazem isso sozinhos, na hora de gravar e na hora de ler; você não precisa se preocupar.

### 4.3 Os arquivos de erros (validador e gerador)

O seu validador grava os erros que encontrou, e o gerador do Gleidson grava os erros que inseriu de propósito (o **gabarito**). Os dois usam o **mesmo formato**, para que você possa comparar os dois na Sprint 3:

```
linha,coluna,erro
5,titulo,vazio
9,ano_fonte,nao_inteiro
12,tipo,fora_da_lista
```

| Código do erro | Quando acontece |
|---|---|
| `vazio` | coluna obrigatória sem valor |
| `nao_inteiro` | `id` ou `ano_fonte` que não é número inteiro |
| `fora_da_faixa` | `ano_fonte` menor que 1500 ou maior que 2026 |
| `fora_da_lista` | `tipo`, `publico`, `mesorregiao` ou `licenca` com valor que não está na lista |
| `repetido` | `id` que já apareceu em outra linha |

O gerador do Gleidson insere só três desses tipos: `vazio`, `nao_inteiro` e `fora_da_lista`.

A regra da coluna `texto` (de 2 a 3 trechos, entre aspas) **não** é conferida pelo validador: você confere à mão, ao preencher. Ela entra nas limitações do RCC.

---

<a id="cronograma"></a>
## 5. Cronograma

| Sprint | Período | Desenvolvimento | Escrita (ver o plano de escrita) |
|---|---|---|---|
| 1 | 23/11 a 26/11 | Formato documentado e estrutura do repositório (**PR até terça, 24/11**). Primeiras 10 narrativas na planilha | **Entrega 1:** Introdução e Objetivos (26/11) |
| 2 | 27/11 a 03/12 | 20 narrativas (até 01/12), `validar.py` e `estatisticas.py` (**PR até 03/12**) | **Entrega 2:** Referencial Teórico e Metodologia (03/12) |
| 3 | 04/12 a 10/12 | Integração com o conversor e o gerador, `resumo.md` e `README.md` (**PR até segunda, 07/12**) | **Entrega 3:** Resultados (08/12). **Entrega 4:** Conclusão, Resumo, Título e revisão (10/12) |

**Tudo termina em 10/12.**

**Datas que não podem escorregar:**

- **24/11 (terça):** o formato documentado entra no repositório. Os colegas precisam dele para conferir o que estão fazendo.
- **01/12 (terça):** as 20 narrativas estão na planilha. Sem elas não há catálogo para validar nem para descrever nos Resultados.
- **04/12 (sexta):** a integração é feita **neste dia**. Ela leva umas duas horas: é só rodar os programas na ordem certa e guardar as saídas.
- **07/12 (segunda):** o código está fechado. De terça a quinta, você só escreve.

---

<a id="fluxo-git"></a>
## 6. Como trabalhar no repositório

### 6.1 As *branches*

| *Branch* | Para que serve | Quem mexe |
|---|---|---|
| `main` | versão final, aprovada | só eu, no fim do trabalho |
| `develop` | onde o trabalho aprovado dos três vai se juntando. É a *branch* padrão | ninguém envia direto: só entra por PR aprovado |
| `feature/...` | uma por sprint, onde você trabalha | você |

As suas *branches* já têm nome:

| Sprint | *Branch* |
|---|---|
| 1 | `feature/formato-planilha` |
| 2 | `feature/catalogo-validador` |
| 3 | `feature/integracao` |

A escrita não tem *branch*: ela acontece no Google Drive (veja o plano de escrita).

### 6.2 O ciclo de cada sprint

**No começo da sprint**, crie a *branch* a partir da `develop` atualizada:

```
git checkout develop
git pull
git checkout -b feature/nome-da-branch
```

**Durante a semana**, envie o trabalho **no fim de cada dia**. O que fica só na máquina do laboratório não foi entregue, e a máquina pode ser formatada.

```
git status
git add .
git commit -m "feat: confere campos obrigatórios vazios"
git push
```

Na primeira vez que der `git push` em uma *branch* nova, o Git responde com um erro e mostra o comando certo, algo como `git push --set-upstream origin feature/formato-planilha`. Copie e rode exatamente o comando que ele mostrar.

**Antes do `git add .`, olhe sempre o `git status`.** Se aparecer `.venv/`, `__pycache__/` ou `dados/fake/`, o seu `.gitignore` está errado: corrija antes de continuar.

### 6.3 Mensagens de *commit*

*Commits* pequenos e frequentes, com mensagem em português e verbo no presente:

| Prefixo | Quando usar | Exemplo |
|---|---|---|
| `feat:` | algo novo funcionando | `feat: adiciona gráfico por mesorregião` |
| `fix:` | correção | `fix: corrige leitura de palavras-chave vazias` |
| `docs:` | documentação, planilha, README | `docs: documenta o formato da planilha` |
| `refactor:` | reorganizar código sem mudar o que ele faz | `refactor: separa a leitura do CSV em uma função` |

**Mensagens proibidas:** `ajustes`, `mudanças`, `update`, `correções`.

### 6.4 O *pull request* (PR)

1. Confira se tudo foi enviado: `git status` deve dizer `nothing to commit, working tree clean`.
2. No GitHub, abra o repositório. Vai aparecer uma faixa amarela com o botão **Compare & pull request**. Se não aparecer: aba **Pull requests → New pull request**, com **base: `develop`** e **compare: a sua *branch***.
3. A descrição já vem com um modelo. Preencha **Sprint**, **Objetivo**, **O que foi feito** e **Como testar** (os comandos e a saída copiada do terminal).
4. Em **Reviewers**, marque `brunogomesifrn`.
5. No grupo da equipe, avise: `Sprint N pronta para revisão - PR #X`.

**Você não faz o *merge* do seu próprio PR.** Eu reviso e integro. Se eu pedir ajustes (nos comentários do PR), faça na mesma *branch*: o PR se atualiza sozinho. Responda cada comentário dizendo o que fez.

**Você também é revisor.** Os PRs do Samuel e do Gleidson vão marcar você. Leia o código deles e comente o que não seguir o formato da [seção 4](#formato). O *merge* é meu.

### 6.5 Regras de ouro

- **Entregue no prazo, mesmo incompleto.** Na descrição do PR, diga o que faltou.
- **Travou mais de 40 minutos no mesmo erro? Pare e peça ajuda.** Mande mensagem no grupo da equipe, me marcando, com: o que você estava tentando fazer, o comando que rodou e **a mensagem de erro inteira, copiada e colada**.
- **Rode tudo a partir da raiz do repositório:** `python scripts\validar.py ...`, e não de dentro da pasta `scripts`.
- **Diário (`docs/diario.md`):** no fim de cada sprint, 3 linhas. Leva cinco minutos e escreve a sua Conclusão por você:

  ```
  ## Sprint 2 - 27/11 a 03/12
  - Funcionou: ...
  - Deu errado: ...
  - Aprendi: ...
  ```

- **Prints (`docs/evidencias/`):** sempre que algo funcionar, tire um print (`Win + Shift + S`) e salve com um nome que diga o que é, por exemplo `s2_converter_saida.png`. Eles viram figuras do RCC.

---

<a id="estrutura"></a>
## 7. A estrutura de pastas

Esta é a figura final. Cada sprint cria a sua parte.

```
mp_narrativas_catalogo/
├── .github/
│   └── pull_request_template.md   ← já existe
├── dados/
│   ├── modelo.csv                 ← Ítalo, Sprint 1
│   ├── narrativas.csv             ← Ítalo, Sprint 2
│   ├── narrativas.json            ← Ítalo, Sprint 3 (gerado pelo converter.py)
│   ├── teste_validador.csv        ← Ítalo, Sprint 2
│   ├── teste_conversor.csv        ← Samuel (e os dois .json de teste dele)
│   └── fake/                      ← saídas do gerador (NÃO vão para o Git)
├── scripts/
│   ├── validar.py                 ← Ítalo, Sprint 2
│   ├── estatisticas.py            ← Ítalo, Sprint 2
│   ├── converter.py               ← Samuel
│   ├── verificar_json.py          ← Samuel
│   └── gerar_fake.py              ← Gleidson
├── resultados/                    ← gráficos, tabelas e relatórios de erros
├── docs/
│   ├── 01_italo_v2_narrativas_desenvolvimento.md   ← este documento
│   ├── 01_italo_v2_narrativas_escrita.md
│   ├── 01_italo_v2_aluno_1.md
│   ├── 01_italo_v2_aluno_2.md
│   ├── orientacoes_escrita_tcc.md
│   ├── projeto_narrativas.md
│   ├── prototipos/                ← prints da plataforma
│   ├── formato_planilha.md        ← Ítalo, Sprint 1
│   ├── fontes_consultadas.md      ← Ítalo, Sprints 1 e 2
│   ├── leituras.md                ← fichamento (ver o plano de escrita)
│   ├── diario.md
│   └── evidencias/
├── .gitignore
├── requirements.txt
└── README.md
```

---

<a id="sprint-1"></a>
# Sprint 1: 23/11 a 26/11 - Formato da planilha e estrutura do repositório

**Branch:** `feature/formato-planilha` · **PR até:** terça, 24/11

**O que você vai entregar:** o repositório organizado, o formato da planilha documentado em `docs/formato_planilha.md`, o `dados/modelo.csv` com 3 narrativas reais, a planilha no Google Planilhas com as listas de valores travadas e, até quinta, as 10 primeiras narrativas preenchidas.

### Passo a passo

**Segunda, 23/11: ambiente e repositório**

1. Aceite o convite do repositório: https://github.com/nicifrn/mp_narrativas_catalogo/invitations

2. No laboratório, abra o VS Code e o terminal (**Terminal → New Terminal**). Se for a primeira vez nesta máquina, configure o Git com o seu nome e o e-mail da sua conta do GitHub:

   ```
   git config --global user.name "Seu Nome"
   git config --global user.email "seu-email@exemplo.com"
   ```

3. Clone o repositório e entre na pasta:

   ```
   cd $HOME\Documents
   git clone https://github.com/nicifrn/mp_narrativas_catalogo.git
   cd mp_narrativas_catalogo
   code .
   ```

   O último comando abre a pasta no VS Code. Daqui em diante, use o terminal **dessa** janela. Se o Git pedir login, vai abrir uma janela do navegador: entre com a sua conta do GitHub e autorize.

4. Confira que você está na `develop` e crie a sua *branch*:

   ```
   git branch
   git checkout -b feature/formato-planilha
   ```

   O `git branch` deve mostrar `* develop` antes de você criar a nova.

5. Crie o ambiente virtual e instale o `matplotlib`:

   ```
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   pip install matplotlib
   pip show matplotlib
   ```

   O `pip show` mostra a versão instalada, na linha `Version:` (por exemplo, `3.9.2`). Crie na raiz do repositório o arquivo `requirements.txt` com **uma linha só**, usando a versão que apareceu: `matplotlib==3.9.2`. É esse arquivo que permite a outra pessoa instalar exatamente a mesma biblioteca com `pip install -r requirements.txt`.

   Com o ambiente ativo, o terminal mostra `(.venv)` no começo da linha. **Toda vez que abrir o terminal**, ative de novo com `.venv\Scripts\Activate.ps1`.

   > **Erro "a execução de scripts foi desabilitada neste sistema"?** No terminal do VS Code, clique na setinha ao lado do **+** e escolha **Command Prompt**. No Command Prompt, o comando de ativar é `.venv\Scripts\activate.bat`. O resto é igual.

6. Crie as pastas que ainda não existem. O Git não guarda pasta vazia, então coloque um arquivo `.gitkeep` (vazio) em cada uma:

   ```
   mkdir dados, scripts, resultados, docs\evidencias
   New-Item dados\.gitkeep, scripts\.gitkeep, resultados\.gitkeep, docs\evidencias\.gitkeep
   ```

   (No Command Prompt, crie as pastas e os arquivos pelo explorador do VS Code: botão direito → **New Folder** / **New File**.)

7. Crie o `.gitignore` na raiz, com este conteúdo:

   ```
   .venv/
   __pycache__/
   dados/fake/
   ```

   A pasta `dados/fake/` fica de fora porque o gerador do Gleidson cria arquivos com milhares de linhas, que podem ser gerados de novo a qualquer momento.

8. O `README.md` já existe na raiz do repositório: ele explica o trabalho e tem os links para os planos dos três. **Não apague nem substitua.** Nesta sprint, só acrescente, na seção "Documentos de apoio", uma linha com o link para o `docs/formato_planilha.md` quando ele for criado. A seção "Como rodar" você completa na Sprint 3.

9. Primeiro *commit* e envio:

   ```
   git status
   git add .
   git commit -m "docs: cria estrutura de pastas, gitignore e requirements"
   git push
   ```

   (Na primeira vez, use o comando `git push --set-upstream ...` que o Git mostrar.)

**Segunda e terça, 23 e 24/11: o formato**

10. Abra e leia, nesta ordem:
    - [`docs/projeto_narrativas.md`](projeto_narrativas.md), para entender o projeto;
    - o print `docs/prototipos/narrativa_detalhes.png`. É a tela de uma narrativa no portal. No quadro **Informações**, à direita, aparecem os campos que a plataforma pretende mostrar: Tipo, Região, Local, Público-alvo, Período histórico, Origem, Idioma original. Embaixo do texto, as Palavras-chave. Compare com as colunas da [seção 4](#formato): a maior parte delas vem daí;
    - os planos dos colegas, [`docs/01_italo_v2_aluno_1.md`](01_italo_v2_aluno_1.md) e [`docs/01_italo_v2_aluno_2.md`](01_italo_v2_aluno_2.md).

11. Confira as **mesorregiões do RN** no IBGE. Abra no navegador:

    https://servicodados.ibge.gov.br/api/v1/localidades/estados/RN/mesorregioes

    O navegador mostra uma lista em JSON com as 4 mesorregiões (Oeste Potiguar, Central Potiguar, Agreste Potiguar e Leste Potiguar). No Firefox, a lista aparece formatada; no Chrome, marque a caixa **Estilo de formatação** (*Pretty-print*) no alto da página.

    Para saber a mesorregião de cada município, abra:

    https://servicodados.ibge.gov.br/api/v1/localidades/estados/RN/municipios

    Cada município aparece com `"nome"` e, dentro de `"microrregiao"`, a `"mesorregiao"`. Use `Ctrl + F` para achar o município que você quer. Guarde esses dois endereços: eles vão para as Referências do RCC (como IBGE) e você vai voltar a eles toda vez que preencher uma narrativa.

12. Escreva o **dicionário de dados** em `docs/formato_planilha.md`. É o documento que explica o formato para quem nunca viu o trabalho. Use esta estrutura:

    ```markdown
    # Formato da planilha de narrativas

    ## Arquivo
    (CSV, UTF-8, vírgula, cabeçalho na linha 1, primeira narrativa na linha 2)

    ## Colunas
    | # | Coluna | Obrigatória | Tipo | Regra | Por que existe |
    |---|---|---|---|---|---|
    | 1 | id | sim | inteiro | ... | identifica a narrativa sem depender do título |
    ...

    ## Listas de valores
    ### tipo
    - lenda: ...  (uma linha explicando cada valor)
    ...

    ## Arquivos de erros
    (o formato linha,coluna,erro e a tabela de códigos)
    ```

    A coluna **"Por que existe"** é sua: para cada coluna, diga em uma frase para que ela serve na plataforma (por exemplo: `mesorregiao` permite filtrar o acervo por região do estado, como o campo "Região" do protótipo). Isso vai quase direto para a Metodologia.

    Para a lista de **tipo**, escreva uma linha explicando cada valor (o que diferencia uma lenda de um mito, um conto de um causo). Pesquise em dicionário (Houaiss, Aulete *on-line*: https://aulete.com.br) e, se puder, no *Dicionário do folclore brasileiro*, de Câmara Cascudo, na biblioteca do campus. Anote de onde tirou cada definição: você vai precisar no Referencial.

    Para a lista de **licença**, explique cada valor. Pesquise em https://creativecommons.org/licenses/?lang=pt-BR (o que é CC BY e CC BY-SA) e na Lei nº 9.610/1998, a Lei de Direitos Autorais (http://www.planalto.gov.br/ccivil_03/leis/l9610.htm), artigo 41: a obra entra em **domínio público 70 anos** depois de 1º de janeiro do ano seguinte à morte do autor.

    Para a coluna **`texto`**, escreva no dicionário a regra (de 2 a 3 trechos curtos, entre aspas, separados por ` | `) e a justificativa: a citação de passagens permitida pelo art. 46, inciso III, da Lei nº 9.610/1998 (veja a [seção 3](#decisoes)). Diga também que a coluna se chama `texto`, e não `trechos`, porque poderá receber o texto completo das narrativas cujos direitos permitirem.

13. Crie a planilha no **Google Planilhas** (https://sheets.google.com → **Em branco**). Nome: `Catálogo de narrativas do RN`.
    - Na linha 1, digite os 12 nomes das colunas, um por célula, de A a L, exatamente como na [seção 4](#formato).
    - Congele o cabeçalho: **Ver → Congelar → 1 linha**.
    - Deixe a coluna G (`texto`) mais larga e com quebra de linha automática, para ler os trechos inteiros: selecione a coluna G → **Formatar → Ajuste de texto → Quebrar**.
    - **Trave as listas.** Selecione a coluna C inteira (clique na letra **C**), vá em **Dados → Validação de dados → Adicionar regra**. Em **Critérios**, escolha **Menu suspenso** e cadastre um valor por item: `lenda`, `conto`, `causo`, `mito`, `cordel`. Em **Opções avançadas**, marque **Rejeitar a entrada**. Clique em **Concluído**. Faça o mesmo para `publico` (D), `mesorregiao` (F) e `licenca` (L).
    - A regra também vai valer para a célula do cabeçalho e vai marcá-la como inválida. Isso não atrapalha: ignore o aviso na linha 1.
    - Compartilhe a planilha comigo como **Leitor** (botão **Compartilhar**, com o e-mail que eu passar no grupo da equipe).

    O menu suspenso evita erro de digitação na planilha real. Registre isso no diário: na Sprint 3, quando o seu validador rodar na planilha, ele vai achar poucos erros nessas colunas, e a explicação é essa trava.

14. Preencha **3 narrativas reais** na planilha (veja "Onde pesquisar" no passo 17) e baixe como CSV: **Arquivo → Fazer download → Valores separados por vírgula (.csv)**. O arquivo vem com um nome como `Catálogo de narrativas do RN - Página1.csv`. Mova para a pasta `dados/` do repositório e renomeie para `modelo.csv`.

    > **Nunca abra nem salve o CSV no Excel.** O Excel do Windows troca os acentos por símbolos estranhos e pode trocar a vírgula por ponto e vírgula. Para ver o arquivo, abra no VS Code.

    Abra o `dados/modelo.csv` no VS Code e confira: a primeira linha é o cabeçalho, os acentos aparecem certos, e a coluna `texto` aparece com as aspas **dobradas** (`"""Primeiro trecho..."" | ""Segundo trecho..."""`). É assim que o CSV guarda aspas dentro de um valor: está certo.

15. Confira o CSV com o Python, direto no terminal. Digite `python` e, dentro dele, linha por linha:

    ```python
    import csv
    with open("dados/modelo.csv", encoding="utf-8") as arquivo:
        for linha in csv.DictReader(arquivo):
            print(linha["id"], linha["titulo"], linha["municipio"])
    ```

    Devem aparecer as 3 narrativas, com os acentos certos. Para sair do Python, digite `exit()`. Tire um print: ele mostra que o arquivo é lido sem erro.

16. *Commit*, envio e PR (até terça, 24/11):

    ```
    git add .
    git commit -m "docs: documenta o formato da planilha e adiciona modelo"
    git push
    ```

    Abra o PR para a `develop` (veja a [seção 6.4](#fluxo-git)). Avise os colegas no grupo da equipe que o formato está no PR.

**Quarta e quinta, 25 e 26/11: as primeiras 10 narrativas**

17. **Onde pesquisar as narrativas.** Comece pelas fontes que têm a referência completa (autor, obra, ano), porque a coluna `fonte` é obrigatória:

    | Fonte | Onde | O que procurar |
    |---|---|---|
    | Obras de **Luís da Câmara Cascudo** | biblioteca do campus; Biblioteca Central Zila Mamede (UFRN) | *Lendas brasileiras*, *Contos tradicionais do Brasil*, *Geografia dos mitos brasileiros*, *Dicionário do folclore brasileiro*. Cascudo indica onde ouviu cada narrativa: é daí que sai o `municipio` |
    | Literatura de **cordel** | acervo de cordel da Fundação Casa de Rui Barbosa (https://www.gov.br/casaruibarbosa) e Biblioteca Nacional Digital (https://bndigital.bn.gov.br) | cordéis de autores potiguares ou que contam histórias de lugares do RN |
    | Obras em **domínio público** | Domínio Público (http://www.dominiopublico.gov.br) e Brasiliana Guita e José Mindlin (https://digital.bbm.usp.br) | coletâneas de contos e lendas populares do Nordeste |
    | **Artigos e trabalhos acadêmicos** | Google Acadêmico (https://scholar.google.com.br) e repositório da UFRN (https://repositorio.ufrn.br) | busque `lendas "Rio Grande do Norte"`, `narrativas orais Seridó`, `cultura popular potiguar` |
    | **Prefeituras e turismo** | sites das prefeituras e da Secretaria de Turismo do RN | busque no Google `lenda` + nome do município, por exemplo `lenda Caicó`, `lenda Martins RN` |
    | IPHAN | http://portal.iphan.gov.br | registros de bens culturais imateriais do RN |

    **Critério para entrar no catálogo:** a narrativa precisa ter **uma fonte que você consiga citar** e **um município do RN** associado a ela. Narrativa sem fonte ou sem município do RN não entra.

    **Tente cobrir as quatro mesorregiões.** Se, depois de procurar, uma região tiver poucas narrativas, isso não é falha sua: é um **resultado** (uma lacuna de registro que o projeto precisa conhecer). Anote.

18. Para cada narrativa:
    - leia a narrativa na fonte;
    - escolha **de 2 a 3 trechos curtos** e copie para a coluna `texto` (veja as regras logo abaixo);
    - escolha o `tipo` e o `publico` (anote no diário os casos em que ficou em dúvida: isso é discussão para o RCC);
    - preencha o `municipio` e confira a `mesorregiao` na lista do IBGE (passo 11);
    - escreva a `fonte` no formato da ABNT (veja [`docs/orientacoes_escrita_tcc.md`](orientacoes_escrita_tcc.md), seção de Referências);
    - escolha a `licenca` **da fonte**: obra de autor que morreu há mais de 70 anos é `dominio_publico`; Câmara Cascudo morreu em 1986, então as obras dele são `direitos_reservados`; site sem informação de licença é `desconhecida`.

    **Regras dos trechos:**

    - cada trecho tem de **1 a 3 linhas** da fonte. Trecho curto é o que a lei permite; se passou disso, corte;
    - escolha trechos que identifiquem a narrativa: por exemplo, um do começo (quem é o personagem, onde acontece), um do momento principal e, se quiser, um do desfecho;
    - copie **exatamente** como está na fonte, com a mesma grafia, mesmo que seja a ortografia antiga (`pharmacia`, `Brazil`). Não corrija, não resuma, não troque palavras;
    - se precisar cortar um pedaço no meio do trecho, marque o corte com `[...]`, como manda a ABNT para citação direta;
    - cada trecho vai **entre aspas**, e os trechos são separados por ` | `. Exemplo do que você digita na célula: `"Primeiro trecho copiado da fonte." | "Segundo trecho copiado da fonte."`;
    - se o trecho tiver aspas dentro (uma fala de personagem, por exemplo), troque essas aspas internas por aspas simples (`'`), como manda a ABNT para citação dentro de citação;
    - se o trecho tiver o caractere `|`, troque por `/`.

    Conte com 10 a 15 minutos por narrativa, quase todo o tempo para achar a fonte. São 10 até quinta.

19. Crie `docs/fontes_consultadas.md` e registre **toda fonte que você abriu**, inclusive as que não renderam nenhuma narrativa:

    ```markdown
    | Data | Fonte | Onde | Narrativas aproveitadas | Observação |
    |---|---|---|---|---|
    | 25/11 | CASCUDO, Lendas brasileiras | biblioteca do campus | 4 | ... |
    | 25/11 | site da prefeitura de X | (endereço) | 0 | não cita a fonte da lenda |
    ```

    Essa tabela vira o parágrafo de "coleta" da Metodologia.

20. No fim da quinta, escreva a entrada da Sprint 1 no `docs/diario.md`, faça o *commit* (`docs: registra fontes consultadas e diário da sprint 1`) e envie. A planilha **não** vai para o repositório ainda: só na Sprint 2.

### Como saber que deu certo

- O PR da Sprint 1 está aberto (ou já integrado) com `docs/formato_planilha.md`, `dados/modelo.csv`, `.gitignore`, `requirements.txt` e `README.md`.
- O `git status` não mostra `.venv/`.
- O Python lê o `modelo.csv` e mostra as 3 narrativas com acento certo.
- Na planilha do Google, as colunas C, D, F e L só aceitam os valores da lista.
- A planilha tem pelo menos 10 narrativas reais.

### Entrega da sprint

- [ ] PR para a `develop` até **24/11**
- [ ] `docs/formato_planilha.md` com as 12 colunas, a justificativa de cada uma e a explicação de cada valor das listas
- [ ] `dados/modelo.csv` com o cabeçalho e 3 narrativas reais
- [ ] Planilha no Google com menu suspenso nas 4 colunas de lista, compartilhada comigo
- [ ] 10 narrativas preenchidas na planilha até **26/11**
- [ ] `docs/fontes_consultadas.md` e `docs/diario.md` atualizados

### Erros comuns

- **Acentos estranhos no CSV** (`CaicÃ³`): o arquivo foi aberto ou salvo no Excel, ou foi lido sem `encoding="utf-8"`. Baixe de novo do Google Planilhas e abra só no VS Code.
- **`KeyError: 'id'`** ao ler o CSV: o nome da coluna no cabeçalho está diferente (maiúscula, espaço no fim, acento). Corrija na planilha e baixe de novo.
- **Trecho reescrito ou resumido:** os trechos são copiados **exatamente** como estão na fonte, entre aspas. Se você mudou palavras, deixou de ser citação.

---

<a id="sprint-2"></a>
# Sprint 2: 27/11 a 03/12 - Catálogo, validador e estatísticas

**Branch:** `feature/catalogo-validador` · **PR até:** quinta, 03/12

**O que você vai entregar:** a planilha com 20 narrativas no repositório (`dados/narrativas.csv`), o `validar.py`, que confere a planilha e grava os erros encontrados, e o `estatisticas.py`, que conta as narrativas e faz dois gráficos.

### Passo a passo

1. Atualize a `develop` (o PR da Sprint 1 já deve ter sido integrado) e crie a *branch* da semana:

   ```
   git checkout develop
   git pull
   git checkout -b feature/catalogo-validador
   ```

2. **Até terça, 01/12:** complete a planilha até **20 narrativas**, do mesmo jeito da Sprint 1 (passos 17 a 19). Em paralelo, programe o validador (passos 3 a 9): uma hora por dia de programação e o resto em narrativas.

**O validador (`scripts/validar.py`)**

3. **O arquivo de teste.** Antes de programar, crie uma planilha pequena em que **você já sabe** onde está cada erro. É com ela que você testa o validador o tempo todo.

   1. No Google Planilhas, crie uma planilha nova chamada `Teste do validador`, com os 12 nomes das colunas na linha 1.
   2. Na linha 2, preencha uma narrativa **sem nenhum erro** (pode copiar uma do seu catálogo).
   3. Copie a linha 2 para as linhas 3 a 9, troque o `id` de cada uma (2, 3, 4...) e estrague **uma coluna por linha**:

      | Linha da planilha | O erro que você coloca | O validador deve dizer |
      |---|---|---|
      | 3 | `titulo` vazio | `3,titulo,vazio` |
      | 4 | `ano_fonte` = `mil novecentos` | `4,ano_fonte,nao_inteiro` |
      | 5 | `ano_fonte` = `3000` | `5,ano_fonte,fora_da_faixa` |
      | 6 | `tipo` = `historia` | `6,tipo,fora_da_lista` |
      | 7 | `licenca` vazia | `7,licenca,vazio` |
      | 8 | `id` igual ao da linha 2 | `8,id,repetido` |
      | 9 | `mesorregiao` = `seridó` | `9,mesorregiao,fora_da_lista` |

      Lembre: o cabeçalho é a linha 1. Se você fez a planilha de teste copiando a do catálogo, ela veio com o menu suspenso: tire (**Dados → Validação de dados →** lixeira em cada regra), senão o Google não aceita `historia` nem `seridó`.

   4. Baixe como CSV, mova para `dados/` e renomeie para `teste_validador.csv`. Copie a tabela acima para a descrição do PR: é a "resposta esperada".

4. **O que o validador faz.** Você roda assim:

   ```
   python scripts\validar.py dados\teste_validador.csv
   ```

   E ele:

   1. pega o nome do arquivo que veio no comando;
   2. confere se o cabeçalho tem as 12 colunas certas, na ordem certa. Se não tiver, avisa e para;
   3. confere cada linha com as **5 regras** da [seção 4.3](#formato): `vazio`, `nao_inteiro`, `fora_da_faixa`, `fora_da_lista` e `repetido`;
   4. mostra cada erro na tela (`Linha 3, coluna titulo: vazio`) e, no fim, quantas linhas leu e quantos erros encontrou;
   5. grava os erros em `resultados/erros_<nome do arquivo>.csv`, no formato `linha,coluna,erro`.

   **Um erro por coluna, no máximo.** Coluna obrigatória vazia é só `vazio`: não confira mais nada nela. Ano que não é inteiro é só `nao_inteiro`: não confira a faixa. Coluna opcional vazia (`ano_fonte`, `url_fonte`, `palavras_chave`) **não** é erro. Espaços sobrando no começo ou no fim (`" lenda "`) também não: tire com `.strip()` antes de conferir.

5. **As peças que você vai usar.** Pesquise cada uma na documentação do Python em português: https://docs.python.org/pt-br/3/library/csv.html, https://docs.python.org/pt-br/3/library/sys.html e https://docs.python.org/pt-br/3/tutorial/errors.html#handling-exceptions.

   O nome do arquivo que vem no comando fica na lista `sys.argv`. A posição 0 é o próprio programa:

   ```python
   import sys

   # python scripts\validar.py dados\teste_validador.csv
   # sys.argv[0] -> "scripts\validar.py"
   # sys.argv[1] -> "dados\teste_validador.csv"

   if len(sys.argv) != 2:
       print("Uso: python scripts\\validar.py ARQUIVO.csv")
       sys.exit(1)
   ```

   O formato vira código em constantes no começo do programa:

   ```python
   COLUNAS = ["id", "titulo", "tipo", "publico", "municipio", "mesorregiao",
              "texto", "palavras_chave", "fonte", "url_fonte", "ano_fonte", "licenca"]

   OBRIGATORIAS = ["id", "titulo", "tipo", "publico", "municipio",
                   "mesorregiao", "texto", "fonte", "licenca"]

   LISTAS = {
       "tipo": {"lenda", "conto", "causo", "mito", "cordel"},
       "publico": {...},
       "mesorregiao": {...},
       "licenca": {...},
   }

   ANO_MINIMO = 1500
   ANO_MAXIMO = 2026
   ```

   Ler o CSV, conferir o cabeçalho e numerar as linhas a partir de 2 (o `enumerate` com `start=2`):

   ```python
   with open(caminho, encoding="utf-8") as arquivo:
       leitor = csv.DictReader(arquivo)
       if leitor.fieldnames != COLUNAS:
           print("Cabeçalho diferente do formato.")
           print("Esperado:", COLUNAS)
           print("Encontrado:", leitor.fieldnames)
           sys.exit(1)
       for numero, linha in enumerate(leitor, start=2):
           # numero é 2, 3, 4...  linha é um dicionário: linha["titulo"]
           ...
   ```

   Saber se um texto é número inteiro: tente converter; se não der, o Python lança um `ValueError`:

   ```python
   try:
       ano = int(valor)
   except ValueError:
       erros.append((numero, "ano_fonte", "nao_inteiro"))
   ```

   Teste no terminal do Python `int("1950")`, `int("mil")` e `int("19.5")` para ver o que acontece em cada caso.

   Achar `id` repetido: um conjunto com os `id` já vistos, criado **antes** do `for` das linhas. Confira se o `id` já está no conjunto e **só depois** acrescente; senão, todo `id` aparece como repetido.

   Guarde os erros em uma lista de tuplas `(linha, coluna, erro)`, e não só mostre na tela: a mesma lista vai para o relatório.

6. **Organize em funções**, uma por regra. Um esqueleto (os comentários dizem o que fazer; o código é seu):

   ```python
   def conferir_vazios(numero, linha, erros): ...      # percorra OBRIGATORIAS com um for
   def conferir_inteiros(numero, linha, erros): ...    # id e ano_fonte, e a faixa do ano
   def conferir_listas(numero, linha, erros): ...      # percorra LISTAS.items()
   def conferir_repetido(numero, linha, ids_vistos, erros): ...
   def validar(caminho): ...                           # devolve (total_de_linhas, erros)
   def gravar_relatorio(erros, caminho): ...

   # aqui: conferir o sys.argv, chamar validar, mostrar os erros e os totais, gravar o relatório
   ```

   Cada função ignora as colunas vazias: quem cuida delas é a `conferir_vazios`. Assim vale a regra "um erro por coluna".

7. **O relatório em CSV.** Monte o nome com o `os.path` e grave com o `csv.writer`:

   ```python
   import os

   nome = os.path.splitext(os.path.basename(caminho))[0]   # "teste_validador"
   saida = os.path.join("resultados", f"erros_{nome}.csv")

   os.makedirs("resultados", exist_ok=True)
   with open(saida, "w", encoding="utf-8", newline="") as arquivo:
       escritor = csv.writer(arquivo)
       escritor.writerow(["linha", "coluna", "erro"])
       for erro in erros:
           escritor.writerow(erro)
   ```

   O `newline=""` é obrigatório no Windows: sem ele, sai uma linha em branco entre cada linha. Grave o relatório **mesmo sem erro** (só com o cabeçalho) e na ordem das linhas (2, 3, 4...): na Sprint 3, você vai comparar esse arquivo com o gabarito do gerador do Gleidson, que segue a mesma ordem.

8. Rode com o arquivo de teste. Devem sair **os 7 erros** da tabela do passo 3, e o `resultados\erros_teste_validador.csv` deve ser igual à coluna "O validador deve dizer". Teste também: o cabeçalho errado (copie o arquivo, troque `titulo` por `Titulo` e rode: o validador avisa e para) e o comando sem o nome do arquivo (mostra a mensagem de uso).

   Faça um *commit* a cada regra que funcionar: `feat: confere campos vazios`, `feat: confere números inteiros e faixa do ano`, `feat: confere valores das listas e id repetido`, `feat: grava relatório de erros`.

9. **Ainda não rode o validador na planilha real.** Isso é o primeiro passo da Sprint 3: a versão "antes da correção" é um dos seus resultados.

**O catálogo e as estatísticas**

10. **Na terça, 01/12**, com as 20 narrativas prontas, baixe a planilha como CSV (Sprint 1, passo 14) e salve como `dados/narrativas.csv`. Faça o *commit*: `docs: adiciona catálogo com 20 narrativas`.

    **Não corrija mais nada nesta versão**, mesmo que você ache algum erro. Se achar, anote no diário e deixe para a Sprint 3.

11. **As estatísticas (`scripts/estatisticas.py`).** Ele lê o **CSV** (não o JSON: assim você não depende do conversor do Samuel) e produz:

    | Saída | Arquivo |
    |---|---|
    | total de narrativas e de municípios diferentes | tela e `resultados/estatisticas.txt` |
    | quantas narrativas por `tipo`, por `publico`, por `mesorregiao` e por `licenca` | tela e `resultados/estatisticas.txt` |
    | gráfico de barras por `tipo` | `resultados/grafico_tipo.png` |
    | gráfico de barras por `mesorregiao` | `resultados/grafico_mesorregiao.png` |

    ```
    python scripts\estatisticas.py dados\narrativas.csv
    ```

12. **As peças das estatísticas.**

    Contar com o `Counter` (https://docs.python.org/pt-br/3/library/collections.html#collections.Counter):

    ```python
    import csv
    from collections import Counter

    with open(caminho, encoding="utf-8") as arquivo:
        narrativas = list(csv.DictReader(arquivo))

    por_tipo = Counter(n["tipo"].strip() for n in narrativas)
    print(por_tipo)                  # Counter({'lenda': 12, 'conto': 8, ...})
    ```

    Municípios diferentes: `len({n["municipio"].strip() for n in narrativas})` (um conjunto não repete valores).

    Um gráfico de barras com o `matplotlib` (https://matplotlib.org/stable/gallery/lines_bars_and_markers/bar_colors.html):

    ```python
    import matplotlib.pyplot as plt

    plt.figure(figsize=(8, 5))
    plt.bar(list(por_tipo.keys()), list(por_tipo.values()))
    plt.xlabel("Tipo de narrativa")
    plt.ylabel("Quantidade")
    plt.savefig("resultados/grafico_tipo.png", dpi=150, bbox_inches="tight")
    plt.close()
    ```

    **Não coloque título no gráfico** (`plt.title`): no RCC, o título vai na legenda da figura, acima dela, como manda a ABNT. Os dois gráficos são iguais na forma: escreva **uma função** que recebe o `Counter`, o nome do eixo e o nome do arquivo, e chame duas vezes.

    Para o `estatisticas.txt`, monte as linhas em uma lista e grave no fim com `arquivo.write("\n".join(linhas))`.

13. Rode, abra os gráficos e o `estatisticas.txt` e confira as contas **à mão** em pelo menos uma coluna (filtre a planilha do Google pelo tipo e conte). Se a conta do programa não bater com a sua, o programa está errado.

    Faça o *commit*: `feat: adiciona estatísticas e gráficos do catálogo`.

14. **Revise os PRs dos colegas.** Até quinta, o Samuel e o Gleidson abrem os PRs deles e marcam você. Abra cada um, aba **Files changed**, e confira se os nomes das colunas, os valores das listas e os códigos de erro estão **exatamente** como na [seção 4](#formato). Se houver diferença, comente na linha (passe o mouse sobre a linha e clique no **+** azul).

15. Escreva o diário da Sprint 2, faça o *commit*, envie e abra o PR até **quinta, 03/12**. Em **Como testar**, cole a saída dos dois programas e a tabela de resposta esperada do validador.

### Como saber que deu certo

- Com o arquivo de teste, a saída do validador e o `resultados\erros_teste_validador.csv` batem, erro por erro, com a tabela do passo 3. A linha 2 (a certa) não gera erro nenhum.
- `dados/narrativas.csv` tem 21 linhas (cabeçalho + 20).
- `resultados/` tem os 2 gráficos e o `estatisticas.txt`, e as contas batem com a contagem à mão.

### Entrega da sprint

- [ ] 20 narrativas na planilha até **01/12** e `dados/narrativas.csv` no repositório (sem correções depois disso)
- [ ] `dados/teste_validador.csv` com 8 narrativas e 7 erros conhecidos
- [ ] `scripts/validar.py` com as 5 regras e o relatório `resultados/erros_<nome>.csv`
- [ ] `scripts/estatisticas.py` gerando `resultados/estatisticas.txt` e 2 gráficos
- [ ] Contagem conferida à mão em pelo menos uma coluna
- [ ] PRs dos colegas revisados
- [ ] PR para a `develop` até **03/12**

### Erros comuns

- **O `id` da primeira linha aparece como repetido:** você acrescentou o `id` no conjunto **antes** de conferir. Confira antes, acrescente depois.
- **`fora_da_lista` para valores certos:** faltou o `.strip()`, ou a lista do programa tem um valor digitado diferente do formato.
- **Erro `vazio` e `nao_inteiro` na mesma coluna:** a função de inteiros não está ignorando os valores vazios.
- **Linha em branco entre as linhas do relatório:** faltou `newline=""` no `open` de escrita.
- **`ModuleNotFoundError: No module named 'matplotlib'`**: o ambiente virtual não está ativo. Ative (`.venv\Scripts\Activate.ps1`) e rode de novo.
- **`FileNotFoundError`**: você rodou de dentro da pasta `scripts`. Volte para a raiz (`cd ..`).
- **Gráfico com os nomes das barras encavalados:** use `plt.xticks(rotation=45)` antes do `savefig`.

---

<a id="sprint-3"></a>
# Sprint 3: 04/12 a 10/12 - Integração e fechamento

**Branch:** `feature/integracao` · **PR até:** segunda, 07/12

**O que você vai entregar:** a planilha real validada e corrigida, o `dados/narrativas.json` gerado pelo conversor do Samuel e conferido pelo verificador dele, o seu validador testado com as bases fictícias do Gleidson, o `resultados/resumo.md` e o `README.md` final.

**A integração acontece na sexta, 04/12.** Nesse dia, os PRs dos colegas já foram integrados por mim na `develop`. Ela leva umas duas horas: é só rodar os programas na ordem certa e guardar as saídas.

### Passo a passo

1. Atualize a `develop` e crie a *branch*:

   ```
   git checkout develop
   git pull
   git checkout -b feature/integracao
   ```

   Confira que os programas dos colegas chegaram: `scripts\converter.py`, `scripts\verificar_json.py` e `scripts\gerar_fake.py` precisam existir.

2. **Validador na planilha real, antes da correção.** Rode sobre o `dados\narrativas.csv` da Sprint 2, **sem corrigir nada**:

   ```
   python scripts\validar.py dados\narrativas.csv
   ```

   **Renomeie** o `resultados\erros_narrativas.csv` para `resultados\erros_narrativas_antes.csv` e tire um print da tela. Se der 0 erros, ótimo: isso também é resultado (lembre do menu suspenso da Sprint 1, passo 13).

3. **Corrija a planilha.** Para cada erro, corrija **no Google Planilhas**, baixe de novo o CSV para `dados\narrativas.csv` e rode o validador outra vez, até ele mostrar **0 erros**. Tire um print e gere de novo as estatísticas:

   ```
   python scripts\validar.py dados\narrativas.csv
   python scripts\estatisticas.py dados\narrativas.csv
   ```

   Faça o *commit*: `fix: corrige erros apontados pelo validador na planilha`.

4. **O JSON.** Com a planilha sem erros, rode o conversor do Samuel e depois o verificador dele:

   ```
   python scripts\converter.py dados\narrativas.csv dados\narrativas.json
   python scripts\verificar_json.py dados\narrativas.csv dados\narrativas.json
   ```

   O verificador deve dizer `Diferenças: 0`. Abra o `dados\narrativas.json` no VS Code e olhe uma narrativa: `id` sem aspas, acentos certos. Tire um print das duas saídas. Faça o *commit*: `docs: adiciona catálogo em JSON`.

   Se o conversor ou o verificador der problema, avise o Samuel no grupo da equipe, com o comando e a saída inteira, e me marque. Ele corrige até terça, 08/12, e você roda de novo.

   **Por que nessa ordem?** O conversor transforma `ano_fonte` em número; se a planilha tiver `mil novecentos` no ano, ele para. Por isso o validador roda **antes**. Anote no diário: é um parágrafo da Metodologia.

5. **O validador com as bases fictícias.** Gere duas bases com o gerador do Gleidson e rode o seu validador em cada uma:

   ```
   python scripts\gerar_fake.py 100
   python scripts\validar.py dados\fake\fake_100.csv
   python scripts\gerar_fake.py 1000
   python scripts\validar.py dados\fake\fake_1000.csv
   ```

   O gerador cria a planilha (`dados\fake\fake_100.csv`) e o gabarito com os erros que inseriu (`dados\fake\fake_100_gabarito.csv`). O seu validador grava o que encontrou em `resultados\erros_fake_100.csv`. Os dois arquivos têm o mesmo formato e a mesma ordem, então **devem ser iguais**.

   Para comparar, use o próprio VS Code: no explorador, clique no gabarito, segure `Ctrl`, clique no relatório do validador, botão direito → **Compare Selected**. Se nenhuma linha ficar destacada, os dois são iguais. Faça isso para a base de 100 e para a de 1.000 e tire um print de cada.

   **Se aparecer diferença:** abra a linha indicada no `fake_100.csv` (`Ctrl + G` e o número) e veja quem está certo. Se o valor está fora das regras e o seu validador não pegou, corrija o validador. Se o gabarito está errado, avise o Gleidson no grupo da equipe, com a linha, a coluna e o valor, e me marque. Anote no diário o que aconteceu: vai para os Resultados.

   Como a pasta `dados/fake/` não vai para o Git, **anote no README o comando exato** que gerou cada base. O gerador usa uma semente fixa, então o mesmo comando gera sempre os mesmos dados.

6. **O resumo** em `resultados\resumo.md`. É dele que você escreve os Resultados do RCC:

   ```markdown
   | O que foi feito | Resultado |
   |---|---|
   | Narrativas no catálogo | 20, de ... municípios |
   | Tipo mais frequente | ... (n) |
   | Mesorregião com mais / com menos narrativas | ... (n) / ... (n) |
   | Erros na planilha real antes da correção | ... (quais: ...) |
   | Erros depois da correção | 0 |
   | JSON gerado e verificado | 20 narrativas, 0 diferenças |
   | Base fictícia de 100: erros inseridos / encontrados pelo validador | ... / ... |
   | Base fictícia de 1.000: erros inseridos / encontrados pelo validador | ... / ... |
   ```

   Para contar os erros de um arquivo, abra no VS Code e veja o número da última linha: o total de erros é esse número menos 1 (o cabeçalho).

7. **O `README.md` final.** Complete o README (a seção "Como rodar" e o que faltar) para que qualquer pessoa da equipe consiga rodar tudo do zero. Mantenha a tabela da equipe e os links para os planos. Ele precisa ter:

   - como instalar (clonar, criar o ambiente, `pip install -r requirements.txt`);
   - **a ordem de execução**, com os comandos exatos dos passos 2 a 5;
   - o link para o formato (`docs/formato_planilha.md`);
   - a observação sobre direitos autorais (o catálogo guarda só de 2 a 3 trechos curtos de cada narrativa, com a referência, conforme o art. 46, inciso III, da Lei nº 9.610/1998).

   Teste o README de verdade: apague a pasta `dados\fake` e os arquivos de `resultados\` (menos o `erros_narrativas_antes.csv` e o `resumo.md`), siga o README do começo ao fim e confira que tudo é gerado de novo.

8. Diário da Sprint 3, *commit*, envio e PR até **segunda, 07/12**. De terça a quinta, só escrita.

### Como saber que deu certo

- O validador mostra 0 erros em `dados/narrativas.csv`.
- `resultados/erros_narrativas_antes.csv` existe e não foi alterado à mão.
- O verificador do Samuel mostra `Diferenças: 0` para o `dados/narrativas.json`.
- Nas bases de 100 e de 1.000, o relatório do validador é igual ao gabarito do gerador (ou a diferença está explicada no diário).
- Seguindo só o README, outra pessoa consegue gerar todas as saídas.

### Entrega da sprint

- [ ] `resultados/erros_narrativas_antes.csv` e prints do validador antes e depois da correção
- [ ] Planilha corrigida e estatísticas geradas de novo
- [ ] `dados/narrativas.json` gerado pelo conversor e conferido pelo verificador
- [ ] Bases de 100 e 1.000 geradas, validadas e comparadas com o gabarito
- [ ] `resultados/resumo.md`
- [ ] `README.md` final, testado do zero
- [ ] PR para a `develop` até **07/12**

---

<a id="riscos"></a>
## 8. Riscos e planos B

| Risco | Quando aparece | O que fazer |
|---|---|---|
| Não encontrar 20 narrativas com fonte e município até 01/12 | Sprint 2 | Feche o catálogo com o que tiver, desde que sejam pelo menos 15, registre todas as tentativas em `docs/fontes_consultadas.md` e diga nos Resultados quantas ficaram. Me avise no grupo da equipe |
| O validador não ficar completo até 03/12 | Sprint 2 | Entregue o que estiver funcionando (no mínimo, cabeçalho e `vazio`) e diga na descrição do PR o que faltou. As regras que faltarem viram limitação no RCC |
| O conversor do Samuel não ficar pronto até 03/12 | Sprint 3 | As suas estatísticas leem o CSV, então nada para. Escreva você um conversor mínimo, de 10 linhas, que só faz `json.dump(list(csv.DictReader(arquivo)), ...)` com `ensure_ascii=False` (tudo fica como texto), e diga nos Resultados que a conversão dos tipos ficou como trabalho futuro |
| O gerador do Gleidson não ficar pronto até 03/12 | Sprint 3 | O teste do validador fica só com o seu `dados/teste_validador.csv`. O teste com bases fictícias vira trabalho futuro |
| Os dois atrasarem | Sprint 3 | O seu trabalho continua completo: formato, catálogo, validador e estatísticas |
| Laboratório fechado ou sem internet | qualquer | A planilha do Google funciona no celular. Preencha narrativas por ele e programe quando voltar |

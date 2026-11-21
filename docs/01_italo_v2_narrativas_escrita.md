# Plano de escrita do RCC - Catálogo estruturado de narrativas do RN

**Aluno:** Ítalo (@italogomees) - Técnico Integrado em Informática

**Orientador:** Prof. Bruno Gomes (@brunogomesifrn) - NIC/IFRN

**Período:** 23/11/2026 a 10/12/2026

**Plano de desenvolvimento correspondente:** [`docs/01_italo_v2_narrativas_desenvolvimento.md`](01_italo_v2_narrativas_desenvolvimento.md)

> **Não há *issues* no GitHub:** este documento é o seu roteiro da escrita. As entregas são avisadas no grupo da equipe.

**Normas e regras de escrita:** [`docs/orientacoes_escrita_tcc.md`](orientacoes_escrita_tcc.md). Tudo o que está lá vale para o seu RCC: estrutura, citações, referências, figuras, tabelas e formatação. Este plano **não repete** as regras da ABNT; ele diz **o que pesquisar e o que escrever** em cada parte do seu trabalho.

> **Importante:** o que segue são **orientações**, não o texto pronto. Não copie estas frases para o RCC. Elas dizem sobre o que é cada parágrafo; o texto tem de ser escrito por você, com as suas palavras e com as referências que você leu.

---

## Sumário

- [1. Como a escrita vai funcionar](#funcionamento)
- [2. Cronograma de entregas](#cronograma)
- [3. A estrutura do seu RCC](#estrutura)
- [4. Fichamento e referências](#fichamento)
- [Entrega 1 - Introdução e Objetivos (26/11)](#entrega-1)
- [Entrega 2 - Referencial Teórico e Metodologia (03/12)](#entrega-2)
- [Entrega 3 - Resultados (08/12)](#entrega-3)
- [Entrega 4 - Conclusão, Resumo, Título e revisão final (10/12)](#entrega-4)
- [5. Referências por onde começar](#referencias)

---

<a id="funcionamento"></a>
## 1. Como a escrita vai funcionar

### Onde escrever

No dia **23/11** eu compartilho com você um documento do Google Drive **já no modelo do IFRN** (capa, folha de rosto, resumo, sumário e as seções da [seção 3](#estrutura)). O documento é novo: o RCC começa do zero.

- **Escreva sempre no documento compartilhado.** Nada de escrever no Word e colar depois: o histórico do Drive mostra o que mudou de uma entrega para outra.
- **Não crie cópias** ("RCC v2", "RCC final"). O Drive guarda tudo em **Arquivo → Histórico de versões**.
- **Marque cada entrega no histórico:** *Arquivo → Histórico de versões → Nomear versão atual*, com um rótulo como `Entrega 1 - Introdução - 26/11`.
- **Comentário se responde, não se apaga.** Responda a cada comentário dizendo o que você fez e só então marque como resolvido.
- **Resolva os comentários da entrega anterior antes de avisar sobre a próxima.**
- **Não dê acesso ao documento a outras pessoas.**

### Como entregar

1. Escreva no documento do Drive.
2. Nomeie a versão no histórico.
3. Avise no grupo da equipe, me marcando: `Entrega 1 pronta para revisão - versão "Entrega 1 - Introdução - 26/11"`.

Eu comento no próprio documento e aviso no grupo quando a entrega estiver aprovada.

### Regras de ouro

- **Entregue no prazo, mesmo incompleto.** No aviso, diga o que ficou faltando.
- **Escreva todo dia um pouco.** Três semanas é pouco tempo: uma hora por dia de escrita rende mais do que um fim de semana inteiro na véspera.
- **Escreva enquanto programa.** Toda decisão que você tomar no código (por que essa coluna, por que validar antes de converter) é um parágrafo da Metodologia. Anote no `docs/diario.md` na hora.

---

<a id="cronograma"></a>
## 2. Cronograma de entregas

| Entrega | Prazo | O que entra |
|---|---|---|
| — | 23/11 (seg) a 24/11 (ter) | Ler as orientações de escrita, o resumo do projeto e as primeiras referências. Começar o fichamento |
| **1** | **26/11 (qui)** | Introdução, Objetivo geral e Objetivos específicos |
| **2** | **03/12 (qui)** | Referencial Teórico (meta: pronto até segunda, 30/11) e Metodologia |
| **3** | **08/12 (ter)** | Resultados |
| **4** | **10/12 (qui)** | Conclusão, revisão da Introdução e dos Objetivos, Resumo, *Abstract*, Título, Apêndices e revisão final |

**Como a escrita conversa com o desenvolvimento:**

- a **Metodologia** (Entrega 2) descreve o que você fez nas Sprints 1 e 2: o formato, a coleta, o validador. Ela é escrita na mesma semana em que você programa, então escreva no dia em que fizer;
- os **Resultados** (Entrega 3) dependem da integração de **sexta, 04/12**. As seções 4.1 e 4.2 (formato e catálogo) podem ser escritas **antes**, com os números da Sprint 2;
- a **Conclusão** precisa estar pronta até **quarta, 09/12**, para sobrar a quinta para o Resumo, o Título e a revisão.

---

<a id="estrutura"></a>
## 3. A estrutura do seu RCC

```
1 INTRODUÇÃO
1.1 Objetivo geral
1.2 Objetivos específicos
2 REFERENCIAL TEÓRICO
2.1 Narrativas populares e patrimônio cultural imaterial
2.2 Acervos digitais e metadados
2.3 Formatos de dados: CSV e JSON
2.4 Qualidade de dados e validação
2.5 Trabalhos relacionados
3 METODOLOGIA
3.1 Classificação da pesquisa
3.2 Etapas do trabalho
3.3 Materiais e métodos
4 RESULTADOS
4.1 O formato da planilha
4.2 O catálogo construído
4.3 A validação da planilha
4.4 O catálogo em JSON
4.5 Limitações
5 CONCLUSÃO
REFERÊNCIAS
APÊNDICE A - Dicionário de dados da planilha
APÊNDICE B - Narrativas catalogadas
```

Tamanho de referência da parte textual: **de 12 a 16 páginas**. Mais ou menos: Introdução, 2; Referencial, 5 a 6; Metodologia, 2 a 3; Resultados, 3 a 4; Conclusão, 1.

### A pergunta do trabalho

Tudo gira em torno de uma pergunta, que aparece na Introdução e é respondida na Conclusão:

> **Como organizar e validar um conjunto de dados de narrativas populares do RN para que ele sirva de base confiável ao acervo digital do projeto Narrativas?**

---

<a id="fichamento"></a>
## 4. Fichamento e referências

**Tudo o que você ler vai para `docs/leituras.md`**, no repositório, neste formato. É o fichamento que transforma leitura em texto:

```
## WANG; STRONG (1996)
- Referência completa (ABNT): ...
- Onde achei: (endereço ou biblioteca)
- Ideia principal, com as minhas palavras: ...
- Trecho que posso citar (com página): "..." (p. X)
- Vou usar na seção: 2.4
```

Regras:

- **Toda afirmação técnica precisa de referência.**
- **Nunca cite uma referência que você não abriu e leu.** Abra o original e confira autor, título, ano e páginas antes de colocar na lista.
- **Documentação oficial** (Python, IBGE) serve para descrever a ferramenta, não para fundamentar conceito. Para conceito, use livro ou artigo.
- **Nada de blog, fórum ou site sem autoria** nas Referências.
- **Crie a seção Referências no primeiro dia** e acrescente cada obra assim que ler.
- **Meta:** de 10 a 15 referências. A [seção 5](#referencias) tem a lista para começar.

**Onde pesquisar:**

| Base | Endereço | Para quê |
|---|---|---|
| Google Acadêmico | https://scholar.google.com.br | artigos em português e inglês. Use aspas para expressão exata: `"qualidade de dados"`, `"acervo digital"`, `"patrimônio imaterial"` |
| Portal de Periódicos CAPES | https://www.periodicos.capes.gov.br | artigos completos. Dentro da rede do IFRN, o acesso é liberado |
| SciELO | https://www.scielo.br | artigos brasileiros revisados |
| Repositório da UFRN | https://repositorio.ufrn.br | trabalhos sobre cultura popular do RN |
| Biblioteca do campus | — | Câmara Cascudo e os livros de metodologia |

---

<a id="entrega-1"></a>
# Entrega 1 - Introdução e Objetivos (prazo: 26/11)

### Antes de escrever (23 e 24/11)

1. Leia **inteiro** o [`docs/orientacoes_escrita_tcc.md`](orientacoes_escrita_tcc.md). Preste atenção nas seções Introdução, Objetivo geral e Objetivos específicos.
2. Leia o [`docs/projeto_narrativas.md`](projeto_narrativas.md). A Introdução do projeto e as referências dele são o ponto de partida da sua: você pode (e deve) usar as mesmas referências, **depois de abrir e ler cada uma**.
3. Leia pelo menos **3 referências** da [seção 5](#referencias): BINDA e DA SILVA (2026), a Convenção da UNESCO (2003) e SAYÃO e SALES (2012). Fiche as três.

### 1 INTRODUÇÃO (cerca de 2 páginas)

A Introdução segue uma ordem fixa de blocos. Escreva um bloco por vez, nesta ordem.

**Bloco 1 - Contextualização (2 parágrafos).** O que são narrativas populares (lendas, contos, causos, mitos, cordéis), por que elas importam para a identidade e a memória de uma comunidade, e por que estão ameaçadas (transmissão oral, envelhecimento de quem conta). Termine falando das tecnologias digitais como forma de registrar e preservar. Referências: BEZERRA (2026), DOS SANTOS FERNANDES e MARTINS (2026), UNESCO (2003), BINDA e DA SILVA (2026).

**Bloco 2 - Problemática (2 parágrafos).** Apresente o projeto Narrativas e a plataforma que ele está construindo. Depois, o problema: **a plataforma ainda não tem acervo**, e não existe um conjunto de dados organizado de narrativas do RN pronto para ser carregado. Cada trabalho que precisou de dados de teste criou a sua própria base, de um jeito diferente. E dados preenchidos à mão, sem um formato definido e sem conferência, chegam com campos vazios, valores escritos de formas diferentes e sem a fonte, o que compromete a confiança no acervo. Feche o bloco com a pergunta do trabalho ([seção 3](#estrutura)), escrita com as suas palavras.

**Bloco 3 - Caminho para a solução (1 parágrafo).** O que a literatura diz que resolve esse tipo de problema: descrever cada item com **metadados** padronizados (SAYÃO e SALES, 2012; DCMI), usar formatos abertos e legíveis por máquina (CSV e JSON) e conferir a **qualidade dos dados** com regras automáticas (WANG e STRONG, 1996). Não aprofunde: isso é o Referencial. Aqui é só o caminho.

**Bloco 4 - Apresentação da solução (1 a 2 parágrafos).** O que **você** fez: definiu um formato de planilha a partir dos campos previstos na plataforma, catalogou 20 narrativas reais do RN com fonte citável, registrando de cada uma de 2 a 3 trechos curtos da fonte original, programou um validador que confere a planilha e, com os colegas, converteu o catálogo para JSON e testou o validador com dados fictícios.

**Bloco 5 - Vínculo com o projeto e escopo (1 parágrafo).** O trabalho faz parte do projeto Narrativas, do NIC/IFRN. Deixe claro o que **não** foi feito: o catálogo guarda trechos curtos citados e a referência, não o texto integral das narrativas, porque a Lei nº 9.610/1998 permite citar passagens de uma obra (art. 46, III), mas não reproduzi-la inteira sem autorização; não houve carga em banco de dados nem interface web; o conversor para JSON e o gerador de dados fictícios foram desenvolvidos por dois colegas do curso (diga isso aqui, com o nome deles).

### 1.1 Objetivo geral (1 frase)

Uma frase, começando com verbo no infinitivo, que diga **o que** foi feito e **para quê**. Ela deve responder à pergunta do trabalho. Releia a seção "Objetivo geral" de [`docs/orientacoes_escrita_tcc.md`](orientacoes_escrita_tcc.md) e o exemplo dela antes de escrever. Os elementos que precisam aparecer: o conjunto de dados, as narrativas populares do RN, a validação e o acervo do projeto Narrativas.

### 1.2 Objetivos específicos (lista)

Lista com marcadores, cada item começando com **verbo no infinitivo**. Cada objetivo específico é um passo que, cumprido, leva ao objetivo geral, e cada um vai ser retomado na Conclusão. Os passos do seu trabalho são:

- o formato da planilha (as colunas e as regras);
- a catalogação das narrativas reais;
- a validação da planilha;
- a conversão para JSON;
- a descrição do catálogo construído.

Escolha o verbo certo para cada um (definir, catalogar, validar, converter, descrever...). Evite verbos vagos como "estudar" e "entender": eles não dizem o que foi entregue.

### Entrega

- [ ] Os 5 blocos da Introdução, com referências
- [ ] Objetivo geral em uma frase
- [ ] Objetivos específicos em lista, com verbos no infinitivo
- [ ] Referências usadas já listadas na seção Referências do documento
- [ ] Pelo menos 3 leituras fichadas em `docs/leituras.md`
- [ ] Versão nomeada e aviso no grupo

---

<a id="entrega-2"></a>
# Entrega 2 - Referencial Teórico e Metodologia (prazo: 03/12)

**Meta:** Referencial pronto até **segunda, 30/11**. Terça e quarta para a Metodologia, quinta para revisar.

## 2 REFERENCIAL TEÓRICO (5 a 6 páginas)

Releia a analogia do Referencial Teórico em [`docs/orientacoes_escrita_tcc.md`](orientacoes_escrita_tcc.md) e assista ao vídeo indicado lá. O Referencial explica os **conceitos** que o leitor precisa conhecer para entender o seu trabalho, sempre amarrados ao trabalho.

### 2.1 Narrativas populares e patrimônio cultural imaterial (cerca de 1 página)

- O que é patrimônio cultural imaterial (Convenção da UNESCO, 2003; IPHAN).
- O que são narrativas populares, e a diferença entre **lenda, mito, conto, causo e cordel**. São exatamente os valores da coluna `tipo` do seu catálogo, e as definições que você pesquisou para o `docs/formato_planilha.md` vêm para cá, com a referência (Cascudo, dicionários).
- Por que registrar: a memória coletiva e o risco de perda (BINDA e DA SILVA, 2026; PIRES, 2025).

### 2.2 Acervos digitais e metadados (cerca de 1,5 página)

- O que é um acervo digital e o que é **curadoria digital** (SAYÃO e SALES, 2012).
- O que são **metadados** ("dados sobre dados"): título, autor, data, assunto, fonte. Apresente o **Dublin Core** (DCMI) como padrão de metadados e mostre que várias colunas do seu catálogo correspondem a elementos dele (`titulo` a *title*, `fonte` a *source*, `licenca` a *rights*, `palavras_chave` a *subject*, `municipio` a *coverage*). Uma tabela com essa correspondência fica muito boa aqui.
- Os princípios **FAIR** (WILKINSON *et al.*, 2016): dados localizáveis, acessíveis, interoperáveis e reutilizáveis. Explique em um parágrafo e diga como o seu catálogo se aproxima deles (formato aberto, documentado, com fonte e licença).
- Os **direitos autorais** e o domínio público, com a **Lei nº 9.610/1998** (http://www.planalto.gov.br/ccivil_03/leis/l9610.htm). Leia os artigos na fonte oficial e explique, com as suas palavras e citando a lei:
  - o **art. 41**: quando uma obra entra em domínio público (70 anos contados de 1º de janeiro do ano seguinte ao da morte do autor);
  - o **art. 46, inciso III**: a citação de passagens de uma obra, para fins de estudo, crítica ou polêmica, na medida justificada para o fim a atingir, com o nome do autor e a origem da obra, não ofende os direitos autorais;
  - a consequência para um acervo digital: indicar a fonte **não** autoriza copiar a obra inteira; citar trechos curtos, com a fonte, é permitido.

  Use a citação direta da lei quando reproduzir as palavras dela (entre aspas, com a indicação do artigo) e coloque a lei nas Referências, no formato de legislação da NBR 6023:2018 (BRASIL. Lei nº 9.610, de 19 de fevereiro de 1998...).

### 2.3 Formatos de dados: CSV e JSON (cerca de 1 página)

- O que é o **CSV** (SHAFRANOVICH, 2005): uma linha por registro, campos separados por vírgula, cabeçalho. Mostre um trecho pequeno de CSV como figura ou quadro.
- O que é o **JSON** (BRAY, 2017): objetos com chave e valor, listas, tipos (texto, número, nulo). Mostre um trecho pequeno de JSON.
- Por que os dois: o CSV é fácil de preencher em planilha por qualquer pessoa; o JSON guarda os **tipos** (número, lista, nulo) e é o formato que sistemas web usam para trocar e carregar dados. É isso que justifica a conversão do catálogo para JSON.

### 2.4 Qualidade de dados e validação (cerca de 1,5 página)

- O que é qualidade de dados: dados "adequados para o uso" de quem vai usá-los (WANG e STRONG, 1996; BATINI e SCANNAPIECO, 2006).
- As **dimensões** que o seu validador confere, uma por parágrafo curto, cada uma ligada a uma regra:
  - **completude**: o dado está preenchido (campo obrigatório vazio);
  - **validade** ou conformidade: o dado obedece ao formato e ao domínio (número inteiro, faixa de ano, valor dentro da lista);
  - **unicidade**: cada registro aparece uma vez só (`id` repetido).
- **Validação automática** e **dados de teste**: por que testar um programa com dados em que o erro é conhecido de antemão (MYERS; BADGETT; SANDLER, 2011). É isso que justifica o gerador de dados fictícios do seu trabalho. Para "dados sintéticos", procure no Google Acadêmico `"dados sintéticos" teste de software` e `"synthetic data" "software testing"` e use um artigo que você tenha lido.

### 2.5 Trabalhos relacionados (cerca de 1 página)

Apresente **2 ou 3 iniciativas** de acervo digital de cultura ou memória, uma por parágrafo: o que é, como organiza os itens (que metadados usa) e o que o seu trabalho tem de parecido e de diferente. Sugestões para pesquisar:

- o **Tainacan** (https://tainacan.org), plataforma brasileira para acervos digitais de museus e instituições culturais;
- o **Museu da Pessoa** (https://museudapessoa.org), acervo de histórias de vida;
- a **Brasiliana Guita e José Mindlin** (https://digital.bbm.usp.br), biblioteca digital;
- um trabalho acadêmico sobre acervo digital de narrativas ou de cultura popular que você encontrar no Google Acadêmico ou no repositório da UFRN.

Para cada um, cite um artigo ou a página oficial com data de acesso. Feche a seção com um parágrafo dizendo o que nenhum deles resolve para o projeto Narrativas: um conjunto de dados de narrativas **do RN**, no formato que a **plataforma do projeto** vai usar.

## 3 METODOLOGIA (3 a 4 páginas)

### 3.1 Classificação da pesquisa (1 parágrafo)

Classifique a pesquisa com GIL (consulte a edição da biblioteca), como explica a seção "Classificação da pesquisa" de [`docs/orientacoes_escrita_tcc.md`](orientacoes_escrita_tcc.md):

- **quanto à natureza:** aplicada (resolve um problema concreto do projeto);
- **quanto aos objetivos:** descritiva (descreve o catálogo construído);
- **quanto aos procedimentos:** bibliográfica (o Referencial) e documental (as fontes das narrativas).

Justifique cada classificação com uma frase sobre o **seu** trabalho, não só com o nome.

### 3.2 Etapas do trabalho (1 parágrafo + 1 figura)

As etapas, na ordem em que aconteceram: pesquisa bibliográfica; definição do formato; coleta e catalogação; desenvolvimento do validador; validação e correção da planilha; conversão para JSON; teste do validador com dados fictícios. Faça um **fluxograma** simples dessas etapas (no Google Desenhos, no draw.io, https://app.diagrams.net, ou no próprio Google Docs) e coloque como figura, com legenda em cima e fonte embaixo ("Fonte: elaborado pelo autor (2026)").

Diga também como o trabalho foi organizado: 3 *sprints* de uma semana, repositório no GitHub com revisão por *pull request*, e a divisão de tarefas com os dois colegas.

### 3.3 Materiais e métodos (2 a 3 páginas)

Releia a seção "Materiais e Métodos" de [`docs/orientacoes_escrita_tcc.md`](orientacoes_escrita_tcc.md), com a analogia da receita de bolo: o leitor precisa conseguir **repetir** o que você fez.

**Materiais.** Um quadro com o que foi usado e para quê: Python (versão: rode `python --version`), módulos `csv`, `json`, `collections`, `random` e `sys`, `matplotlib` (versão: está no `requirements.txt`), Google Planilhas, VS Code, Git e GitHub, a API de localidades do IBGE.

**Métodos.** Um parágrafo (ou subtítulo sem número, em negrito) para cada parte:

- **definição do formato:** de onde vieram as colunas (o protótipo da plataforma, os metadados Dublin Core), as listas de valores e as regras. O formato completo vai no **Apêndice A** (é o seu `docs/formato_planilha.md`); aqui você resume e aponta para ele;
- **coleta e catalogação:** quais fontes foram consultadas (a tabela do `docs/fontes_consultadas.md`, resumida), o **critério para uma narrativa entrar** (fonte citável e município do RN), como a mesorregião foi conferida no IBGE e **como os trechos foram registrados**: de 2 a 3 por narrativa, de 1 a 3 linhas cada, copiados sem alteração da fonte original, entre aspas, separados por ` | `, com os cortes marcados com `[...]`. Em seguida, **justifique a escolha com a lei**: o catálogo registra trechos curtos, e não o texto integral nem um resumo, porque a citação de passagens é permitida pelo art. 46, inciso III, da Lei nº 9.610/1998, desde que se indiquem o autor e a origem da obra, o que a coluna `fonte` garante; o texto integral só poderá ser incluído para as obras em domínio público (art. 41) ou com autorização. Explique também por que a coluna se chama `texto`: ela foi preparada para receber o texto completo no futuro;
- **validação:** as regras do seu validador e os códigos de erro (a tabela de erros do formato). Diga que a planilha real foi validada **antes** de qualquer correção, e por que o validador roda antes do conversor;
- **conversão:** o que o conversor do colega faz com cada tipo de coluna (inteiro, lista, nulo) e como o verificador confere o resultado;
- **teste com dados fictícios:** como o gerador do colega cria narrativas fictícias, insere erros de propósito em cerca de 10% das linhas e grava o gabarito, e como você comparou o gabarito com o relatório do validador;
- **estatísticas:** quais contagens foram feitas.

### Entrega

- [ ] Referencial com as seções 2.1 a 2.5, com referências em todas
- [ ] Metodologia com 3.1, 3.2 (com o fluxograma) e 3.3
- [ ] Lei nº 9.610/1998 (arts. 41 e 46, III) explicada na seção 2.2, usada como justificativa do registro de trechos na seção 3.3 e listada nas Referências
- [ ] Todas as leituras fichadas em `docs/leituras.md`
- [ ] Comentários da Entrega 1 resolvidos
- [ ] Versão nomeada e aviso no grupo

---

<a id="entrega-3"></a>
# Entrega 3 - Resultados (prazo: 08/12)

Releia a seção "Resultados" de [`docs/orientacoes_escrita_tcc.md`](orientacoes_escrita_tcc.md). A regra principal: **cada tabela e cada figura são apresentadas no texto antes de aparecerem e comentadas depois.**

**O que os Resultados são, no seu trabalho:** um **relato do que você produziu** no projeto, com os números que saíram dos programas. Não é preciso análise estatística, comparação com outros trabalhos nem conclusões gerais. Para cada parte, diga o que foi feito, mostre o resultado (um número, uma tabela, uma figura) e comente em 2 ou 3 frases.

Tudo o que você precisa está em `resultados/`: o `resumo.md`, o `estatisticas.txt`, os gráficos e os relatórios de erros, além dos prints em `docs/evidencias/`.

### 4.1 O formato da planilha (meia página)

O formato final, em um quadro resumido (coluna, obrigatória, tipo), apontando para o Apêndice A. Comente em poucas frases uma ou duas decisões (por exemplo, por que `mesorregiao` é uma lista e `municipio` é texto livre).

### 4.2 O catálogo construído (1 página)

- Quantas narrativas, de quantos municípios e de quantas fontes diferentes.
- Os 2 gráficos (por **tipo** e por **mesorregião**), cada um com legenda e um comentário curto: qual tipo apareceu mais, e qual mesorregião ficou com menos narrativas (se uma região ficou com poucas, diga isso: é uma informação útil para o projeto).

### 4.3 A validação da planilha (meia página a 1 página)

- Quantos erros o seu validador encontrou na planilha real **antes da correção**, e quais (uma tabela pequena ou uma frase), e que depois da correção ficaram 0. Os prints do validador antes e depois podem ser figuras.
- O teste com as bases fictícias do gerador: em uma frase ou uma tabela pequena, quantos erros o gerador inseriu nas bases de 100 e de 1.000 narrativas e quantos o validador encontrou. Se tiver aparecido alguma diferença, conte o que era e o que foi corrigido.

### 4.4 O catálogo em JSON (meia página)

O catálogo convertido para JSON pelo conversor do colega e conferido pelo verificador dele (`Diferenças: 0`). Uma figura com uma narrativa no CSV ao lado da mesma narrativa no JSON mostra o resultado melhor que um parágrafo.

### 4.5 Limitações (1 parágrafo)

O catálogo tem 20 narrativas (é uma amostra, não o acervo do RN); cada narrativa está representada só por trechos curtos; a classificação de `tipo` e de `publico` foi feita por uma pessoa só; o validador não confere a coluna `texto` (os trechos e as aspas) nem se o município existe.

### Entrega

- [ ] Seções 4.1 a 4.5
- [ ] Todas as tabelas e figuras com legenda em cima, fonte embaixo, citadas no texto antes de aparecer
- [ ] Os números do texto conferem com os arquivos de `resultados/`
- [ ] Comentários da Entrega 2 resolvidos
- [ ] Versão nomeada e aviso no grupo

---

<a id="entrega-4"></a>
# Entrega 4 - Conclusão, Resumo, Título e revisão final (prazo: 10/12)

### 5 CONCLUSÃO (até quarta, 09/12; 1 a 2 páginas)

Releia a seção "Conclusão" de [`docs/orientacoes_escrita_tcc.md`](orientacoes_escrita_tcc.md). A Conclusão **não traz informação nova** e **não tem citação**. Ela:

1. retoma o problema e a pergunta do trabalho em um parágrafo;
2. retoma **cada objetivo específico**, na ordem, dizendo como foi cumprido e qual o resultado principal (um parágrafo curto para cada, ou um parágrafo para todos);
3. responde à pergunta, com base no que foi feito;
4. diz qual a contribuição para o projeto Narrativas (o primeiro conjunto de dados do acervo, o formato documentado e os programas que outros trabalhos podem usar);
5. aponta os **trabalhos futuros**: carregar o JSON no banco da plataforma quando o cadastro de narrativas existir; ampliar o catálogo para as mesorregiões com menos registros; incluir o texto integral das narrativas em domínio público; conferir no validador a coluna `texto`, o município e a mesorregião (com a lista do IBGE); uma tela de cadastro na própria plataforma que use as mesmas regras do validador.

O seu `docs/diario.md` ajuda aqui: o que deu errado e o que você aprendeu em cada sprint.

### Revisão da Introdução e dos Objetivos (quarta, 09/12)

Releia a Introdução e os Objetivos **depois** de escrever a Conclusão. Tudo o que a Introdução promete tem de estar nos Resultados, e todo objetivo específico tem de ter sido retomado na Conclusão. Se algo mudou no caminho (por exemplo, o catálogo ficou com 18 narrativas), ajuste a Introdução.

### Resumo e *Abstract* (quinta, 10/12)

Releia a seção "Resumo" de [`docs/orientacoes_escrita_tcc.md`](orientacoes_escrita_tcc.md) (NBR 6028:2021): parágrafo único, de 150 a 500 palavras, com contexto, objetivo, método, resultados principais (com números) e conclusão. Depois, as palavras-chave (de 3 a 5, separadas por ponto e vírgula). O *Abstract* é a tradução do Resumo para o inglês; revise a tradução com cuidado, termo técnico por termo técnico.

### Título (quinta, 10/12)

O título é a última coisa a ser definida. Ele precisa dizer **o que** foi feito e **sobre o quê**, sem ser longo. Releia a seção "Título do trabalho" de [`docs/orientacoes_escrita_tcc.md`](orientacoes_escrita_tcc.md). Título provisório, para você melhorar: *Construção de um conjunto de dados estruturado de narrativas populares do Rio Grande do Norte para um acervo digital*.

### Apêndices

- **Apêndice A - Dicionário de dados da planilha:** o conteúdo do `docs/formato_planilha.md`, formatado como quadro.
- **Apêndice B - Narrativas catalogadas:** um quadro com `id`, título, município e fonte (abreviada) das narrativas. Sem os trechos, para não ficar longo.

### Revisão final

- [ ] Sumário atualizado e com a numeração das seções certa
- [ ] Toda citação do texto está nas Referências, e toda referência foi citada no texto
- [ ] Referências em ordem alfabética, no formato da NBR 6023:2018
- [ ] Toda figura e tabela com legenda em cima, fonte embaixo e chamada no texto
- [ ] Nenhuma frase copiada de fonte sem aspas e referência
- [ ] Os números do Resumo, dos Resultados e da Conclusão são os mesmos
- [ ] Todos os comentários resolvidos
- [ ] Versão nomeada `Entrega 4 - Versão final - 10/12` e aviso no grupo

---

<a id="referencias"></a>
## 5. Referências por onde começar

**Abra e leia cada uma antes de citar.** Confira os dados (autor, título, ano, páginas, edição) **no original**: as referências abaixo são o ponto de partida da busca, e a forma final na sua lista é responsabilidade sua.

**Do projeto Narrativas** (as referências completas estão em [`docs/projeto_narrativas.md`](projeto_narrativas.md)):

- BEZERRA *et al.* (2026), saberes e narrativas;
- BINDA e DA SILVA (2026), preservação do patrimônio imaterial;
- DOS SANTOS FERNANDES e MARTINS (2026), pesquisa em cultura popular;
- PIRES (2025), patrimônio cultural;
- REIS (2023), humanidades digitais.

**Patrimônio e narrativas:**

- UNESCO. *Convenção para a Salvaguarda do Patrimônio Cultural Imaterial*. Paris, 2003. A versão em português está no portal do IPHAN (http://portal.iphan.gov.br, busque "Convenção para a Salvaguarda").
- CASCUDO, Luís da Câmara. *Dicionário do folclore brasileiro*. Use a edição da biblioteca e anote editora e ano dela.
- BRASIL. Lei nº 9.610, de 19 de fevereiro de 1998 (Lei de Direitos Autorais), arts. 41 e 46. http://www.planalto.gov.br/ccivil_03/leis/l9610.htm. **Obrigatória:** é ela que justifica o registro de trechos curtos no catálogo.

**Acervos digitais e metadados:**

- SAYÃO, Luis Fernando; SALES, Luana Farias. Curadoria digital: um novo patamar para preservação de dados digitais de pesquisa. *Informação & Sociedade: Estudos*, 2012. Busque o título no Google Acadêmico.
- DCMI (Dublin Core Metadata Initiative). *Dublin Core Metadata Element Set*. https://www.dublincore.org/specifications/dublin-core/dces/
- WILKINSON, Mark D. *et al.* The FAIR Guiding Principles for scientific data management and stewardship. *Scientific Data*, v. 3, 2016. Acesso aberto: busque o título no Google Acadêmico.

**Formatos de dados:**

- SHAFRANOVICH, Y. *RFC 4180: Common Format and MIME Type for Comma-Separated Values (CSV) Files*. 2005. https://www.rfc-editor.org/rfc/rfc4180
- BRAY, T. (ed.). *RFC 8259: The JavaScript Object Notation (JSON) Data Interchange Format*. 2017. https://www.rfc-editor.org/rfc/rfc8259

**Qualidade de dados e testes:**

- WANG, Richard Y.; STRONG, Diane M. Beyond accuracy: what data quality means to data consumers. *Journal of Management Information Systems*, v. 12, n. 4, 1996. Pelo Portal de Periódicos CAPES.
- BATINI, Carlo; SCANNAPIECO, Monica. *Data quality: concepts, methodologies and techniques*. Springer, 2006. Pelo Portal de Periódicos CAPES (Springer).
- MYERS, Glenford J.; BADGETT, Tom; SANDLER, Corey. *The art of software testing*. 3. ed. Wiley, 2011.

**Metodologia:**

- GIL, Antonio Carlos. *Como elaborar projetos de pesquisa*. Atlas. Use a edição da biblioteca.

**Ferramentas e dados (para Materiais, não para conceito):**

- IBGE. API de localidades. https://servicodados.ibge.gov.br/api/docs/localidades
- PYTHON SOFTWARE FOUNDATION. Documentação do Python: módulos `csv` e `json`. https://docs.python.org/pt-br/3/

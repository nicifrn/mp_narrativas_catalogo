# Catálogo estruturado de narrativas populares do RN

Conjunto de dados de narrativas populares do Rio Grande do Norte (lendas, contos, causos, mitos e cordéis) para o acervo do projeto **Narrativas** (NIC/IFRN). O resultado é uma planilha com narrativas reais, de fontes citáveis, convertida para JSON, com o formato documentado e ferramentas que conferem a qualidade dos dados.

**Orientador:** Prof. Bruno Gomes (@brunogomesifrn) - NIC/IFRN

**Período:** 23/11/2026 a 10/12/2026, em 3 sprints

---

## A equipe e as tarefas

Três alunos trabalham em paralelo. O que liga o trabalho dos três é o **formato da planilha**: o Ítalo preenche esse formato, o Aluno 1 confere esse formato e o Aluno 2 gera dados nesse formato. O formato está fechado desde o início, então **ninguém espera por ninguém**.

| Quem | O que faz | Plano de trabalho |
|---|---|---|
| **Ítalo** (@italogomees) | Define o formato da planilha, preenche com narrativas reais do RN, converte para JSON, gera as estatísticas, integra o trabalho dos colegas e escreve o RCC | [Plano de desenvolvimento](docs/01_italo_v2_narrativas_desenvolvimento.md) · [Plano de escrita do RCC](docs/01_italo_v2_narrativas_escrita.md) |
| **Aluno 1** (@aluno1) | Programa o validador da planilha (`scripts/validar.py`): campos vazios, números inválidos, `id` repetido, valores fora da lista | [Plano do Aluno 1](docs/01_italo_v2_aluno_1.md) |
| **Aluno 2** (@aluno2) | Programa o gerador de narrativas fictícias (`scripts/gerar_fake.py`), com opção de inserir erros de propósito para testar o validador | [Plano do Aluno 2](docs/01_italo_v2_aluno_2.md) |

**Cada um mexe só nos seus arquivos.** No final, integrar é **rodar** os programas em sequência, e não juntar código.

> **Comece por aqui:** leia o **seu** plano inteiro na segunda, 23/11, antes de começar. Ele tem o que programar, em que ordem, com quais comandos e onde pesquisar. As *issues* do GitHub resumem cada sprint; se uma *issue* e o plano parecerem dizer coisas diferentes, **vale o plano**.

## Cronograma resumido

| Sprint | Período | Ítalo | Aluno 1 | Aluno 2 |
|---|---|---|---|---|
| 1 | 23/11 a 26/11 | Formato documentado e estrutura do repositório (**PR até 24/11**); 10 primeiras narrativas | Ambiente, arquivo de teste e primeira versão do validador | Ambiente e gerador de narrativas corretas |
| 2 | 27/11 a 03/12 | 20 narrativas, `converter.py` e `estatisticas.py` | Validador completo (**entrega: 03/12**) | Erros de propósito e gabarito (**entrega: 03/12**) |
| 3 | 04/12 a 10/12 | Integração (04/12), `comparar.py`, README final; Resultados, Conclusão, Resumo e Título | Ajustes apontados pelo Ítalo | Ajustes apontados pelo Ítalo |

Os detalhes e as datas de cada entrega estão nos planos.

## Documentos de apoio

- [Projeto Narrativas](docs/projeto_narrativas.md): resumo do projeto pai.
- [Orientações de escrita do TCC](docs/orientacoes_escrita_tcc.md): estrutura, citações, referências, figuras e tabelas (ABNT). Vale para o RCC do Ítalo.
- [Protótipos da plataforma](docs/prototipos/): telas do portal. A tela [`narrativa_detalhes.png`](docs/prototipos/narrativa_detalhes.png) mostra os campos de onde vem a maior parte das colunas da planilha.

## Como trabalhar no repositório

- A *branch* padrão é a `develop`. Cada aluno cria a sua `feature/...` a partir dela e abre um *pull request* (PR) para a `develop` ao final de cada sprint.
- Ninguém faz *commit* direto na `main` nem na `develop`: tudo entra por PR, revisado pelo orientador.
- No PR, preencha o modelo (objetivo, o que foi feito, como testar) e escreva `Closes #N` com o número da sua *issue*.

O passo a passo completo (comandos, mensagens de *commit*, o que fazer quando travar) está na seção "Como trabalhar no repositório" de cada plano.

## Estrutura do repositório

As pastas `dados/`, `scripts/` e `resultados/` são criadas pelo Ítalo na Sprint 1. Ao final, o repositório fica assim:

```
mp_narrativas_catalogo/
├── .github/pull_request_template.md
├── dados/          ← modelo.csv, narrativas.csv, narrativas.json, teste_validador.csv
├── scripts/        ← validar.py, gerar_fake.py, converter.py, estatisticas.py, comparar.py
├── resultados/     ← gráficos, tabelas e relatórios de erros
├── docs/           ← planos de trabalho, formato da planilha e documentos de apoio
├── .gitignore
├── requirements.txt
└── README.md
```

## Como rodar

*(O Ítalo completa esta seção na Sprint 3 com o passo a passo para gerar todas as saídas do zero.)*

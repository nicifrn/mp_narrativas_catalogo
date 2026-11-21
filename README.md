# Catálogo estruturado de narrativas populares do RN

Conjunto de dados de narrativas populares do Rio Grande do Norte (lendas, contos, causos, mitos e cordéis) para o acervo do projeto **Narrativas** (NIC/IFRN). O resultado é uma planilha com narrativas reais, de fontes citáveis, conferida por um validador e convertida para JSON, com o formato documentado.

**Orientador:** Prof. Bruno Gomes (@brunogomesifrn) - NIC/IFRN

**Período:** 23/11/2026 a 10/12/2026, em 3 sprints

---

## A equipe e as tarefas

Três alunos trabalham em paralelo. O que liga o trabalho dos três é o **formato da planilha**: o Ítalo preenche e valida esse formato, o Samuel converte esse formato para JSON e o Gleidson gera dados fictícios nesse formato. O formato está fechado desde o início, então **ninguém espera por ninguém**.

| Quem | O que faz | Plano de trabalho |
|---|---|---|
| **Ítalo** (@italogomees) | Define o formato da planilha, preenche com narrativas reais do RN, programa o validador da planilha (`scripts/validar.py`) e as estatísticas, integra o trabalho dos colegas e escreve o RCC | [Plano de desenvolvimento](docs/01_italo_v2_narrativas_desenvolvimento.md) · [Plano de escrita do RCC](docs/01_italo_v2_narrativas_escrita.md) |
| **Samuel** (@samuelmarinho10) | Programa o conversor de CSV para JSON (`scripts/converter.py`) e o verificador, que confere se o JSON saiu igual ao CSV (`scripts/verificar_json.py`) | [Plano do Samuel](docs/01_italo_v2_aluno_1.md) |
| **Gleidson** (@gleidsonxsz) | Programa o gerador de narrativas fictícias (`scripts/gerar_fake.py`), com opção de inserir erros de propósito para testar o validador | [Plano do Gleidson](docs/01_italo_v2_aluno_2.md) |

**Cada um mexe só nos seus arquivos.** No final, integrar é **rodar** os programas em sequência, e não juntar código.

> **Comece por aqui:** leia o **seu** plano inteiro na segunda, 23/11, antes de começar. **Não há *issues*: o plano é o seu roteiro.** Ele tem o que programar, em que ordem, com quais comandos e onde pesquisar. Siga as sprints na ordem e marque as caixas da "Entrega da sprint" à medida que for terminando.

## Cronograma resumido

| Sprint | Período | Ítalo | Samuel | Gleidson |
|---|---|---|---|---|
| 1 | 23/11 a 26/11 | Formato documentado e estrutura do repositório (**PR até 24/11**); 10 primeiras narrativas | Arquivo de teste e primeira versão do conversor (**PR até 26/11**) | Gerador de narrativas corretas (**PR até 26/11**) |
| 2 | 27/11 a 03/12 | 20 narrativas, `validar.py` e `estatisticas.py` (**PR até 03/12**) | Conversor completo e verificador (**PR até 03/12**) | Erros de propósito e gabarito (**PR até 03/12**) |
| 3 | 04/12 a 10/12 | Integração (04/12), `resumo.md` e README final (**PR até 07/12**); Resultados, Conclusão, Resumo e Título | Ajustes pedidos depois da integração | Ajustes pedidos depois da integração |

Os detalhes e as datas de cada entrega estão nos planos.

## Documentos de apoio

- [Projeto Narrativas](docs/projeto_narrativas.md): resumo do projeto pai.
- [Orientações de escrita do TCC](docs/orientacoes_escrita_tcc.md): estrutura, citações, referências, figuras e tabelas (ABNT). Vale para o RCC do Ítalo.
- [Protótipos da plataforma](docs/prototipos/): telas do portal. A tela [`narrativa_detalhes.png`](docs/prototipos/narrativa_detalhes.png) mostra os campos de onde vem a maior parte das colunas da planilha.

## Como trabalhar no repositório

- A *branch* padrão é a `develop`. Cada aluno cria a sua `feature/...` a partir dela e abre um *pull request* (PR) para a `develop` ao final de cada sprint.
- Ninguém faz *commit* direto na `main` nem na `develop`: tudo entra por PR, revisado pelo orientador.
- No PR, preencha o modelo (sprint, objetivo, o que foi feito, como testar) e avise no grupo da equipe.
- Dúvidas, travamentos e pedidos de ajuste vão para o grupo da equipe.

O passo a passo completo (comandos, mensagens de *commit*, o que fazer quando travar) está na seção "Como trabalhar no repositório" de cada plano.

## Estrutura do repositório

As pastas `dados/`, `scripts/` e `resultados/` são criadas pelo Ítalo na Sprint 1. Ao final, o repositório fica assim:

```
mp_narrativas_catalogo/
├── .github/pull_request_template.md
├── dados/          ← modelo.csv, narrativas.csv, narrativas.json e os arquivos de teste
├── scripts/        ← validar.py, estatisticas.py, converter.py, verificar_json.py, gerar_fake.py
├── resultados/     ← gráficos, estatísticas, relatórios de erros e resumo
├── docs/           ← planos de trabalho, formato da planilha e documentos de apoio
├── .gitignore
├── requirements.txt
└── README.md
```

## Como rodar

*(O Ítalo completa esta seção na Sprint 3 com o passo a passo para gerar todas as saídas do zero.)*


# Diário de desenvolvimento

## Sprint 1 — 23/11/2026 a 26/11/2026

### Objetivo

Definir e documentar o formato do catálogo de narrativas populares do Rio Grande do Norte, organizar o ambiente de desenvolvimento e realizar a coleta das 10 primeiras narrativas reais.

### Atividades realizadas

- Instalação e configuração do Git e do Python.
- Clonagem do repositório do projeto.
- Criação da branch `feature/formato-planilha`.
- Configuração do ambiente virtual Python (`.venv`).
- Instalação da biblioteca Matplotlib.
- Organização das pastas `dados`, `docs`, `scripts` e `resultados`.
- Criação dos arquivos `.gitignore` e `requirements.txt`.
- Análise dos protótipos da plataforma.
- Definição das 12 colunas do catálogo.
- Documentação da estrutura em `docs/formato_planilha.md`.
- Atualização do README.md.
- Criação da planilha no Google Planilhas.
- Configuração dos menus suspensos nas colunas `tipo`, `publico`, `mesorregiao` e `licenca`.
- Criação do arquivo `dados/modelo.csv` com três narrativas reais.
- Realização de commits e envio das alterações ao GitHub.
- Pesquisa e cadastramento das 10 primeiras narrativas.
- Criação do arquivo `docs/fontes_consultadas.md`.
- Teste de leitura do arquivo `dados/modelo.csv` utilizando o módulo `csv` do Python.
- Registro da evidência do teste em `docs/evidencias/s1_leitura_modelo_csv.png`.

### Decisões tomadas

- Utilizar o formato CSV para armazenar os dados do catálogo.
- Utilizar menus suspensos para padronizar os valores e reduzir erros de digitação.
- Separar as palavras-chave por ponto e vírgula.
- Utilizar trechos curtos das narrativas, acompanhados de referências bibliográficas.
- Classificar como `desconhecida` a licença das fontes cuja licença não foi identificada.
- Manter o arquivo `modelo.csv` com apenas três narrativas, conforme o plano de desenvolvimento.
- Priorizar narrativas de diferentes municípios e mesorregiões.
- Descartar a Lenda do Poço de Sant'Ana por possível duplicidade com a Lenda do Vaqueiro de Caicó.

### Dificuldades encontradas e soluções adotadas

| Dificuldade | Solução |
|---|---|
| Bloqueio da ativação do ambiente virtual pelo PowerShell. | Alteração temporária da política de execução para a sessão do terminal. |
| Textos extensos prejudicando a visualização da planilha. | Configuração do ajuste de texto para cortar o conteúdo visualmente, sem excluir os dados. |
| Dificuldade para identificar as licenças de algumas fontes. | Utilização do valor `desconhecida`. |
| Possibilidade de duplicidade entre narrativas. | Substituição de uma narrativa por outra de um município diferente. |
| Dificuldade para localizar referências bibliográficas completas. | Pesquisa em repositórios acadêmicos, publicações institucionais e portais culturais. |

### Resultados alcançados

- 12 colunas definidas e documentadas.
- 4 colunas com menus suspensos.
- 3 narrativas reais no arquivo modelo.csv.
- 10 narrativas cadastradas no Google Planilhas.
- 8 municípios contemplados.
- 4 mesorregiões contempladas.
- 10 fontes registradas, sendo 8 aproveitadas.
- Leitura bem-sucedida das três narrativas do modelo.csv, com acentuação correta e sem erros de execução.

#### Distribuição por mesorregião

| Mesorregião | Quantidade |
|---|---:|
| Leste | 5 |
| Central | 2 |
| Oeste | 2 |
| Agreste | 1 |
| Total | 10 |

### Pendências

- Conferir os trechos e as referências bibliográficas nas fontes.
- Compartilhar a planilha com o orientador.
- Realizar o commit da documentação final da Sprint 1.
- Abrir o Pull Request para a branch develop.

### Próximos passos — Sprint 2

- Ampliar o catálogo para 20 narrativas reais.
- Diversificar os tipos de narrativas cadastradas.
- Exportar o catálogo para `dados/narrativas.csv`.
- Desenvolver o script `scripts/validar.py`.
- Desenvolver o script `scripts/estatisticas.py`.
- Gerar gráficos e relatórios sobre os dados coletados.

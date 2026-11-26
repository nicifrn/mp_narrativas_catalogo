
# Formato da planilha de narrativas

Este documento apresenta a estrutura e as regras de preenchimento do catálogo de narrativas populares do Rio Grande do Norte, desenvolvido para o projeto Narrativas.


## Relação com os protótipos da plataforma

A estrutura da planilha foi definida considerando
as necessidades do projeto Narrativas e os
protótipos disponíveis no repositório.

Foram analisados os seguintes protótipos:

- `index.png`: página inicial, com busca por
  palavras-chave, tipo e região.
- `narrativas.png`: catálogo com filtros por
  tipo, público-alvo, região e palavras-chave.
- `narrativa_detalhes.png`: página de detalhes,
  com informações sobre o conteúdo, a localização,
  o público-alvo e as fontes da narrativa.

As 12 colunas foram mantidas por atenderem ao
escopo inicial do catálogo. Recursos como imagens,
áudios, avaliações e comentários não fazem parte
desta etapa do desenvolvimento.

## Arquivo

- Formato: CSV (Comma-Separated Values).
- Codificação: UTF-8.
- Separador de colunas: vírgula.
- A primeira linha contém o cabeçalho.
- A primeira narrativa começa na linha 2.
- Cada linha representa uma narrativa.
- Os campos opcionais sem informação devem permanecer vazios.
- Os nomes e a ordem das colunas devem ser mantidos.

## Colunas

| # | Coluna | Obrigatória | Tipo | Regra | Por que existe |
|---|---|---|---|---|---|
| 1 | id | Sim | Inteiro | Número único e sequencial, sem repetição. | Identifica cada narrativa sem depender do título. |
| 2 | titulo | Sim | Texto | Título da narrativa. | Permite identificar e localizar a narrativa no catálogo. |
| 3 | tipo | Sim | Lista | lenda, conto, causo, mito ou cordel. | Permite classificar e filtrar as narrativas por tipo. |
| 4 | publico | Sim | Lista | infantil, juvenil, adulto ou livre. | Indica o público ao qual a narrativa é destinada. |
| 5 | municipio | Sim | Texto | Nome do município do RN conforme o IBGE, com acentuação. | Identifica a localização geográfica associada à narrativa. |
| 6 | mesorregiao | Sim | Lista | oeste, central, agreste ou leste. | Permite organizar e filtrar as narrativas por região do estado. |
| 7 | texto | Sim | Texto | De 2 a 3 trechos curtos da fonte original, entre aspas e separados por barra vertical. | Apresenta parte do conteúdo original da narrativa, respeitando os direitos autorais. |
| 8 | palavras_chave | Não | Texto | Palavras separadas por ponto e vírgula. | Facilita a busca por assuntos, personagens e temas. |
| 9 | fonte | Sim | Texto | Referência bibliográfica conforme as normas da ABNT. | Identifica a origem das informações e permite sua conferência. |
| 10 | url_fonte | Não | Texto | Endereço eletrônico da fonte, quando disponível. | Facilita o acesso à fonte original. |
| 11 | ano_fonte | Não | Inteiro | Ano de publicação da fonte, entre 1500 e 2026. | Permite identificar o período de publicação da fonte consultada. |
| 12 | licenca | Sim | Lista | dominio_publico, cc_by, cc_by_sa, direitos_reservados ou desconhecida. | Registra as condições de utilização do conteúdo. |

## Listas de valores

Os valores das listas devem ser escritos em letras minúsculas, sem acentos e com sublinhado no lugar de espaços, quando necessário.

### tipo

- `lenda`: narrativa popular transmitida pela tradição, que pode misturar acontecimentos reais e elementos imaginários.
- `conto`: narrativa geralmente curta, com personagens e acontecimentos organizados em um enredo.
- `causo`: história popular, geralmente contada oralmente, que pode apresentar acontecimentos reais ou exagerados.
- `mito`: narrativa tradicional que procura explicar origens, fenômenos ou crenças de uma cultura.
- `cordel`: narrativa popular geralmente escrita em versos e tradicionalmente publicada em folhetos.

### publico

- `infantil`: narrativa destinada principalmente às crianças.
- `juvenil`: narrativa destinada principalmente aos adolescentes.
- `adulto`: narrativa destinada principalmente ao público adulto.
- `livre`: narrativa adequada a diferentes faixas etárias.

### mesorregiao

Classificação baseada nas mesorregiões geográficas do IBGE.

- `oeste`: Oeste Potiguar.
- `central`: Central Potiguar.
- `agreste`: Agreste Potiguar.
- `leste`: Leste Potiguar.

### licenca

- `dominio_publico`: obra que não está mais sujeita à proteção patrimonial dos direitos autorais ou que se encontra em domínio público por outra hipótese legal.
- `cc_by`: licença que permite compartilhar e adaptar a obra, desde que seja atribuído crédito ao autor.
- `cc_by_sa`: licença que permite compartilhar e adaptar a obra, exigindo atribuição ao autor e manutenção da mesma licença ou de licença compatível nas adaptações.
- `direitos_reservados`: obra protegida por direitos autorais, cuja utilização depende de autorização ou de uma exceção prevista em lei.
- `desconhecida`: situação em que não foi possível identificar a licença da obra.

## Regras de preenchimento

### Texto da narrativa

A coluna `texto` deve conter de 2 a 3 trechos curtos, copiados exatamente como aparecem na fonte original.

Cada trecho deve estar entre aspas e separado pelo caractere `|`, com um espaço de cada lado.

Exemplo ilustrativo:

    "Primeiro trecho da fonte." | "Segundo trecho da fonte."

O caractere `|` não deve aparecer dentro dos trechos.

A utilização de trechos curtos para fins de estudo é fundamentada no artigo 46, inciso III, da Lei nº 9.610/1998, respeitando a extensão justificada para a finalidade e a identificação do autor e da origem da obra.

### Palavras-chave

As palavras-chave devem ser separadas por ponto e vírgula.

Exemplo:

    lobisomem; sertão; lua cheia

### Campos opcionais

Quando não houver informação disponível para um campo opcional, a célula deverá permanecer vazia.

Não devem ser utilizados valores como `N/A`, `-` ou `sem informação`.

### Formatação do CSV

Campos que contêm vírgulas ou aspas devem seguir as regras de formatação do CSV. O Google Planilhas realiza esse tratamento automaticamente durante a exportação.

## Arquivos de erros

Os arquivos de erros produzidos pelo validador e pelo gerador de narrativas fictícias devem seguir o mesmo formato:

    linha,coluna,erro

Exemplo:

    linha,coluna,erro
    5,titulo,vazio
    9,ano_fonte,nao_inteiro
    12,tipo,fora_da_lista

### Códigos de erro

| Código | Descrição |
|---|---|
| vazio | Campo obrigatório sem preenchimento. |
| nao_inteiro | O campo id ou ano_fonte não contém um número inteiro. |
| fora_da_faixa | O ano da fonte é menor que 1500 ou maior que 2026. |
| fora_da_lista | O valor informado não pertence à lista de valores permitidos. |
| repetido | O identificador da narrativa já foi utilizado em outra linha. |

A numeração das linhas considera o cabeçalho como linha 1.

A regra dos trechos da coluna texto será conferida manualmente.


## Referências

- Dicionário Caldas Aulete.
  https://www.aulete.com.br/

- IBGE. Mesorregiões do Rio Grande do Norte.
  https://servicodados.ibge.gov.br/api/v1/localidades/estados/RN/mesorregioes

- IBGE. Municípios do Rio Grande do Norte.
  https://servicodados.ibge.gov.br/api/v1/localidades/estados/RN/municipios

- BRASIL. Lei nº 9.610, de 19 de fevereiro de 1998.
  https://www.planalto.gov.br/ccivil_03/leis/l9610.htm

- Creative Commons Brasil. Sobre as licenças.
  https://br.creativecommons.net/licencas/


import csv
import os
import random

COLUNAS = ["id", "titulo", "tipo", "publico", "municipio", "mesorregiao",
           "texto", "palavras_chave", "fonte", "url_fonte", "ano_fonte", "licenca"]

TIPOS = ["lenda", "conto", "causo", "mito", "cordel"]
PUBLICOS = ["infantil", "juvenil", "adulto", "livre"]
LICENCAS = ["dominio_publico", "cc_by", "cc_by_sa",
            "direitos_reservados", "desconhecida"]

MUNICIPIOS = {
    "Natal": "leste",
    "Parnamirim": "leste",
    "Ceará-Mirim": "leste",
    "Macaíba": "leste",
    "Mossoró": "oeste",
    "Pau dos Ferros": "oeste",
    "Apodi": "oeste",
    "Assú": "oeste",
    "Caicó": "central",
    "Currais Novos": "central",
    "Macau": "central",
    "Angicos": "central",
    "Santa Cruz": "agreste",
    "Nova Cruz": "agreste",
    "João Câmara": "agreste",
}

SERES = ["do Lobisomem", "da Mula sem Cabeça", "do Boi Tatá", "da Cobra Grande",
         "do Vaqueiro Encantado", "da Moça da Pedra"]

PALAVRAS = ["sertão", "assombração", "lua cheia",
            "vaqueiro", "rio", "encantamento"]


def gerar_narrativa(numero):
    tipo = random.choice(TIPOS)
    municipio = random.choice(list(MUNICIPIOS.keys()))
    ser = random.choice(SERES)

    # de 2 a 3 trechos, cada um entre aspas, separados por " | "
    quantidade = random.randint(2, 3)
    trechos = []
    for i in range(1, quantidade + 1):
        trechos.append(f'"Trecho fictício {i} da narrativa {numero}."')
    texto = " | ".join(trechos)

    # de 1 a 3 palavras-chave, separadas por "; "
    palavras = random.sample(PALAVRAS, random.randint(1, 3))
    palavras_chave = "; ".join(palavras)

    # metade das vezes sem link
    if random.random() < 0.5:
        url_fonte = ""
    else:
        url_fonte = f"https://exemplo.com/narrativa/{numero}"

    # de vez em quando sem ano
    if random.random() < 0.2:
        ano_fonte = ""
    else:
        ano_fonte = random.randint(1900, 2026)

    return {
        "id": numero,
        "titulo": f"{tipo.capitalize()} {ser} de {municipio}",
        "tipo": tipo,
        "publico": random.choice(PUBLICOS),
        "municipio": municipio,
        "mesorregiao": MUNICIPIOS[municipio],
        "texto": texto,
        "palavras_chave": palavras_chave,
        "fonte": f"Fonte fictícia número {numero}.",
        "url_fonte": url_fonte,
        "ano_fonte": ano_fonte,
        "licenca": random.choice(LICENCAS),
    }


QUANTIDADE = 20

narrativas = []
for numero in range(1, QUANTIDADE + 1):
    narrativas.append(gerar_narrativa(numero))

os.makedirs("dados/fake", exist_ok=True)
caminho = "dados/fake/fake_20.csv"

with open(caminho, "w", encoding="utf-8", newline="") as arquivo:
    escritor = csv.DictWriter(arquivo, fieldnames=COLUNAS)
    escritor.writeheader()
    for narrativa in narrativas:
        escritor.writerow(narrativa)

print(f"Narrativas geradas: {QUANTIDADE}")
print(f"Planilha: {caminho}")


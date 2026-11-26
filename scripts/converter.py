import csv
import json
import sys


def ler_csv(caminho):
    narrativas = []
    with open(caminho, encoding="utf-8") as arquivo:
        for linha in csv.DictReader(arquivo):
            limpa = {coluna: valor.strip() for coluna, valor in linha.items()}
            narrativas.append(limpa)
    return narrativas


def gravar_json(narrativas, caminho):
    with open(caminho, "w", encoding="utf-8") as arquivo:
        json.dump(narrativas, arquivo, ensure_ascii=False, indent=2)


if len(sys.argv) != 3:
    print("Uso: python scripts\\converter.py ENTRADA.csv SAIDA.json")
    sys.exit(1)

caminho_csv = sys.argv[1]
caminho_json = sys.argv[2]

narrativas = ler_csv(caminho_csv)
gravar_json(narrativas, caminho_json)

print(f"{len(narrativas)} narrativas convertidas.")
print(f"JSON gravado em: {caminho_json}")
def obter_taxa(moeda):
    # Simula uma busca de taxa (ex: vinda de uma API)
    taxas = {"DOLAR": 5.10, "EURO": 5.50}
    return taxas.get(moeda.upper(), 1.0)
    # taxas.get("DOLAR") é igual taxas["DOLAR"]


def converter_valor(quantia, taxa):
    return quantia / taxa

# --- PROGRAMA PRINCIPAL ---
print("--- SISTEMA DE CÂMBIO INOVADOR ---")
valor_brl = float(input("Quanto você tem em R$? "))
destino = input("Converter para (Dolar/Euro)? ")

taxa_atual = obter_taxa(destino)
resultado = converter_valor(valor_brl, taxa_atual)

print(f"Você terá {resultado:,.2f} na moeda {destino}.")
import requests

# Função para obter as taxas de câmbio em tempo real da API Open Exchange Rates
def obter_taxas(api_key):
    url = f"https://openexchangerates.org/api/latest.json?app_id={api_key}"
    resposta = requests.get(url)
    
    if resposta.status_code == 200:
        dados = resposta.json()
        return dados['rates']
    else:
        print("Erro ao obter as taxas de câmbio.")
        return None

# Função para converter um valor entre duas moedas
def converter_moeda(valor, moeda_origem, moeda_destino, taxas):
    if moeda_origem != "USD":
        valor_em_usd = valor / taxas[moeda_origem]
    else:
        valor_em_usd = valor
    
    valor_convertido = valor_em_usd * taxas[moeda_destino]
    return valor_convertido

# Lista de algumas moedas suportadas
moedas_disponiveis = {
    'USD': 'Dólar Americano',
    'EUR': 'Euro',
    'BRL': 'Real Brasileiro',
    'JPY': 'Iene Japonês',
    'GBP': 'Libra Esterlina',
    'CAD': 'Dólar Canadense',
    'AUD': 'Dólar Australiano',
    'CHF': 'Franco Suíço',
    'CNY': 'Yuan Chinês',
    'INR': 'Rupia Indiana'
}

# Função principal
def main():
    # Substitua 'sua_chave_api' pela sua chave de API do Open Exchange Rates
    api_key = "chave da api aqui"
    taxas = obter_taxas(api_key)
    
    if taxas is None:
        return
    
    print("Moedas disponíveis para conversão:")
    for codigo, nome in moedas_disponiveis.items():
        print(f"{codigo}: {nome}")
    
    moeda_origem = input("Digite o código da moeda de origem: ").upper()
    moeda_destino = input("Digite o código da moeda de destino: ").upper()
    valor = float(input(f"Digite o valor em {moeda_origem}: "))
    
    if moeda_origem not in taxas or moeda_destino not in taxas:
        print("Moeda inválida.")
        return
    
    valor_convertido = converter_moeda(valor, moeda_origem, moeda_destino, taxas)
    print(f"{valor:.2f} {moeda_origem} equivale a {valor_convertido:.2f} {moeda_destino}.")

if __name__ == "__main__":
    main()

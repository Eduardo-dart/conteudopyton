tamanho_do_arquivo = float(input("quantos megabytes(mb) seu arquivo pesa?"))
velocidade_internet = float(input("qual a velocidade da sua internet em megabites por segundo(Mbps)?"))
velocidade_de_download = velocidade_internet/8
tempo_do_download_segundos = (tamanho_do_arquivo/velocidade_de_download)
tempo_do_downlod_minutos = tempo_do_download_segundos/60

print("seu arquivo vai demorar",tempo_do_downlod_minutos,"minutos")

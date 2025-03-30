import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import threading
import time

def buscar_palavra_no_site(url_inicial, palavra, profundidade_maxima=3):
    """
    Busca recursivamente uma palavra específica em todas as páginas de um site utilizando threads.

    Parâmetros:
        url_inicial (str): A URL inicial do site.
        palavra (str): A palavra a ser buscada.
        profundidade_maxima (int): A profundidade máxima de navegação (padrão: 3).

    Retorna:
        dict: Um dicionário onde as chaves são URLs e os valores indicam se a palavra foi encontrada.
    """
    urls_visitados = set()
    resultados = {}
    lock = threading.Lock()  
    
    def buscar_recursivo(url_atual, profundidade_atual):
        with lock:
            if profundidade_atual > profundidade_maxima or url_atual in urls_visitados:
                return
            urls_visitados.add(url_atual)

        try:
            print(f"Buscando em: {url_atual} (Profundidade: {profundidade_atual})")
            response = requests.get(url_atual, timeout=10)
            response.raise_for_status()  # Levanta exceção para erros HTTP

            soup = BeautifulSoup(response.text, 'html.parser')

            conteudo = soup.get_text().lower()
            palavra_encontrada = palavra.lower() in conteudo
            with lock:
                resultados[url_atual] = palavra_encontrada

            links = soup.find_all('a', href=True)
            threads = []
            for link in links:
                url_completa = urljoin(url_inicial, link['href'])
                if url_completa.startswith(url_inicial):
                    t = threading.Thread(target=buscar_recursivo, args=(url_completa, profundidade_atual + 1))
                    threads.append(t)
                    t.start()

            for t in threads:
                t.join()

        except requests.exceptions.RequestException as e:
            print(f"Erro ao acessar {url_atual}: {e}")

    buscar_recursivo(url_inicial, profundidade_atual=1)
    return resultados

def main():
    url_inicial = input("Digite a URL inicial do site (ex.: https://www.exemplo.com): ").strip()
    palavra = input("Digite a palavra a ser buscada: ").strip()

    print("\nIniciando busca com threads...")
    inicio = time.perf_counter()
    resultados = buscar_palavra_no_site(url_inicial, palavra)
    fim = time.perf_counter()
    tempo_com_threads = fim - inicio

    print("\nResultados da busca:")
    for url, encontrada in resultados.items():
        status = "Encontrada" if encontrada else "Não encontrada"
        print(f"{url}: Palavra '{palavra}' {status}")
    print(f"\nTempo de execução com threads: {tempo_com_threads:.2f} segundos")

if __name__ == "__main__":
    main()

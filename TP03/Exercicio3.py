import time
import threading
from PIL import Image
from tkinter import Tk, filedialog

def processar_faixa(imagem, imagem_preto_branco, largura, start_y, end_y):
    """
    Processa uma faixa horizontal da imagem, convertendo cada pixel para tons de cinza.
    Cada faixa é definida pelos índices de linha (y) start_y até end_y.
    """
    for y in range(start_y, end_y):
        for x in range(largura):
            r, g, b = imagem.getpixel((x, y))
            luminancia = int(0.299 * r + 0.587 * g + 0.114 * b)
            imagem_preto_branco.putpixel((x, y), luminancia)

def converter_para_preto_e_branco_com_threads():
    try:
        root = Tk()
        root.withdraw()
        caminho_imagem = filedialog.askopenfilename(
            title="Selecione uma imagem",
            filetypes=[("Imagens", "*.jpg *.jpeg *.png *.bmp *.gif"), ("Todos os arquivos", "*.*")]
        )

        if not caminho_imagem:
            print("Nenhuma imagem foi selecionada.")
            return

        imagem = Image.open(caminho_imagem).convert("RGB")
        largura, altura = imagem.size
        imagem_preto_branco = Image.new("L", (largura, altura))

        num_threads = 4
        slice_altura = altura // num_threads  # Altura de cada faixa
        threads = []

        inicio = time.perf_counter()

        for i in range(num_threads):
            start_y = i * slice_altura
            end_y = (start_y + slice_altura) if i != num_threads - 1 else altura
            t = threading.Thread(target=processar_faixa, args=(imagem, imagem_preto_branco, largura, start_y, end_y))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

        fim = time.perf_counter()
        tempo_com_threads = fim - inicio

        caminho_saida = filedialog.asksaveasfilename(
            title="Salvar imagem em preto e branco",
            defaultextension=".jpg",
            filetypes=[("JPEG", "*.jpg"), ("PNG", "*.png"), ("Todos os arquivos", "*.*")]
        )

        if not caminho_saida:
            print("Operação de salvamento cancelada.")
            return

        imagem_preto_branco.save(caminho_saida)
        print(f"Imagem convertida com sucesso! Salva em: {caminho_saida}")
        print(f"Tempo de execução com threads: {tempo_com_threads:.2f} segundos")

    except Exception as e:
        print(f"Erro ao processar a imagem: {e}")

if __name__ == "__main__":
    converter_para_preto_e_branco_com_threads()

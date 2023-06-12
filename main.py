# importar opencv2 para trabalhar com as imagens
import cv2

# importar tkinter
import customtkinter as ctk
from tkinter import filedialog

# importar PIL para trabalhar imagem na janela
from PIL import Image, ImageTk

# importar deepface para o reconhecimento facial
from deepface import DeepFace

# iniciar janela tkinter
janela = ctk.CTk()
janela.minsize(400, 600)
janela.maxsize(400, 600)
janela.configure(bg='black')
janela.title("Reconhecimento Facial")


# função para selecionar imagem a janela
def selecionar_imagem():
    caminho_imagem = filedialog.askopenfilename()
    # lê a imagem usando cv2.imread()
    imagem = cv2.imread(caminho_imagem)
    # redimensiona a imagem para 250x250 pixels
    imagem = cv2.resize(imagem, (250, 250))
    # converte a imagem de BGR para RGB
    imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)
    # passa a imagem para DeepFace
    resultado = DeepFace.analyze(imagem, actions=("age", "emotion", "gender", "race"))
    print(resultado)
    # converte a imagem em formato Tkinter
    foto = ImageTk.PhotoImage(Image.fromarray(imagem))
    # atualiza o Label com a imagem
    rotulo.configure(image=foto)
    rotulo.image = foto
    # define a distância da imagem em relação à borda do frame
    rotulo.place(x=80, y=20)
    # extrai a idade, emoção, gênero e raça do resultado retornado pela DeepFace
    idade = resultado[0]["age"]
    emocao = resultado[0]["dominant_emotion"]
    genero = resultado[0]["dominant_gender"]
    raca = resultado[0]["dominant_race"]
    # atualiza as labels correspondentes com as informações extraídas
    labelidade.configure(text="Idade:         " + str(idade))
    labelemocao.configure(text="Emoção:      " + emocao)
    labelgenero.configure(text="Gênero:       " + genero)
    labelraca.configure(text="Raça:         " + raca)

def capturar_imagem():
    # acessar a câmera do dispositivo
    camera = cv2.VideoCapture(0)
    while True:
        # capturar um quadro da câmera
        ret, imagem = camera.read()
        # exibir o quadro em uma janela separada
        cv2.imshow('Capturando imagem', imagem)
        # aguardar a tecla 'q' para fechar a janela e salvar a imagem
        if cv2.waitKey(1) & 0xFF == ord('q'):
            # salvar a imagem em disco
            cv2.imwrite('imagem_capturada.jpg', imagem)
            break
    # liberar os recursos da câmera
    camera.release()
    # fechar a janela
    cv2.destroyAllWindows()

# criar botão para capturar imagem
botao_capturar = ctk.CTkButton(janela, text='Capturar imagem', command=capturar_imagem)
botao_capturar.place(x=50, y=300)

#criar botão para selecionar imagem
botao = ctk.CTkButton(janela, text='Selecionar imagem', command=selecionar_imagem)
botao.place(x=230, y=300)

#criar label para apresentar a imagem na janela
rotulo = ctk.CTkLabel(janela)

#labels para apresentar as respostas
labelidade = ctk.CTkLabel(janela, text="Idade:", font=("Arial", 14))
labelidade.place(x=50, y=350)

labelraca = ctk.CTkLabel(janela, text="Raça:", font=("Arial", 14))
labelraca.place(x=50, y=400)

labelemocao = ctk.CTkLabel(janela, text="Emoção:", font=("Arial", 14))
labelemocao.place(x=50, y=450)

labelgenero = ctk.CTkLabel(janela, text="Gênero: ", font=("Arial", 14))
labelgenero.place(x=50, y=500)


#looping da janela
janela.mainloop()

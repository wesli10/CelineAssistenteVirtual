import speech_recognition as sr
import pyttsx3
from config import *
from random import choice
import sys


reproducao = pyttsx3.init()
voices = reproducao.getProperty('voices')
reproducao.setProperty('voices', voices[0].id)


def sai_som(resposta):
    reproducao.say(resposta)
    reproducao.runAndWait()

def assistente():
    print("( ' - ') Just Do IT")
    sai_som("Eu me chamo Celine, com quem eu falo?")
    while True:
        resposta_erro_aleatoria = choice(lista_erros)
        rec = sr.Recognizer()
        with sr.Microphone() as s:
            rec.adjust_for_ambient_noise(s)

            while True:
                try:
                    audio = rec.listen(s)
                    user_name = rec.recognize_google(audio, language="pt")
                    user_name = verifica_nome(user_name)
                    name_list()
                    apresentacao = "{}".format(verifica_nome_existe(user_name))
                    sai_som(apresentacao)

                    brute_user_name = user_name
                    user_name = user_name.split(" ")
                    user_name = user_name[0]
                    break


                except sr.UnknownValueError:
                    pass
            break

    while True:
        resposta_erro_aleatoria = choice(lista_erros)
        rec = sr.Recognizer()
        with sr.Microphone() as s:
            rec.adjust_for_ambient_noise(s)

            while True:
                try:
                    audio = rec.listen(s)
                    entrada = rec.recognize_google(audio, language="pt-br")


                    #chame ela pra saber se está disponivel
                    if "Celine" in entrada:
                        sai_som("Pois não")

                    elif "anotar" in entrada:
                        anotar(entrada)

                    #Reiniciar
                    elif "Reiniciar PC" in entrada or "reiniciar computador" in entrada:
                        os.system("shutdown /r /t 0")

                    #Pesquisa Google
                    elif "pesquisa" in entrada or "pesquisar" in entrada:
                        pesquisa(entrada)

                    #Abrir Aplicativo
                    elif "Abrir" in entrada or "abre" in entrada:
                        abrir(entrada)

                    #operações matemáticas
                    elif "Quanto é" in entrada or "quanto é" in entrada:
                        entrada = entrada.replace("Quanto é", "")
                        sai_som(calcula(entrada))
                        
                    # Pede Tempo
                    elif "temperatura" in entrada:

                        lista_tempo = temperatura()
                        temp = lista_tempo[0]
                        temp_max = lista_tempo[1]
                        temp_min = lista_tempo[2]

                        sai_som("A temperatura de hoje é {:.0f}°. Temos a máxima de {:.0f} e uma minima de {:.0f}°".format(temp,  temp_max, temp_min))
                        

                    # Informações da cidade
                    elif "informações" in entrada and "cidade" in entrada:

                        sai_som("Mostrando informações da cidade")
                        

                    else:
                        sai_som(conversas[entrada])

                    if resposta == "Mostrando informações da cidade":
                        #mostra informações da cidade

                        lista_infos = clima_tempo()
                        longitude = lista_infos[0]
                        latitude = lista_infos[1]
                        temp = lista_infos[2]
                        pressao_atm = lista_infos[3]
                        humidade = lista_infos[4]
                        temp_max = lista_infos[5]
                        temp_min = lista_infos[6]
                        v_speed = lista_infos[7]
                        v_direc = lista_infos[8]
                        nebulosidade = lista_infos[9]
                        id_da_cidade = lista_infos[10]

                        print("Assistente:")
                        print("Mostrando informações de {}\n\n".format(cidade))
                        sai_som("Mostrando informações de {}".format(cidade))
                        print("Longitude: {}, Latitude: {}\nId: {}\n".format(longitude, latitude, id_da_cidade))
                        print("Temperatura : {:.0f}°".format(temp))
                        print("Temperatura Máxima : {:.0f}°".format(temp_max))
                        print("Temperatura Mínima : {:.0f}°".format(temp_min))
                        print("Humidade: {}".format(humidade))
                        print("Nebulosidade: {}".format(nebulosidade))
                        print("Velocidade do vento: {}m/s\nDireção do vento: {}".format(v_speed,v_direc))

                    
                except:
                    pass
                    

if __name__ == '__main__':
    intro()
    sai_som("iniciando")
    assistente()
         
            



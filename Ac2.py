import sounddevice as sd
import wave
import speech_recognition as sr
import streamlit as st

def guardaraudio(nome_arquivo,duracao,taxa=44100):
    audio = sd.rec(int(duracao*taxa),samplerate=taxa, channels=1,dtype='int16')
    st.title("Fale os itens que deseja adicionar a sua lista de compras...")
    sd.wait()
    with wave.open(nome_arquivo,'wb') as wb:
        wb.setsampwidth(2)
        wb.setnchannels(1)
        wb.setframes(taxa)
        wb.writeframes(audio.tobytes())

    st.write("Gravado com sucesso")
guardaraudio("audio.wav",10)


import requests
from gtts import gTTS


def generar_texto_huggingface(prompt, max_length=150):
    url =  "https://api-inference.huggingface.co/models/PlanTL-GOB-ES/gpt2-large-bne"
    headers = {"Authorization": "Bearer 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"}
    payload = {
        "inputs": prompt,
        "parameters": {"max_length": max_length, "temperature": 0.7},
    }

    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()[0]["generated_text"]
    else:
        return f"Error: {response.status_code}, {response.text}"


def generar_audio(texto, archivo_salida="audio.mp3"):
    tts = gTTS(text=texto, lang='es')
    tts.save(archivo_salida)
    print(f"Audio generado: {archivo_salida}")


if __name__=="__main__":
    tema = input("Escribe el tema inicial para el video: ")
    texto_generado= generar_texto_huggingface(tema)
    
    if texto_generado.startswith("Error"):
        print(f"No se pudo generar el texto: {texto_generado}")
    else:
        print(f"Texto generado:\n{texto_generado}")

        generar_audio(texto_generado,archivo_salida="video_audio.mp3")
import requests
from gtts import gTTS


def generar_texto_huggingface(prompt, max_length=150):
    url =  "https://api-inference.huggingface.co/models/PlanTL-GOB-ES/gpt2-large-bne"
    headers = {"Authorization": "Bearer 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"}
    payload = {
        "inputs": prompt,
        "parameters": {"max_length": 50, "temperature": 0.5}
    }

    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()[0]["generated_text"]
    else:
        return f"Error: {response.status_code}, {response.text}"


def generar_audio(texto, archivo_salida="audio_ia.mp3"):
    
    api_url = "https://api.elevenlabs.io/v1/text-to-speech/dlGxemPxFMTY7iXagmOj"

    headers = {
        "xi-api-key": "sk_10be862972ad045c8bec7033161028e25a31291b731e8225",
        "Content-Type": "application/json",
 
    }

    payload = {
        "text": texto,
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.7
        }
    }


    response = requests.post(api_url, headers=headers, json=payload)

    if response.status_code ==200:

        with open(archivo_salida, "wb") as f:
            f.write(response.content)
        print(f"Audio generado y guardado en: {archivo_salida}")

    else:
        print(f"Error: {response.status_code}, {response.text}")
  



  
if __name__=="__main__":
    tema = input("Escribe el tema inicial para el video: ")
    texto_generado= generar_texto_huggingface(tema)
    
    if texto_generado.startswith("Error"):
        print(f"No se pudo generar el texto: {texto_generado}")
    else:
        print(f"Texto generado:\n{texto_generado}")

        generar_audio(texto_generado,archivo_salida="video_audio.mp3")
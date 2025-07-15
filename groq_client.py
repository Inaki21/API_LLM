import os
import requests

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

def ask_groq(question):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    # data = {
    #     "model": "llama-3.3-70b-versatile",  # mixtral-8x7b-32768
    #     "messages": [
    #         {"role": "user", "content": question}
    #     ]
    # }

    data = {
    "model": "llama-3.3-70b-versatile",  #mixtral-8x7b-32768;llama3-70b-8192
    "messages": [
        {"role": "system", "content": "Eres un asistente de viajes experto. Ayudas a los usuarios a planificar viajes, recomendar destinos, actividades, alojamientos y transporte. Sé claro, útil, y personaliza tus respuestas."},
        {"role": "user", "content": question}
        ]
    }


    response = requests.post(GROQ_API_URL, headers=headers, json=data)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Error: {response.status_code} - {response.text}"



# import os
# from groq import Groq
# from dotenv import load_dotenv

# # Cargar las variables de entorno
# load_dotenv()

# # Configuración de la API de Groq
# client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# def get_chat_response(user_message: str) -> str:
#     try:
#         chat_completion = client.chat.completions.create(
#             messages=[{"role": "user", "content": user_message}],
#             model="llama-3.3-70b-versatile",
#             stream=False,
#         )
#         return chat_completion.choices[0].message.content
#     except Exception as e:
#         return f"Error al obtener respuesta del modelo: {str(e)}"
# "\x1b[1;51m" <- Bold text
# "\x1b[1;41m" <- Text with red background
# "\x1b[1;21m" <- Underline text
# "\x1b[3;21m" <- Italic underline text
# "\x1b[3;32m" <- Green italic text
# "\x1b[9;21m" <- Strikethrough underlined text

import openai

#openai.api_key = ""
api_key = "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"
openai.api_key = api_key

system_rol = """Vas a hacer de cuenta que eres un analizador de sentimientos.
                Yo te paso sentimientos y tu analizas el sentimiento de los mensajes,
                y me das al menos una respuesta con al menos 1 caracter y como máximo 4 caracteres.
                SOLO RESPUESTAS NUMERICAS, donde -1 es sentimiento negativo maximo, 0 sentimiento neutral, y 1 sentimiento positivo maximo.
                puedes ir entre esos rangos, es decir 0.3, -0.5, 0, etc... también son válidos.
                (Puedes responder con int or float)"""


mensaje = [{"role": "system", "content": system_rol}]

class AnalizarSentimientos:
    def analizar_sentimiento(self, polaridad):
        if polaridad > -0.6 and polaridad <= -0.3:
            return "\x1b[3;31m" + "Negativo"
        elif polaridad > -0.3 and polaridad <= -0.1:
            return "\x1b[3;31m" + "Un poco negativo"
        elif polaridad > -0.1 and polaridad <= 0.1:
            return "\x1b[3;33m" + "Neutral"
        elif polaridad >= 0.1 and polaridad <= 0.4:
            return "\x1b[3;32m" + "Ligeramente positivo"
        elif polaridad >= 0.4 and polaridad <= 0.9:
            return "\x1b[3;32m" + "Positivo"
        elif polaridad > 0.9:
            return "\x1b[3;32m" + "Muy positivo"
        else:
            return "\x1b[3;31m" + "Muy negativo"

        
analizador = AnalizarSentimientos()

while True:
    user_prompt = input("\x1b[1;51m" + "\nEscribe algo, cualquier cosa: " + "\x1b[0;37m")

    mensaje.append({"role":"user", "content": user_prompt})

    completion = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = mensaje,
        max_tokens = 8
    )

    # Store chatgpt answers so can have memory when we ask follow-up questions.
    respuesta = completion.choices[0].message["content"]
    mensaje.append({"role":"assistant", "content": respuesta})

    sentimiento = analizador.analizar_sentimiento(float(respuesta))
    print(sentimiento)
    print(completion)

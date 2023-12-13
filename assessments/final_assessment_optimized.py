# "\x1b[1;51m" <- Bold text
# "\x1b[1;41m" <- Text with red background
# "\x1b[1;21m" <- Underline text
# "\x1b[3;21m" <- Italic underline text
# "\x1b[3;32m" <- Green italic text
# "\x1b[9;21m" <- Strikethrough underlined text

import openai
from openai_key import api_key

openai.api_key = api_key

system_rol = """Vas a hacer de cuenta que eres un analizador de sentimientos.
                Yo te paso sentimientos y tu analizas el sentimiento de los mensajes,
                y me das al menos una respuesta con al menos 1 caracter y como máximo 4 caracteres.
                SOLO RESPUESTAS NUMERICAS, donde -1 es sentimiento negativo maximo, 0 sentimiento neutral, y 1 sentimiento positivo maximo.
                puedes ir entre esos rangos, es decir 0.3, -0.5, 0, etc... también son válidos.
                (Puedes responder con int or float)"""


mensaje = [{"role": "system", "content": system_rol}]


# Apply SRP, bc this class should only provide color and name of the feeling.
class Sentimiento:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __str__(self) -> str:
        return "\x1b[3;{}m{}\x1b[0;37m".format(self.color, self.name)


# Apply OCP, since we can add more ranges without modifying method.
class AnalizarSentimientos:

    def __init__(self, range):
        self.range = range


    def analizar_sentimiento(self, polaridad):
        for range, sentimiento in self.range:
            if range[0] < polaridad <= range[1]:
                return sentimiento
        
        return Sentimiento("Muy negativo", "31")


ranges = [
    ((-0.6, -0.3), Sentimiento("Negativo", "31")),
    ((-0.3, -0.1), Sentimiento("Ligeramente negativo", "31")),
    ((-0.1, 0.1), Sentimiento("Neutral", "33")),
    ((0.1, 0.4), Sentimiento("Ligeramente positivo", "32")),
    ((0.4, 0.9), Sentimiento("Positivo", "32")),
    ((0.9, 1), Sentimiento("Muy Positivo", "32"))
]

        
analizador = AnalizarSentimientos(ranges)

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

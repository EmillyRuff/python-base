"""
Alarme de temperatura
Faça um script que pergunta ao usuário qual a temperatura atual e o indice de
umidade do ar sendo que caso será exibida uma mensagem de alerta dependendo das
condições:
temp maior 45: "ALERTA!!! 🥵 Perigo calor extremo"
temp maior que 30 e temp vezes 3 for maior ou igual a umidade:
    "ALERTA!!! 🥵♒ Perigo de calor úmido"
temp entre 10 e 30: "😀 Normal"
temp entre 0 e 10: "🥶 Frio"
temp <0: "ALERTA!!! ⛄ Frio Extremo."
ex:
python3 alerta.py
temperatura: 30
umidade: 90
...
"ALERTA!!! 🥵♒ Perigo de calor úmido"
"""
def verificar_alerta(temp, umidade):
    if temp > 45:
        return "ALERTA!!! 🥵 Perigo calor extremo"
    elif temp > 30 and (temp * 3) >= umidade:
        return "ALERTA!!! 🥵♒ Perigo de calor úmido"
    elif 10 <= temp <= 30:
        return "😀 Normal"
    elif 0 <= temp < 10:
        return "🥶 Frio"
    else:
        return "ALERTA!!! ⛄ Frio Extremo."

if __name__ == "__main__":
    try:
        temperatura = float(input("Temperatura: "))
        umidade = float(input("Umidade: "))
        print("\n", verificar_alerta(temperatura, umidade))
    except ValueError:
        print("Por favor, insira valores numéricos válidos.")

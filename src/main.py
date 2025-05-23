from sklearn.tree import DecisionTreeClassifier

def main():
    characteristics = [
        [20, 4],   # Tênis
        [70, 1],   # Basquete
        [68, 2],   # Futebol
        [63, 3],   # Futebol
        [21, 4],    # Tênis
        [75, 1],   # Basquete
        [22, 0],   # Baseball
        [24, 0],   # Baseball
    ]

    types = ['Tênis', 'Basquete', 'Futebol', 'Futebol', 'Tênis', 'Basquete', 'Baseball', 'Baseball']
    colors = {0: 'branca', 1: 'laranja', 2: 'amarela', 3: 'preto e branco', 4: 'verde'}
    
    model = DecisionTreeClassifier()
    model.fit(characteristics, types)
    
    try:
        new_ball_size = int(input("Qual e a circumferencia da bola? "))
    except:
        print("O tamanho da bola deve ser um numero!")
        return
    print("\n")
    try:
        new_color = int(input("Qual é a cor da bola? (0 - branca; 1 - laranja; 2 - amarela; 3 - preto e branco; 4 - verde): "))
        if new_color < 0:
            print("A cor da bola deve ser um numero entre 0 e 2!")
            return
        if new_color > 4:
            print("A cor da bola deve ser um numero entre 0 e 2!")
            return
    except:
        print("A cor da bola deve ser um numero!")
        return
    print("\n\n")

    new_ball = [[new_ball_size, new_color]]
    resultado = model.predict(new_ball)
    
    print(f"Bola de {new_ball[0][0]}cm ({colors[new_ball[0][1]]}) classificada como: {resultado[0]}")


if __name__ == "__main__":
    main()

import random
import time

def rodar_roleta():
    # Lista de símbolos possíveis na máquina
    simbolos = ['7', '🍒', '🍋', '🍇', '💎', '🍀']
    
    # Sorteia 3 símbolos aleatórios
    resultado = [random.choice(simbolos) for _ in range(3)]
    return resultado

def jogar():
    print("=" * 30)
    print("  🎰 CASSINO DE TEXTO: 777 🎰  ")
    print("=" * 30)
    print("Regra: tire 7 7 7 para ganhar!")
    
    saldo = 100  # saldo inicial
    custo_jogada = 10
    
    while saldo >= custo_jogada:
        input(f"\nSeu saldo atual: ${saldo}. pressione ENTER para jogar por ${custo_jogada}...")
        saldo -= custo_jogada
        
        print("\n🎰 girando a máquina...")
        time.sleep(0.5)
        
        for _ in range(3):
            res_temporario = rodar_roleta()
            print(f"| {res_temporario[0]} | {res_temporario[1]} | {res_temporario[2]} |", end="\r")
            time.sleep(0.4)
        
        # Resultado final
        resultado_final = rodar_roleta()
        print(f"| {resultado_final[0]} | {resultado_final[1]} | {resultado_final[2]} |")
        print("-" * 30)
        
        if resultado_final == ['7', '7', '7']:
            premio = 500
            saldo += premio
            print(f"🎉 🎉 JACKPOT!!! voce tirou 777 e ganhou ${premio}! 🎉 🎉")
        else:
            print("❌ nao foi dessa vez. Tente novamente!")
            
    print("\n o seu saldo acabou!")

if __name__ == "__main__":
    jogar()

from datetime import datetime
import module_text

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    dt = datetime.now()
    date = dt.strftime(module_text.DATE_FORMAT)
    time = dt.strftime(module_text.TIME_FORMAT)
    opcao = input(module_text.TXT_MENU).lower()
    
    match opcao:
        case "d":
            valor = float(input("Informe o valor do depósito: "))

            if valor > 0:
                saldo += valor
                extrato += f"{date} - {time} - C - R$ {valor:.2f} \n"

            else:
                print(f"{module_text.TXT_ERROR_VALUE}")
                
        case "s":
            valor = float(input(module_text.TXT_SAQUE))

            excedeu_saldo = valor > saldo

            excedeu_limite = valor > limite

            excedeu_saques = numero_saques >= LIMITE_SAQUES

            if excedeu_saldo:
                print(f"{module_text.TXT_EXCEDEU_SALDO}")

            elif excedeu_limite:
                print(f"{module_text.TXT_EXCEDEU_LIMITE}")

            elif excedeu_saques:
                print(f"{module_text.TXT_EXCEDEU_SAQUES}")
                numero_saques = LIMITE_SAQUES

            elif valor > 0:
                saldo -= valor
                extrato += f"{date} - {time} - D - R$ {valor:.2f}\n"
                numero_saques += 1
                print(f"Você utilizou {numero_saques}/{LIMITE_SAQUES} diários.")

            else:
                print(f"{module_text.TXT_ERROR_VALUE}")


        case "e":
            print(f"\n{module_text.TXT_EXTRATO.upper().center(42, "=")}")
            print(f"{module_text.TXT_ERROR_EXTRATO.upper()}" if not extrato else extrato)
            print(f"\nSaldo em {date}: R$ {saldo:.2f}")
            print("==========================================")

        case "q":
            break

        case _:
            print("Operação inválida, por favor selecione novamente a operação desejada.")
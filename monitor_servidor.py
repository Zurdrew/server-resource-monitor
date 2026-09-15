import psutil
import datetime

# Configurações de limite (em porcentagem)
LIMITE_CPU = 85.0
LIMITE_RAM = 85.0
LIMITE_DISCO = 90.0
ARQUIVO_LOG = "alerta_servidor.log"

def registrar_log(mensagem):
    agora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(ARQUIVO_LOG, "a") as log:
        log.write(f"[{agora}] ALERTA: {mensagem}\n")
    print(f"Alerta registrado: {mensagem}")

def verificar_sistema():
    print("Iniciando verificação de recursos...")
    
    # Coleta os dados
    uso_cpu = psutil.cpu_percent(interval=1)
    uso_ram = psutil.virtual_memory().percent
    uso_disco = psutil.disk_usage('/').percent

    print(f"Status Atual -> CPU: {uso_cpu}% | RAM: {uso_ram}% | Disco: {uso_disco}%")

    # Verifica os limites
    if uso_cpu > LIMITE_CPU:
        registrar_log(f"Uso de CPU crítico: {uso_cpu}%")
    
    if uso_ram > LIMITE_RAM:
        registrar_log(f"Uso de Memória RAM crítico: {uso_ram}%")
        
    if uso_disco > LIMITE_DISCO:
        registrar_log(f"Espaço em Disco crítico: {uso_disco}%")

if __name__ == "__main__":
    verificar_sistema()
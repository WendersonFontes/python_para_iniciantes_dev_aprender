#schedule.cada.tempo.fazer
#schedule.every(10).monday.do(FazerTarefaImportante)
#schedule.every(10).monday.at("08:00").do(FazerTarefaImportante)
#schedule.every(10).monday.day("08:00").do(FazerTarefaImportante)
import schedule
import time

def fazer_tarefa_importante():
    print('Gerando texto...')

def main():
    # Agendar a tarefa para ser executada a cada 10 segundos
    schedule.every(10).seconds.do(fazer_tarefa_importante)

    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        print("Interrompido pelo usuário. Saindo...")

if __name__ == "__main__":
    main()

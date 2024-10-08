from time import sleep

from airflow.decorators import dag, task

from datetime import datetime

@dag (
        dag_id= "minha_primeira_dag",
        description="minha elt braba",
        schedule="* * * * *",
        start_date=datetime(2024,9,11),
        catchup=False #backfill

)
def minha_primeira_dag():

    @task
    def primeira_atividade():
        print("minha primeira atividade!")
        sleep(2)

    @task
    def segunda_atvidade():
        print("minha segunda atividade!")
        sleep(2)

    @task
    def terceira_atividade():
        print("minha terceira atividade")
        sleep(2)

    @task
    def quarta_atividade():
        print("pipeline finalizou")

    t1 = primeira_atividade()
    t2 = segunda_atvidade()
    t3 = terceira_atividade()
    t4 = quarta_atividade()

    t1 >> t2 >> t3 >> t4

minha_primeira_dag()

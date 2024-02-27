from typing import List, Dict
import csv


class ProcessJobs:
    def __init__(self) -> None:
        self.jobs_list = list()

    def read(self, path) -> List[Dict]:
        # abrir o arquivo csv, O método deve tratar o arquivo como CSV.
        with open(
            path, encoding="utf-8"
        ) as file:  # codificação utf-8 para leitura html
            # criar um read de dicinario (DictReader) para o arquivo csv
            read_file = csv.DictReader(file)
            # cada linha itinerar no arquivo csv
            for row in read_file:
                # adicionar a lista de jobs
                # armazenar(append) o resultado em uma lista de dicionários
                self.jobs_list.append(row)

    def get_unique_job_types(self) -> List[str]:
        # criar uma lista vazia
        jobs_lista = []
        # iterar sobre a lista de jobs
        for job in self.jobs_list:
            # adicionar o tipo de trabalho na lista
            jobs_lista.append(job["job_type"])
            # retornar a lista de tipos de trabalho
        return list(set(jobs_lista))

    def filter_by_multiple_criteria(self, jobs, filter) -> List[dict]:
        jobs_lista = []
        # O método deve lançar uma exceção TypeError quando o filtro
        # fornecido para o
        # método filter_by_multiple_criteria não é um dicionário
        if not type(filter) is dict:  # is é um ==
            raise TypeError

        for job in jobs:
            # verifica se todas (critérios)as chaves e valorers em f
            # ilters corresponde ao valores em job,
            # ai se sim ele significa que as condicoes do filtro
            # sao atendidas
            if all(job[key] == value for key, value in filter.items()):
                # se for atendido, adicione o trabalho à lista de trabalhos
                jobs_lista.append(job)
        return jobs_lista


# cada chave de dicionario representa um job com (industry e job_type)
# e cada valor é uma lista de dicionarios que representam os jobs
# o filtro  de job onde ve se a industria é igual a
# "IT" e o job_type é igual a "FULL_TIME"


# if all(job[key] == value for key, value in filter.items()):
# estrutura geral all(expressão for variável in iterável)
# expressão: É a expressão que será avaliada para cada elemento
# do iterável.
# variável: É a variável de iteração que assume cada valor do iterável
# em cada iteração.
# iterável: É o iterável (geralmente uma sequência como uma lista,
# tupla ou dicionário) sobre o qual a iteração ocorrerá.

# job[key] == value for key, value in filter.items()

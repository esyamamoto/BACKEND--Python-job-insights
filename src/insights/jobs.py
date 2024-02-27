from typing import List, Dict
import csv


class ProcessJobs:
    def __init__(self) -> None:
        self.jobs_list = list()

    def read(self, path) -> List[Dict]:
        # abrir o arquivo csv, O método deve tratar o arquivo como CSV.
        with open(path, encoding="utf-8") as file: #codificação utf-8 para leitura html
            #criar um read de dicinario (DictReader) para o arquivo csv
            read_file = csv.DictReader(file)
            #cada linha itinerar no arquivo csv
            for row in read_file:
                #adicionar a lista de jobs
                # armazenar(append) o resultado em uma lista de dicionários
                self.jobs_list.append(row)
            

    def get_unique_job_types(self) -> List[str]:
        #criar uma lista vazia
        jobs_lista = []
        #iterar sobre a lista de jobs
        for job in self.jobs_list:
            #adicionar o tipo de trabalho na lista
            jobs_lista.append(job["job_type"])
            #retornar a lista de tipos de trabalho
        return list(set(jobs_lista))
       
    def filter_by_multiple_criteria(self) -> List[dict]:
        pass

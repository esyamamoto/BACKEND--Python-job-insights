from typing import Union, List, Dict
from src.insights.jobs import ProcessJobs


class ProcessSalaries(ProcessJobs):
    def __init__(self):
        super().__init__()

    def get_max_salary(self) -> int:
        # O método deve ignorar os valores ausentes.
        if len(self.jobs_list) == 0:  # len = lenght
            raise ValueError("The jobs list is empty")
        # cria lista de salarios mac
        salary_max = [
            # retornar um valor inteiro
            int(job["max_salary"])
            for job in self.jobs_list
            if job["max_salary"] != ""
            and job[
                "max_salary"
            ].isdigit()  # isdigit = verifica se é um número
        ]
        return max(salary_max)

    def get_min_salary(self) -> int:
        # O método deve ignorar os valores ausentes.
        if len(self.jobs_list) == 0:  # len = lenght
            raise ValueError("The jobs list is empty")
        # cria lista de salarios min
        salary_min = [
            # retornar um valor inteiro
            int(job["min_salary"])
            for job in self.jobs_list
            if job["min_salary"] != ""
            and job[
                "min_salary"
            ].isdigit()  # isdigit = verifica se é um número
        ]
        return min(salary_min)

    def matches_salary_range(self, job: Dict, salary: Union[int, str]) -> bool:
        pass

    def filter_by_salary_range(
        self, jobs: List[dict], salary: Union[str, int]
    ) -> List[Dict]:
        pass

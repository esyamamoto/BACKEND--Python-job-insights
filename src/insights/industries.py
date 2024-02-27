from src.insights.jobs import ProcessJobs
from typing import List


class ProcessIndustries(ProcessJobs):
    def __init__(self):
        super().__init__()

    def get_unique_industries(self) -> List[str]:
        if not self.jobs_list:
            self.read("data/jobs.csv")
        industries = []
        for job in self.jobs_list:
            if job["industry"] not in industries and job["industry"] != "":
                industries.append(job["industry"])
        return industries

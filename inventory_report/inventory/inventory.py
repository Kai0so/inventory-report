import csv
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def import_data(self, path, type):
        with open(path, encoding="utf-8") as file:
            inventory_reader = csv.DictReader(
                file, delimiter=",", quotechar='"'
            )
            inventory_list = list(inventory_reader)
        if type == "simples":
            return SimpleReport.generate(inventory_list)
        elif type == "completo":
            return CompleteReport.generate(inventory_list)

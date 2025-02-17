from datetime import datetime

class CalculoDiferencaDatas:
    def __init__(self, data1, data2):
        self.data1 = datetime.strptime(data1, "%Y-%m-%d")
        self.data2 = datetime.strptime(data2, "%Y-%m-%d")

    def calcular_diferenca(self):
        diferenca = self.data2 - self.data1
        return diferenca.days

data_inicial = "2025-01-01"
data_final = "2025-17-02"
calculadora = CalculoDiferencaDatas(data_inicial, data_final)
print("A diferença entre as datas é:", calculadora.calcular_diferenca(), "dias")
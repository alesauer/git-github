# Calculadora de Diferença entre Datas

Este projeto Python calcula a diferença em dias entre duas datas fornecidas.

## Funcionalidades

- Recebe duas datas no formato YYYY-MM-DD
- Calcula a diferença em dias entre as datas
- Retorna o resultado em dias

## Como usar

1. Certifique-se de ter Python 3.x instalado
2. Execute o script com:
```bash
python app.py
```

3. O script calculará automaticamente a diferença entre as datas pré-definidas:
   - Data inicial: 2024-01-01
   - Data final: 2024-03-01

4. O resultado será exibido no terminal:
```
Diferença entre as datas: 60 dias
```

## Estrutura do Código

- `CalculoDiferencaDatas`: Classe principal que realiza o cálculo
  - `__init__`: Inicializa as datas
  - `calcular_diferenca`: Calcula a diferença em dias

## Requisitos

- Python 3.x
- Módulo datetime (nativo do Python)

## Exemplo de Uso

Para modificar as datas, edite as variáveis `data_inicial` e `data_final` no arquivo `app.py`.

## Licença

[MIT](https://choosealicense.com/licenses/mit/)

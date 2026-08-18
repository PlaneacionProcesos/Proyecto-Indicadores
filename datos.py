import pandas as pd

df = pd.DataFrame({
    "mes": ["Enero", "Enero", "Febrero", "Febrero"],
    "producto": ["A", "B", "A", "B"],
    "ventas": [100, 150, 120, 180]
})


def ventas_mes():
    resultado = df.groupby("mes")["ventas"].sum().reset_index()
    return resultado


def ventas_productos():
    resultado = df.groupby("producto")["ventas"].sum().reset_index()
    return resultado
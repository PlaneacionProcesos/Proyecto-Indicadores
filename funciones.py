from datos import resultados_completos


def total_registros(df):

    return df["indicador_id"].nunique()


def total_indicadores_estrategicos(df):

    return df[
        df["tipo de indicador"] == "Estrategico"
    ]["indicador_id"].nunique()


def total_indicadores_sgc(df):

    return df[
        df["tipo de indicador"] == "SGC"
    ]["indicador_id"].nunique()


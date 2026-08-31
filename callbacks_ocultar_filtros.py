from dash import Input, Output


def registrar_callback_ocultar_filtros (app):

# ========================================================================================
# OCULTAR FILTROS
# ========================================================================================

    @app.callback(
        Output("segmentadores", "className"),
        Output("btn-toggle-filtros", "children"),
        Input("btn-toggle-filtros", "n_clicks"),
        prevent_initial_call=True,
    )
    def toggle_filtros(n_clicks):

        if n_clicks % 2 == 1:

            return (
                "segmentadores oculto",
                "▶",
            )

        return (
            "segmentadores",
            "◀",
        )

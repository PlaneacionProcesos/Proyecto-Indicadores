.app                         100vh
│
├── .header                  110px
│
├── .navegacion              altura propia
│
└── .contenedor              flex: 1
    │
    ├── .segmentadores       300px
    │
    └── #contenido-seccion   flex: 1
        │
        └── .graficas        flex: 1
            │
            ├── .tarjetas    140px
            │
            └── .visualizaciones
                              ↕ SCROLL



app.py
│
├── layout_header()
├── layout_navegacion()
├── dcc.Store("seccion-actual")
│
└── .contenedor
    ├── layout_filtros()
    │
    └── #contenido-seccion
        └── layout_resumen()
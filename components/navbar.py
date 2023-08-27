from dash import html
import dash_trich_components as dtc


def Navbar():
    navbar = html.Div(
        [
            html.Div(
                [
                    html.Div(
                        html.Div(
                            html.A(
                                "JohnTor",
                                className="logo",
                                href="https://jonathanmagliano.github.io/johntor",
                            )
                        )
                    ),
                    html.Div(dtc.ThemeToggle(
                        tooltip_text="Modo Light/Dark"
                    )),
                ],
                className="container flex_row_btw",
            ),
        ],
        className="navbar",
    )
    return navbar

from dash import html
import dash_bootstrap_components as dbc


def Footer():
    footer = html.Div(
        html.Div(
            dbc.Row(
                [
                    dbc.Col(
                        [
                            html.Div(
                                "Contato", className="uppercase bold font-xs padding4"
                            ),
                            html.Div(
                                html.A(
                                    "contato.johntor@gmail.com",
                                    href="mailto:contato.johntor@gmail.com",
                                    target="_blank",
                                ),
                                className="padding4",
                            ),
                        ],
                        lg=8,
                        width=12,
                    ),
                    dbc.Col(
                        [
                            html.Div(
                                [
                                    html.Ul(
                                        [
                                            html.Li(
                                                html.A(
                                                    [
                                                        html.I(
                                                            className="fas fa-envelope"
                                                        ),
                                                        html.Span(
                                                            " entre em contato por e-mail"
                                                        ),
                                                    ],
                                                    target="_blank",
                                                    href="mailto:contato.johntor@gmail.com",
                                                ),
                                                className="padding4",
                                            ),
                                            html.Li(
                                                html.A(
                                                    [
                                                        html.I(
                                                            className="fas fa-briefcase"
                                                        ),
                                                        html.Span(
                                                            " faça a proposta de trabalho pela Upwork"
                                                        ),
                                                    ],
                                                    target="_blank",
                                                    href="https://www.upwork.com/ab/flservices/workwith/johntor",
                                                ),
                                                className="padding4",
                                            ),
                                        ]
                                    )
                                ]
                            )
                        ],
                        lg=4,
                        width=12,
                    ),
                ],
                className="padding32",
            ),
            className="primary_bg radius8",
        ),
        className="padding16 default_inverse footer font-sm",
    )

    return footer

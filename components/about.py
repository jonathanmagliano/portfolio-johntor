from dash import html
import dash_bootstrap_components as dbc

def About():
    about = html.Div(
        [
            html.Div(
                [
                    html.H4(
                        "ABOUT", className="font-xl bold letter_spac8 default_inverse"
                    ),
                    html.Div(
                        [
                            dbc.Row(
                                [
                                    dbc.Col(
                                        [
                                            html.Div(
                                                [
                                                    "Somos uma equipe multidisciplinar de alta qualidade com pessoas de distintas habilidades e temos parcerias com muita experiência em construção de negócios, análise de dados, visualizações, análise preditiva, planejamento por pesquisa de mercado, entre outros. Contamos com profissionais dispostos a encontrar as melhores soluções através dos dados. Temos uma visão de como os atuais modelos de negócio funcionam e também pensamos por uma cultura data-driven.",
                                                    html.Br(),
                                                    html.Br(),
                                                    "No momento nós temos parceiros estratégicos distribuídos por regiões percorrendo o Brasil. Buscamos gerar valor através de cada detalhe de forma minuciosa para a satisfação do cliente. Entre em contato conosco e nos conte um pouco sobre o seu problema de negócio e como podemos te ajudar.",
                                                ],
                                                className="font-sm",
                                            ),
                                            html.Div(className="bottom32 dt_hide"),
                                        ],
                                        lg=9,
                                        sm=12,
                                    ),
                                ]
                            ),
                            dbc.Row(
                                dbc.Col(
                                    html.Div(
                                        [
                                            html.Div(
                                                html.A(
                                                    html.I(className="fab fa-linkedin-in"),
                                                    href="https://www.linkedin.com/in/jonathanmagliano",
                                                    target="_blank",
                                                )
                                            ),
                                            html.Div(
                                                html.A(
                                                    html.I(className="fas fa-at"),
                                                    href="https://www.upwork.com/ab/flservices/workwith/johntor",
                                                    target="_blank",
                                                )
                                            ),
                                            html.Div(
                                                html.A(
                                                    html.I(className="fab fa-github "),
                                                    href="https://github.com/jonathanmagliano",
                                                    target="_blank",
                                                )
                                            ),
                                        ],
                                        className="about_logos font-lg",
                                    ),
                                    width=12,
                                )
                            ),
                        ],
                        className="about_content padding32",
                    ),
                ],
                className="terciary_bg radius8 relative about",
            ),
        ],
        className="padding16",
    )
    return about

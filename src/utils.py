import os
from datetime import datetime, timedelta
from pathlib import Path
from typing import Union
import streamlit as st


def login_input() -> Union[str, str]:
    """
    Adiciona o input de usuário e senha para login.

    Returns
    -------
    user, password: Union[str, str]
        O usuário e a senha inseridos pelo usuário.
    """

    st.sidebar.markdown("#### Login")
    user = st.sidebar.text_input("Usuário")
    password = st.sidebar.text_input("Senha", type="password")

    return user, password


def date_input(date_format: str = "DD/MM/YYYY") -> Union[str, str]:
    """
    Adiciona o input de data para seleção do período.

    Parameters
    ----------
    date_format : str, optional
        O formato da data a ser exibido, por padrão é "DD/MM/YYYY".

    Returns
    -------
    start_date, end_date: Union[str, str]
        A data inicial e final selecionadas pelo usuário no formato de string.
    """
    with st.form("Date"):

        start_date = st.date_input(
            "Data inicial", datetime.today() - timedelta(days=3), format=date_format
        )
        end_date = st.date_input(
            "Data final", datetime.today() + timedelta(days=7), format=date_format
        )

        if not end_date >= start_date:
            st.error("Erro: A data final deve ser maior ou igual a inicial.")

        st.form_submit_button("Selecione o período desejado")

        start_date = start_date.strftime("%d/%m/%Y")
        end_date = end_date.strftime("%d/%m/%Y")

        return start_date, end_date


def path_input() -> Path:
    """
    Retorna o caminho para o diretório de downloads.

    Returns
    -------
    download_path : Path
        O caminho para o diretório de downloads.
    """
    download_path = Path(os.path.join(os.getcwd() + "/downloads"))
    return download_path


def all_filled(
    submitted: bool,
    start_date: str,
    end_date: str,
    user: str,
    password: str,
    download_path: Path,
) -> bool:
    """
    Verifica se todos os campos necessários estão preenchidos.

    Parameters
    ----------
    submitted : bool
        Indica se o formulário foi submetido.
    start_date : str
        A data inicial selecionada.
    end_date : str
        A data final selecionada.
    user : str
        O nome de usuário inserido.
    password : str
        A senha inserida.
    download_path : Path
        O caminho para o diretório de downloads.

    Returns
    -------
    filled : bool
        True se todos os campos estiverem preenchidos, False caso contrário.
    """
    return submitted and start_date and end_date and user and password and download_path

from playwright.sync_api import sync_playwright, Playwright
from pathlib import Path
import streamlit as st

import time


from actions import (
    enter_credentials,
    go_to_receipts,
    select_period,
    select_receipt_status,
    get_search_results,
    download_file,
)


def run(
    playwright: Playwright,
    url: str,
    start_date: str,
    end_date: str,
    download_path: Path,
):

    browser = playwright.firefox.launch(headless=False)
    page = browser.new_context(viewport={"width": 1920, "height": 1040}).new_page()
    page.goto(url)

    enter_credentials(page)

    go_to_receipts(page)

    select_period(page, start_date, end_date)

    select_receipt_status(page)

    total_results = get_search_results(page)

    if total_results != 0:
        download_file(page, download_path)

    else:
        st.error(
            "O período escolhido não retornou nenhum resultado. Favor escolher outro período."
        )

    time.sleep(3)


# if __name__ == "__main__":

#     with sync_playwright() as playwright:
#         run(
#             playwright=playwright,
#             url="https://signin.evoluservices.com/",
#             start_date="04/09/23",
#             end_date="27/02/24",
#             download_path="/home/bruno/Downloads/",
#         )

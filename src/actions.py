from src.consts import USER, PASSWORD
from playwright.sync_api import Page
import time
from pathlib import Path


def enter_credentials(page: Page):
    page.wait_for_load_state("load")

    page.locator('//*[@id="j_username"]').fill(USER)
    page.locator('//*[@id="j_password"]').fill(PASSWORD)
    page.click("#btn-login button")

    page.wait_for_load_state("load")

    time.sleep(1)


def go_to_receipts(page: Page):

    page.locator('//*[@id="receipts"]').click()
    page.wait_for_load_state("load")
    time.sleep(2)


def select_period(page: Page, start_date: str, end_date: str):
    page.get_by_label("Data Prevista de Recebimento:").click()
    page.wait_for_selector(".x-combo-list")

    for _ in range(4):
        page.keyboard.press("ArrowDown")
    page.keyboard.press("Enter")

    # Data de ínicio
    page.keyboard.press("Tab")
    page.locator(
        ".x-form-field-wrap.x-form-field-trigger-wrap.evc-periodfield-inicio.x-trigger-wrap-focus input"
    ).fill(start_date)

    # Data final
    page.keyboard.press("Tab")
    page.locator(
        ".x-form-field-wrap.x-form-field-trigger-wrap.evc-periodfield-termino.x-trigger-wrap-focus input"
    ).fill(end_date)


def select_receipt_status(page: Page):
    page.get_by_label("Status do Recebimento:").click()
    page.locator('.x-combo-list-item span:has-text("A Receber")').click()

    page.locator('//div[contains(text(), "Valor selecionado:")]').click()


def get_search_results(page: Page):

    page.get_by_role("button", name="Buscar").click()
    page.wait_for_load_state("load")

    total_results = page.query_selector(
        "td.x-toolbar-cell:nth-child(2) > div.x-form-display-field"
    ).inner_text()

    return int(total_results)


def download_file(page: Page, download_path: Path):

    page.keyboard.press("PageDown")
    page.wait_for_load_state("load")
    page.get_by_role("button", name="Exportar").click()

    time.sleep(1.5)

    with page.expect_download() as download_info:
        page.locator(
            '//div[@class="x-window-footer x-window-footer-noborder x-panel-btns"]//button[text()="Exportar"]'
        ).click()

    download = download_info.value
    download.save_as(download_path + download.suggested_filename)

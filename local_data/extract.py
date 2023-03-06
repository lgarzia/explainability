import datetime
import uuid
from pathlib import Path
from typing import Dict, List, Tuple

import pandas as pd
from splinter.driver.webdriver import WebDriverElement
from splinter.driver.webdriver.chrome import WebDriver


def build_and_save_daily_crash_report(browser: WebDriver, date_data_path: Path) -> Tuple[pd.DataFrame, List[WebDriverElement]]:
    table_list = pd.read_html(browser.html)
    assert len(table_list) == 1
    df_crsh_rpt_list = table_list[0]
    anchors = browser.find_by_tag("table").links.find_by_text('View')
    assert len(anchors) == df_crsh_rpt_list.shape[0]
    append_key_data = []
    for a in anchors:
        append_key_data.append((a['href'], a['href'].split('=')[-1], str(uuid.uuid4())))
    df_crsh_rpt_keys = pd.DataFrame(data=append_key_data, columns=['raw_href', 'acc_rpt_num', 'acc_uuid'])
    df_crsh_rpt_full = pd.merge(df_crsh_rpt_keys, df_crsh_rpt_list, left_index=True, right_index=True)

    path = date_data_path / "daily_crash_report.csv"
    df_crsh_rpt_full.to_csv(path, index=False)
    return df_crsh_rpt_full, anchors

def build_and_save_daily_crash_report_details(browser: WebDriver, date_data_path: Path, record_uuid: str) -> Dict[str, pd.DataFrame]:
    tables = browser.find_by_tag("table")
    df_table_list = pd.read_html(browser.html)
    assert len(tables) == len(df_table_list)
    results = {}
    for i, table in enumerate(tables):
        table_raw_tile = table.find_by_tag("caption").text
        table_clean_title = str.lower(table_raw_tile).replace(' ', '_').replace('.', '_')
        data_title_path = date_data_path / f"{table_clean_title}"
        data_title_path.mkdir(parents=True, exist_ok=True)
        df_table = df_table_list[i]
        df_path = data_title_path / f"{record_uuid}.csv"
        df_table.to_csv(df_path, index=False)
        results[table_clean_title] = df_table
    return results
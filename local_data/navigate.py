import datetime
from typing import Tuple

from splinter.driver.webdriver.chrome import WebDriver


def get_available_date_list(browser: WebDriver) -> Tuple[str, datetime.datetime, str]:
    dates = []
    for d in browser.find_by_xpath("//*[@id='date']/option"):
        if d.text !='':
            raw_str_date = d.text
            datetime_date = datetime.datetime.strptime(d.text, "%B %d, %Y")
            cln_str_date = datetime_date.strftime("%Y-%m-%d")
            dates.append((raw_str_date, datetime_date, cln_str_date))    
    dates = sorted(dates, key=lambda x: x[1], reverse=False)
    return dates

def enter_available_date(browser: WebDriver, date_string:str) -> None:
    date_select = browser.find_by_xpath(f"//*[@id='date']/option[text()='{date_string}']").click()

def search_crash_report(browser: WebDriver):
    browser.find_by_value('Search').click()


from core.driver_factory import get_driver
from pages.example_page import ExamplePage


def run_test():
    driver = get_driver()

    try:
        page = ExamplePage(driver)
        page.open(page.URL)

        title = page.get_title()
        print("Title is:", title)

    finally:
        driver.quit()


if __name__ == "__main__":
    run_test()

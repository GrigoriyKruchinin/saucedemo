from playwright.sync_api import Playwright, sync_playwright

def run(playwright: Playwright) -> None:
    try:
        # Инициализация браузера
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()

        # Открываем сайт saucedemo
        page.goto("https://www.saucedemo.com/")

        # Авторизация
        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")
        page.click("#login-button")

        # Добавляем товар в корзину
        page.click("#add-to-cart-sauce-labs-backpack")

        # Переход в корзину
        page.click(".shopping_cart_link")

        # Проверка наличия товара в корзине
        assert "Sauce Labs Backpack" in page.inner_text(".cart_item")

        # Оформляем покупку
        page.click("#checkout")
        page.fill("#first-name", "Test")
        page.fill("#last-name", "User")
        page.fill("#postal-code", "12345")
        page.click("#continue")
        page.click("#finish")

        # Проверка успешного завершения покупки
        assert "Thank you for your order!" in page.inner_text("h2.complete-header")

        print("Тест прошел успешно!")

    except AssertionError as e:
        print(f"Ошибка утверждения тестов: {e}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
    finally:
        # Закрытие браузера
        if 'browser' in locals():
            browser.close()

with sync_playwright() as playwright:
    run(playwright)

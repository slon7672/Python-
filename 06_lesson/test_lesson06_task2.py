def test_session_storage_auth(browser):

    # 1. Откройте страницу https://gitflic.ru/
    browser.get("https://gitflic.ru/")

    # 2. Установите cookie пользователя 1.
    browser.add_cookie(
        {
            "name": "SESSION",
            "value": "NDkwZDE5ZjYtNzI5Yy00NjFhLWJiNDYtNGUxNGZlOTAwOTNj",
            "domain": "gitflic.ru",
        }
    )

    # Добавляем cookie для окна подтверждения работы с cookie
    browser.add_cookie(
        {
            "name": "cookiesAccepted",
            "value": "true",
            "domain": "gitflic.ru"
        }
    )

    # 3. Обновляем страницу, чтобы cookie применилась
    browser.refresh()

    # 4. Перейдите на страницу пользователя 1.
    browser.get("https://gitflic.ru/user/xoziaka")

    # 5. Сохраните текущий URL.
    url1 = browser.current_url

    # 6. Разлогиньтесь (очистите куки).
    browser.delete_all_cookies()

    # 7. Установите cookie пользователя 2.
    browser.add_cookie(
        {
            "name": "SESSION",
            "value": "MTJhMjMxOWItMzk3MS00MDY2LTg0MzAtNjM4NjNiNWE2Mzc1",
            "domain": "gitflic.ru",
        }
    )

    # Добавляем cookie для окна подтверждения работы с cookie
    browser.add_cookie(
        {
            "name": "cookiesAccepted",
            "value": "true",
            "domain": "gitflic.ru"
        }
    )

    # 8. Обновляем страницу, чтобы cookie применилась
    browser.refresh()

    # 9. Перейдите на страницу пользователя 1.
    browser.get("https://gitflic.ru/user/slon")

    # 10. Сохраните текущий URL.
    url2 = browser.current_url

    # 11. Проверьте, что URL для пользователя 1 и пользователя 2 различаются.
    assert url1 != url2

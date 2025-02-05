from selene import browser, be, query


def test_duckduckgo_should_find_selene(adjust_window_size):
    browser.open('https://duckduckgo.com/')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    required_text = browser.element('[data-testid="result-title-a"]').get(query.text)
    assert required_text == "Selene: User-Oriented Web UI Browser Tests in Python - GitHub Pages"
    browser.quit()

def test_that_duckduckgo_have_empty_result(adjust_window_size):
    browser.open('https://duckduckgo.com/')
    browser.element('[name="q"]').should(be.blank).type('@$#@$@').press_enter()
    result = browser.element('//*[@data-area="mainline"]//*[contains(text(), "No results found for")]').get(query.text)
    assert result == "No results found for @$#@$@."
    browser.quit()

def test_iframe(page):
    page.goto(
        "https://www.w3schools.com/html/tryit.asp?filename=tryhtml_iframe_height_width"
    )
    iframe = page.frame_locator("#iframeResult")
    inner_iframe = iframe.frame_locator('[src="demo_iframe.htm"]')
    texto = inner_iframe.locator("h1").inner_text()
    print(texto)

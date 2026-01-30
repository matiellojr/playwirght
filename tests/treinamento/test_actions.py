# def test_click(page):
#     page.goto("https://automationexercise.com")
#     page.pause()
#     # page.get_by_role("link", name="Website for automation").click(button="right")
#     # page.get_by_role("link", name="Website for automation").click(position={"x": 50, "y": 70})
#     page.get_by_role("link", name="(6) Polo").click()
#     page.get_by_role("link", name="(6) Polo").click(modifiers=["Control"]) # Open in new tab navegator
#     page.get_by_role("link", name="(6) Polo").click(button="right") # Right click


# def test_click(page):
#     page.goto("https://bootswatch.com/default/")
#     page.pause()
#     page.get_by_role('button', name='Primary').nth(1).click(force=True)


# def test_fill(page):
#     page.goto("https://automationexercise.com/login")
#     page.pause()
#     page.get_by_role("textbox", name="Name").fill("Junior", timeout=1000)
#     page.locator("form").filter(has_text="Signup").get_by_placeholder("Email Address").fill("Teste@teste.com")
#     page.get_by_role("button", name="Signup").click()

# def test_check_uncheck(page):
#     page.goto("https://bootswatch.com/default/")
#     page.pause()
#     page.get_by_role("checkbox", name="Default checkbox").check()
#     page.get_by_role("checkbox", name="Checked checkbox").uncheck()
#     page.pause()

# def test_select_option(page): 
#     page.goto("https://bootswatch.com/default/")
#     page.pause()
#     page.get_by_label("Example select").select_option("2")
#     page.get_by_label("Example multiple select").select_option(["1", "3", "4"])
    
# def test_press(page): 
#     page.goto("https://bootswatch.com/default/")
#     page.pause()
#     page.get_by_placeholder("name@example.com").fill("Email.email@teste.com")
#     page.get_by_placeholder("name@example.com").press("Tab")
#     page.keyboard.type("Space")

# def test_press_2(page): 
#     page.goto("https://bootswatch.com/default/")
#     page.pause()
#     page.get_by_role("textbox", name="Example textarea").click()
#     page.get_by_placeholder("name@example.com").click()
#     page.get_by_role("textbox", name="Example textarea").click()
#     page.get_by_role("textbox", name="Example textarea").fill(" teste teste teste")
#     page.get_by_role("textbox", name="Example textarea").press("Home")
#     page.get_by_role("textbox", name="Example textarea").fill("teste teste teste")
#     page.get_by_role("textbox", name="Example textarea").press("End")
#     page.get_by_role("textbox", name="Example textarea").press("ControlOrMeta+a")
#     page.get_by_role("textbox", name="Example textarea").press("ControlOrMeta+c")
#     # page.get_by_placeholder("name@example.com").click()
#     page.get_by_placeholder("name@example.com").press("ControlOrMeta+v")
#     page.pause()

# def test_type(page): 
#     page.goto("https://bootswatch.com/default/")
#     page.pause()
#     # ir até area de texto
#     page.get_by_role("textbox", name="Example textarea").click()
#      # type digita caracter por caracter, diferente do fill que preenche todo o campo de uma vez e rapido
#     page.get_by_role("textbox", name="Example textarea").type("lorem ipsum lorem ipsum lorem ipsum")
#     page.get_by_role("textbox", name="Example textarea").press("Enter")
#      # type digita caracter por caracter, diferente do fill que preenche todo o campo de uma vez e devagar    
#     page.get_by_role("textbox", name="Example textarea").type("lorem ipsum lorem ipsum lorem ipsum", delay=500)


# def test_hover(page): 
#     page.goto("https://automationexercise.com/")
#     page.pause()
#     page.locator(".single-products:visible").filter(has_text="Madame Top For Women").click()
#     page.locator(".single-products:visible").filter(has_text="Madame Top For Women").hover()
#     page.locator("div:nth-child(9) > .product-image-wrapper > .single-products > .product-overlay > .overlay-content > .btn").click()


# def test_dblclick(page): 
#     page.goto("https://automationexercise.com/login")
#     page.pause()
#     page.locator(".login-form h2").dblclick()



# from playwright.sync_api import expect
# def test_expect(page): 
#     page.goto("https://automationexercise.com/")
#     page.pause()
#     page.locator(".single-products:visible").filter(has_text="Madame Top For Women").click()
#     page.locator(".single-products:visible").filter(has_text="Madame Top For Women").hover()
#     page.locator("div:nth-child(9) > .product-image-wrapper > .single-products > .product-overlay > .overlay-content > .btn").click()
#     expect(page.locator("#cartModal")).to_contain_text('Your product has been added to cart.', timeout=10000)
#     # expect(page.locator("#cartModal")).to_contain_text('Your product has been addeeeed to cart.', timeout=10000)
#     # expect(page.get_by_role("button", name="Continue Shoppingssssssssss")).to_be_visible()
#     expect(page.get_by_role("button", name="Continue Shopping")).to_be_visible()
#     expect(page.get_by_role("button", name="Continue Shopping")).to_be_enabled()
#     page.get_by_role("button", name="Continue Shopping").click()
#     expect(page.locator("#cartModal")).not_to_be_visible()
#     expect(page.get_by_role("heading", name="AutomationExercise")).to_be_visible()
#     page.get_by_role("button", name="Test Cases").click()
#     page.get_by_role("link", name="Website for practice").click()
#     page.get_by_role("img", name="demo website for practice").click()
#     expect(page.get_by_role("heading", name="Features Items")).to_be_visible()
#     expect(page.get_by_role("link", name="Website for automation")).to_be_visible()
#     expect(page.get_by_role("listitem").filter(has_text="Video Tutorials")).to_be_visible()
#     expect(page.locator("#header")).to_contain_text("Products")
#     expect(page.locator("body")).to_contain_text("Features Items")
#     expect(page.get_by_role("link", name=" Women")).to_be_visible()
#     expect(page.get_by_role("heading", name=" Women")).to_be_visible()



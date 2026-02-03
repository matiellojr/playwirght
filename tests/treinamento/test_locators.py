# def test_get_by_role(page):
# page.goto("https://automationexercise.com/")
# page.pause()
# page.get_by_role("link", name="Signup / Login").click()
# page.get_by_role("button", name="Login").click()

# page.goto("https://bootswatch.com/default/")
# page.pause()
# page.locator("#navbarColor01").get_by_role("button", name="Dropdown").click()


# def test_get_by_text(page):
#     page.goto("https://automationexercise.com/")
#     page.pause()
#     # page.get_by_text("Full-Fledged practice website for Automation Engineers").click()
#     # page.get_by_text("Full-Fledged practice website for Automation Engineers").first.click()
#     # page.get_by_text("Full-Fledged practice website for Automation Engineers", exact=True).first.click()
#     page.get_by_text("Full-Fledged practice website for ", exact=True).first.click()


# O parâmetro exact=True garante que o texto do label seja igual ao informado, sem variações.
# Sem o exact=True, pode encontrar textos parecidos ou que contenham o termo buscado.

# def test_get_by_label(page):
#     page.goto("https://bootswatch.com/default/")
#     page.pause()
#     page.get_by_label("Valid input", exact=True).fill("Teste")
#     # page.get_by_label("Valid Input").fill("Teste")
#     page.get_by_label("Recipient's username", exact=True).fill("Teste")


# def test_get_by_placeholder(page):
#     page.goto("https://automationexercise.com/login")
#     page.pause()
#     page.get_by_placeholder("Name").fill("Teste")
#     page.locator("form").filter(has_text="Signup").get_by_placeholder("Email Address").fill("Teste")
#     # page.get_by_placeholder("Email Address").fill("Teste")


# def test_get_by_title(page):
#     page.goto("https://bootswatch.com/default/")
#     page.pause()
#     page.get_by_title("Source Title").nth(1).click()

# def test_locator_css(page):
#     page.goto("https://automationexercise.com")
#     page.pause()
#     page.locator("#accordian .panel-title").first.click()

import os
import pytest
import pytest_html
from slugify import slugify  # pip install python-slugify


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
	"""
    Este hook é executado após cada fase do teste.
	Usamos ele para verificar falhas e anexar capturas de tela ao relatório HTML.
	"""
	outcome = yield
	report = outcome.get_result()
	# Lista de extras para o relatório HTML
	extras = getattr(report, "extra", [])
	# Só captura na fase 'call' (execução do teste em si)
	if report.when == "call":
		xfail = hasattr(report, "wasxfail")
		try:
			# Captura quando falha (mas não é um XFAIL esperado)
			if (report.skipped and xfail) or (report.failed and not xfail):
				# Garante nome de arquivo seguro
				screenshots_dir = "imagens"
				os.makedirs(screenshots_dir, exist_ok=True)
				screen_file = os.path.join(
					screenshots_dir, f"{slugify(item.nodeid)}.png"
				)
				# page deve estar disponível no teste (fixture do Playwright)
				page = item.funcargs.get("page")
				if page:
					page.screenshot(path=screen_file, full_page=True)
					extras.append(pytest_html.extras.png(screen_file))
		except Exception as e:
			print(f"Erro ao capturar imagem: {e}")
	report.extra = extras
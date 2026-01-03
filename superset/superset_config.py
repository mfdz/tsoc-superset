FEATURE_FLAGS = {
    "ENABLE_TEMPLATE_PROCESSING": True,
}

ENABLE_PROXY_FIX = True
SECRET_KEY = "YOUR_OWN_RANDOM_GENERATED_STRING"

# To allow sqlite, wee need to enable unsafe db connections
PREVENT_UNSAFE_DB_CONNECTIONS = False
# Requires running pybabel compile -d superset/translations
LANGUAGES = { "de": {"flag": "de", "name": "Deutsch"}, "en": {"flag": "us", "name": "English"}}

# TODO: replace for prod
TALISMAN_ENABLED = False

APP_NAME = "Dashboard DELFI zHV / OpenStreetMap Haltestellenabgleich"
FAVICONS = [{"href": "https://mfdz.de/favicon.ico"}]
APP_ICON = "https://mfdz.de/media/site/3469423397-1603810793/schriftzug-path-lg.svg"

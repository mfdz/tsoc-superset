FEATURE_FLAGS = {
    "ENABLE_TEMPLATE_PROCESSING": True,
}

ENABLE_PROXY_FIX = True
SECRET_KEY = "YOUR_OWN_RANDOM_GENERATED_STRING"

# Grant Public Role the right to view dashboards.
# Note: This still requires (currently manually) granting database access to user Public
PUBLIC_ROLE_LIKE = "Guest_template"

# To allow duckdb, wee need to enable unsafe db connections
PREVENT_UNSAFE_DB_CONNECTIONS = False
# Requires running pybabel compile -d superset/translations
LANGUAGES = { "de": {"flag": "de", "name": "Deutsch"}, "en": {"flag": "us", "name": "English"}}

# For more information on TALISMAN setup, see https://superset.apache.org/docs/security/
TALISMAN_ENABLED = True

TALISMAN_CONFIG = {
    "content_security_policy": {
        "base-uri": ["'self'"],
        "default-src": ["'self'"],
        "img-src": [
            "'self'",
            "blob:",
            "data:",
            "https://apachesuperset.gateway.scarf.sh",
            "https://static.scarf.sh/",
            "ows.terrestris.de",
            "mfdz.de",
            "data.mfdz.de",
        ],
        "worker-src": ["'self'", "blob:"],
        "connect-src": [
            "'self'",
            "https://api.mapbox.com",
            "https://events.mapbox.com",
        ],
        "object-src": "'none'",
        "style-src": [
            "'self'",
            "'unsafe-inline'",
        ],
        "script-src": ["'self'", "'strict-dynamic'"],
    },
    "content_security_policy_nonce_in": ["script-src"],
    "force_https": False,
    "session_cookie_secure": False,
}
THEME_DEFAULT = {
    "token": {
        "fontFamily": "'Inter', Helvetica, Arial",
        "brandLogoUrl" : "https://mfdz.de/media/site/3469423397-1603810793/schriftzug-path-lg.svg",
        # ... other tokens
    },
    # ... other theme properties
}
THEME_DARK = {
    "algorithm": "dark",
    "token": {
        "fontFamily": "'Inter', Helvetica, Arial",
        "brandLogoUrl" : "https://data.mfdz.de/img/mitfahrdezentrale-weiss.svg",
        # ... other tokens
    },
    # ... other theme properties
}
APP_NAME = "Dashboard DELFI zHV / OpenStreetMap Haltestellenabgleich"
FAVICONS = [{"href": "https://mfdz.de/favicon.ico"}]

BABEL_DEFAULT_LOCALE = "de"


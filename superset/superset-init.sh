#!/bin/bash

# create Admin user, you can read these values from env or anywhere else possible
superset fab create-admin --username "$ADMIN_USERNAME" --firstname Superset --lastname Admin --email "$ADMIN_EMAIL" --password "$ADMIN_PASSWORD"

# create custom role(s), i.e. Guest_template which will be assigned to Public using PUBLIC_ROLE_LIKE
# (Inspired by the geOrchestra superset project, https://github.com/georchestra/superset)
superset fab import-roles -p /app/config/stops_custom_roles.json

# Upgrading Superset metastore
superset db upgrade

# setup roles and permissions
superset superset init

# import dashboards
# Note: import-directory does not accept an owning user. To be able to edit the imported dashboards/charts, you'll need to assign them an owning user.
superset import-directory --overwrite /dashboards/dashboard_kreis
superset import-directory --overwrite /dashboards/dashboard_deutschland

# Starting server
/bin/sh -c /usr/bin/run-server.sh

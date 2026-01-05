FROM apache/superset:v5.0.0

USER root

ENV ADMIN_USERNAME=$ADMIN_USERNAME
ENV ADMIN_EMAIL=$ADMIN_EMAIL
ENV ADMIN_PASSWORD=$ADMIN_PASSWORD

RUN . /app/.venv/bin/activate && \
    uv pip install \
    duckdb==1.4.3 \
    duckdb-engine==0.17.0

COPY ./superset-init.sh /superset-init.sh
RUN chmod 0755 /superset-init.sh

COPY superset_config.py /app/
ENV SUPERSET_CONFIG_PATH=/app/superset_config.py

USER superset
ENTRYPOINT [ "/superset-init.sh" ]

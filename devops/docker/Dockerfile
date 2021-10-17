ARG pyversion=3.9
FROM python:${pyversion}-bullseye
ARG pyversion=3.9
ENV PYVERSION ${pyversion:-3.9}

# Install packages
RUN apt-get -yqq update && \
    apt-get -yqq install apache2 apache2-dev locales && \
    apt-get clean

# Prepare virtualenv
RUN mkdir /app
WORKDIR /app
RUN python -m venv ./virtualenv
RUN ./virtualenv/bin/pip install --upgrade pip setuptools

# Install mod_wsgi
RUN ./virtualenv/bin/pip install mod_wsgi
RUN ln -s /app/virtualenv/lib/python$PYVERSION/site-packages/mod_wsgi/server/mod_wsgi-*.so /app/virtualenv/lib/python$PYVERSION/site-packages/mod_wsgi/server/mod_wsgi.so

# Prepare app directory
RUN mkdir ./pylibs

# Configure Apache
COPY ./config/apache/start-apache.sh /
COPY ./config/mod_wsgi/wsgi.conf.tmpl /tmp/wsgi.conf.tmpl
RUN a2dismod mpm_event && a2enmod mpm_prefork
RUN sed -e s/\$PYVERSION/$PYVERSION/g /tmp/wsgi.conf.tmpl | sed -e s/\$PYV/`echo $PYVERSION | sed -e "s/\\.//"`/g >/etc/apache2/mods-enabled/wsgi.conf
ONBUILD COPY apache.conf /etc/apache2/sites-available/000-default.conf

# Start Apache
EXPOSE 80
CMD ["/bin/sh", "/start-apache.sh"]
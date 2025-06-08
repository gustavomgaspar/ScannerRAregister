FROM php:8.3-apache


# Set timezone
ENV TZ=${TZ:-UTC}
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Install necessary packages and PHP extensions
RUN apt-get update && apt-get install -y \
        zip \
        libzip-dev \
        libfreetype6-dev \
        libjpeg62-turbo-dev \
        libpng-dev \
        libwebp-dev \
    && docker-php-ext-configure gd --with-freetype --with-jpeg --with-webp \
    && docker-php-ext-install -j$(nproc) mysqli pdo pdo_mysql opcache zip gd 

# Set ServerName to suppress the warning
RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf

# Allow directory listing
RUN echo "<Directory /var/www/html/>" >> /etc/apache2/apache2.conf \
    && echo "    Options Indexes FollowSymLinks" >> /etc/apache2/apache2.conf \
    && echo "    AllowOverride None" >> /etc/apache2/apache2.conf \
    && echo "    Require all granted" >> /etc/apache2/apache2.conf \
    && echo "</Directory>" >> /etc/apache2/apache2.conf
RUN apt-get install -y zlib1g-dev libicu-dev g++ \
    && docker-php-ext-configure intl \
    && docker-php-ext-install intl
# Adjust permissions and ownership
RUN chown -R www-data:www-data /var/www/html 
RUN chmod -R 755 /var/www/html

# Copy php.ini configuration
COPY ./php.ini ${PHP_INI_DIR}/conf.d/99-php.ini

# Restart Apache to apply changes
RUN service apache2 restart

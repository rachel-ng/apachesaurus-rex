# apachesaurus rex

you know there's an honest to god Problem™ when you've memorized most of these


### apache stuff

```
$ sudo a2ensite ambrosia.conf
```

```
$ sudo a2dissite 000-default.conf
```

```
$ service apache2 reload
```

```
$ service apache2 restart
```

### /var/www/ambrosia

```
$ cd /var/www/ambrosia
```

```
$ nano /var/www/ambrosia/ambrosia.wsgi
```

### /etc/apache2/sites-available

```
$ cd /etc/apache2/sites-available
```

```
$ nano /etc/apache2/sites-available/ambrosia.conf
```

### check your error logs and stuff

```
$ sudo cat /var/log/apache2/error.log
```

```
$ sudo tail /var/log/apache2/access.log -f
```

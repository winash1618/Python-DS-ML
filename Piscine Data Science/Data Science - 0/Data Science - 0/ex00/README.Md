- https://www.digitalocean.com/community/tutorials/how-to-install-postgresql-on-ubuntu-22-04-quickstart
- https://medium.com/coding-blocks/creating-user-database-and-adding-access-on-postgresql-8bfcd2f4a91e

```bash
sudo apt update
sudo apt install postgresql postgresql-contrib
```
- important commands
```bash
sudo -u postgres psql
sudo -u postgres createuser --interactive
sudo -u postgres createdb <db_name>
sudo -u postgres psql
psql=# alter user <username> with encrypted password '<password>';
psql=# grant all privileges on database <dbname> to <username> ;
```
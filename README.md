## Put.io Sync

Simple script to sync files between put.io downloads and local storage. It uses a small database to keep track of already downloaded files, so that the same file is never downloaded twice (even if it's deleted or moved).

## Requirements

- Sqlite
- Python 2.x (see python required libraries in requirements.txt)

## Getting Started

Create a sqlite database:

```
sqlite3 putio.db

> CREATE TABLE downloads (id int, name string);
> .q
```

Create a file config.yml with your settings (see config.yml.sample)

## License

putio-sync is released under the [MIT License](http://www.opensource.org/licenses/MIT).


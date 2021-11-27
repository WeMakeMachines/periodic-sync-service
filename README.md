# Periodic Sync Service

A service which can be configured to periodically make a GET request to a URL, and save the response to a **memcached** server

## Configuration

1. Create a `config.ini` (use `example_config.ini` as a base)
2. Add the server location of your **memcached** server
    > Example: For a UNIX socket connection `/run/memcached/memcached.sock`

    > Example: For a TCP connection `127.0.0.1`
3. Create a new section for your request
4. Add the keys `url` and `interval` to your new section
    > Interval must be supplied in seconds

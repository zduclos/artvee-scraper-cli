# artvee-scraper-cli

 **artvee-scraper-cli** is an easy to use command line utility for fetching public domain artwork from Artvee (https://www.artvee.com).

- [Artvee Web-scraper CLI](#artvee-scraper-cli)
  - [Installation](#installation)
  - [Synopsis](#synopsis)
  - [Examples](#examples)
  - [Available Commands](#available-commands)

## Installation

Using PyPI
```console
$ python -m pip install artvee-scraper-cli
```
Python 3.10+ is officially supported.

## Synopsis
```console
artvee-scraper-cli <command> [optional arguments] [positional arguments]
```

## Examples
View help
```console
$ artvee-scraper-cli -h
usage: artvee-scraper-cli [-h] {log-json,file-json,file-multi} ...

Scrape artwork from https://www.artvee.com

positional arguments:
  {log-json,file-json,file-multi}
    log-json            Artwork is output to the log as a JSON object
    file-json           Artwork is represented as a JSON object and written to a file
    file-multi          Artwork image and metadata are written as separate files

optional arguments:
  -h, --help            show this help message and exit
```

View help for the *file-json* command
```console
$ artvee-scraper-cli file-json -h
usage: artvee-scraper-cli file-json [-h] [-t [1-10]] [-l {DEBUG,INFO,WARNING,ERROR,CRITICAL}]
                    [-c {abstract,figurative,landscape,religion,mythology,posters,animals,illustration,still-life,botanical,drawings,asian-art}]
                    [--log-dir LOG_DIR] [--log-max-size [1-10240]] [--log-max-backups [0-100]]
                    [--space-level [2-6]] [--sort-keys] [--overwrite-existing]
                    dir_path

positional arguments:
  dir_path              JSON file output directory

optional arguments:
  -h, --help            show this help message and exit
  -t [1-10], --worker-threads [1-10]
                        Number of worker threads (1-10)
  -l {DEBUG,INFO,WARNING,ERROR,CRITICAL}, --log-level {DEBUG,INFO,WARNING,ERROR,CRITICAL}
                        Set the application log level
  -c {abstract,figurative,landscape,religion,mythology,posters,animals,illustration,still-life,botanical,drawings,asian-art}, --category {abstract,figurative,landscape,religion,mythology,posters,animals,illustration,still-life,botanical,drawings,asian-art}
                        Category of artwork to scrape
  --space-level [2-6]   Enable pretty-printing; number of spaces to indent (2-6)
  --sort-keys           Sort JSON keys in alphabetical order
  --overwrite-existing  Overwrite existing files

optional log file arguments:
  --log-dir LOG_DIR     Log file output directory
  --log-max-size [1-10240]
                        Maximum log file size in MB (1-10,240)
  --log-max-backups [0-100]
                        Maximum number of log files to keep (0-100)
```

Download artwork from *artvee.com* and save each as individal files (JSON format) in the directory *~/artvee/downloads*
```console
$ artvee-scraper-cli file-json ~/artvee/downloads
```

## Available Commands
- [log-json](#log-json)
- [file-json](#file-json)
- [file-multi](#file-multi)

## log-json
Download artwork and output each to the log as a JSON objects.
Note: This command is intended for development test usage; typically it is not desirable to dump the data to the log.
```console
$ artvee-scraper-cli log-json [optional arguments]
```

###### Optional arguments
> `-h` | `--help` (boolean)
>> Display help message.

> `-t` | `--worker-threads` (integer)
>> The number of worker threads used for processing. Range of values is [1-10]. The default value is *3*.

> `-l` | `--log-level` (string)
>> Application log level. One of: **DEBUG, INFO, WARNING, ERROR, CRITICAL**. The default value is *INFO*.

>`-c` | `--category` (string)
>> Category of artwork to fetch. One of: **abstract, figurative, landscape, religion, mythology, posters, animals, illustration, still-life,  botanical, drawings, asian-art**. May be repeatedly used to specify multiple categories (*-c animals, -c drawings*). The default value is *ALL*   categories.

###### Optional log file arguments
> `--log-dir` (string)
>> Path to existing directory used to store *artvee_scraper.log* log files. Disabled by default.

> `--log-max-size` (integer)
>> Maximum size in MB the log file should reach before triggering a rollover. Only applies if *--log-dir* has been specified. Range of values is [1-10240]. The default value is *1024*MB (1GB).

> `--log-max-backups` (integer)
>> Maximum number of log file archives to keep. Only applies if *--log-dir* has been specified. The actively written file is *artvee_scraper.log*. Backup files will have an incrementing numerical suffix; *artvee_scraper.log.1 ... artvee_scraper.log.N*. If this value is zero, rollovers will be disabled. Range of values is [0-100]. The default value is *10*.

###### Optional writer arguments
> `--space-level` (integer)
>> Pretty print JSON; number of spaces to indent. Range of values is [2-6]. Disabled by default.

> `--sort-keys` (boolean)
>> Sort JSON keys in alphabetical order. Disabled by default.

> `--include-image` (boolean)
>> Image will be included in output. Excessive output warning! Disabled by default.


###### Basic Example
```console
$ artvee-scraper-cli log-json
```
###### Output:
```console
  ...
2038-01-19 18:34:38.941 INFO [ThreadPoolExecutor-0_0] runner.<lambda>(79) | Processing 'Komposition' by Otto Freundlich
2038-01-19 18:34:38.943 INFO [ThreadPoolExecutor-0_0] log_writer.write(45) | {"url": "https://artvee.com/dl/komposition-2/", "resource": "komposition-2", "title": "Komposition", "category": "Abstract", "artist": "Otto Freundlich", "date": "1938", "origin": "German, 1878-1943", "image": {"source_url": "https://mdl.artvee.com/sdl/102399absdl.jpg", "width": 1423, "height": 1800, "file_size": 1.1, "file_size_unit": "MB", "format_name": "jpg"}}
  ...
```

###### Advanced Example
```console
$ artvee-scraper-cli log-json --worker-threads 2 --log-level DEBUG --category abstract --log-dir /var/log/artvee --log-max-size 2048 --log-max-backups 10 --space-level 2 --sort-keys --include-image
```
###### Output:
```console
$ cat /var/log/artvee/artvee_scraper_cli.log
  ...
2038-01-19 18:40:11.772 DEBUG [ThreadPoolExecutor-0_0] artvee_client.get_image(132) | Retrieving image; url=https://mdl.artvee.com/sdl/105042absdl.jpg
2038-01-19 18:40:11.772 DEBUG [ThreadPoolExecutor-0_0] connectionpool._new_conn(1051) | Starting new HTTPS connection (1): mdl.artvee.com:443
2038-01-19 18:40:11.853 DEBUG [ThreadPoolExecutor-0_0] connectionpool._make_request(546) | https://mdl.artvee.com:443 "GET /sdl/105042absdl.jpg HTTP/11" 200 2011451
2038-01-19 18:40:11.941 INFO [ThreadPoolExecutor-0_0] runner.<lambda>(79) | Processing 'Gare' by Joaquín Torres-García
2038-01-19 18:40:11.967 INFO [ThreadPoolExecutor-0_0] log_writer.write(45) | {
  "artist": "Joaquín Torres-García",
  "category": "Abstract",
  "date": "1928",
  "image": {
    "file_size": 1.92,
    "file_size_unit": "MB",
    "format_name": "jpg",
    "height": 1259,
    "raw": "/9j/4AAQSkZJRgABA ... o4xSSSVkumh//9k=",
    "source_url": "https://mdl.artvee.com/sdl/105042absdl.jpg",
    "width": 1800
  },
  "origin": "Uruguayan, 1874-1949",
  "resource": "gare",
  "title": "Gare",
  "url": "https://artvee.com/dl/gare/"
}
  ...
```

## file-json
Download artwork and write each to the filesystem. Each artwork is stored as a JSON object.
```console
$ artvee-scraper-cli file-json [optional arguments] <dir_path>
```

###### Positional arguments
> `dir_path` (string) Position *0*.
>> Path to existing directory used to store output files.

###### Optional arguments
> `-h` | `--help` (boolean)
>> Display help message.

> `-t` | `--worker-threads` (integer)
>> The number of worker threads used for processing. Range of values is [1-10]. The default value is *3*.

> `-l` | `--log-level` (string)
>> Application log level. One of: **DEBUG, INFO, WARNING, ERROR, CRITICAL**. The default value is *INFO*.

>`-c` | `--category` (string)
>> Category of artwork to fetch. One of: **abstract, figurative, landscape, religion, mythology, posters, animals, illustration, still-life,  botanical, drawings, asian-art**. May be repeatedly used to specify multiple categories (*-c animals, -c drawings*). The default value is *ALL*   categories.

###### Optional log file arguments
> `--log-dir` (string)
>> Path to existing directory used to store *artvee_scraper.log* log files. Disabled by default.

> `--log-max-size` (integer)
>> Maximum size in MB the log file should reach before triggering a rollover. Only enabled if *--log-dir* has been specified. Range of values is [1-10240]. The default value is *1024*MB (1GB).

> `--log-max-backups` (integer)
>> Maximum number of log file archives to keep. Only enabled if *--log-dir* has been specified. The actively written file is *artvee_scraper.log*. Backup files will have an incrementing numerical suffix; *artvee_scraper.log.1 ... artvee_scraper.log.N*. If this value is zero, rollovers will be disabled. Range of values is [0-100]. The default value is *10*.

###### Optional writer arguments
> `--space-level` (integer)
>> Pretty print JSON; number of spaces to indent. Range of values is [2-6]. Disabled by default.

> `--sort-keys` (boolean)
>> Sort JSON keys in alphabetical order. Disabled by default.

> `--overwrite-existing` (boolean)
>> Allow existing duplicate files to be overwritten. Disabled by default.

###### Basic Example
```console
$ artvee-scraper-cli file-json ~/artvee/downloads
```
###### Output:
```console
$ cat ~/artvee/downloads/woman-by-the-window.json
{"url": "https://artvee.com/dl/woman-by-the-window/", "resource": "woman-by-the-window", "title": "Woman by the window", "category": "Abstract", "artist": "Mikuláš Galanda", "date": "1928", "origin": "Slovak, 1895 – 1938", "image": {"source_url": "https://mdl.artvee.com/sdl/101518absdl.jpg", "width": 1317, "height": 1800, "file_size": 2.48, "file_size_unit": "MB", "raw": "/9j/4AAQSkZJRgAB ... aK1lZLTp7i/Vn//Z", "format_name": "jpg"}}
```

###### Advanced Example
```console
$ artvee-scraper-cli file-json ~/artvee/downloads --worker-threads 1 --log-level INFO --category mythology --log-dir /var/log/artvee --log-max-size 512 --log-max-backups 10 --space-level 4 --sort-keys --overwrite-existing
```
###### Output:
```console
$ cat ~/artvee/downloads/the-judgment-of-paris-3.json
{
    "artist": "Joachim Wtewael",
    "category": "Mythology",
    "date": "1602",
    "image": {
        "file_size": 7.42,
        "file_size_unit": "MB",
        "format_name": "jpg",
        "height": 2138,
        "raw": "/9j/4R8FRXhpZgAASUkq ... /pNfu/+89V/wB46//Z",
        "source_url": "https://mdl.artvee.com/sdl/400408mtsdl.jpg",
        "width": 2833
    },
    "origin": "Dutch, 1566 - 1638",
    "resource": "the-judgment-of-paris-3",
    "title": "The Judgment of Paris",
    "url": "https://artvee.com/dl/the-judgment-of-paris-3/"
}
```

## file-multi
Download artwork and write each to the filesystem. Each artwork is stored as two files: metadata (JSON) & image (JPG).
```console
$ artvee-scraper-cli file-multi [optional arguments] <metadata_dir_path> <image_dir_path>
```

###### Positional arguments
> `metadata_dir_path` (string) Position *0*.
>> Path to existing directory used to store output metadata files.

> `image_dir_path` (string) Position *1*.
>> Path to existing directory used to store output image files.

###### Optional arguments
> `-h` | `--help` (boolean)
>> Display help message.

> `-t` | `--worker-threads` (integer)
>> The number of worker threads used for processing. Range of values is [1-10]. The default value is *3*.

> `-l` | `--log-level` (string)
>> Application log level. One of: **DEBUG, INFO, WARNING, ERROR, CRITICAL**. The default value is *INFO*.

> `-c` | `--category` (string)
>> Category of artwork to fetch. One of: **abstract, figurative, landscape, religion, mythology, posters, animals, illustration, still-life,  botanical, drawings, asian-art**. May be repeatedly used to specify multiple categories (*-c animals -c drawings*). The default value is *ALL*   categories.

###### Optional log file arguments
> `--log-dir` (string)
>> Path to existing directory used to store *artvee_scraper.log* log files. Disabled by default.

> `--log-max-size` (integer)
>> Maximum size in MB the log file should reach before triggering a rollover. Only enabled if *--log-dir* has been specified. Range of values is [1-10240]. The default value is *1024*MB (1GB).

> `--log-max-backups` (integer)
>> Maximum number of log file archives to keep. Only enabled if *--log-dir* has been specified. The actively written file is *artvee_scraper.log*. Backup files will have an incrementing numerical suffix; *artvee_scraper.log.1 ... artvee_scraper.log.N*. If this value is zero, rollovers will be disabled. Range of values is [0-100]. The default value is *10*.

###### Optional writer arguments
> `--space-level` (integer)
>> Pretty print JSON; number of spaces to indent. Range of values is [2-6]. Disabled by default.

> `--sort-keys` (boolean)
>> Sort JSON keys in alphabetical order. Disabled by default.

> `--overwrite-existing` (boolean)
>> Allow existing duplicate files to be overwritten. Disabled by default.

###### Basic Example
```console
$ artvee-scraper-cli file-multi ~/artvee/downloads/metadata ~/artvee/downloads/images
```
###### Output:
```console
$ cat ~/artvee/downloads/metadata/the-pet-pig.json
{"url": "https://artvee.com/dl/the-pet-pig/", "resource": "the-pet-pig", "title": "The pet pig", "category": "Abstract", "artist": "Edvard Munch", "date": "1908-1910", "origin": "Norwegian, 1863 - 1944", "image": {"source_url": "https://mdl.artvee.com/sdl/103755absdl.jpg", "width": 1800, "height": 1320, "file_size": 1.67, "file_size_unit": "MB", "format_name": "jpg"}}
$ hexdump -C ~/artvee/downloads/images/the-pet-pig.jpg
00000000  ff d8 ff e0 00 10 4a 46  49 46 00 01 01 01 01 2c  |......JFIF.....,|
  ...
001aa430  40 2b 9c 02 8a 2b 48 b6  d6 bd ff 00 c8 0f ff d9  |@+...+H.........|
001aa440
```

###### Advanced Example
```console
$ artvee-scraper-cli file-multi --worker-threads 1 --log-level INFO --category asian-art --log-dir /var/log/artvee --log-max-size 512 --log-max-backups 10 --space-level 2 --sort-keys --overwrite-existing ~/artvee/downloads/metadata ~/artvee/downloads/images
```
###### Output:
```console
$ cat ~/artvee/downloads/metadata/two-ronin-looking-into-yoshiwara.json
{
  "artist": "Andō Hiroshige",
  "category": "Asian-art",
  "date": "19th century",
  "image": {
    "file_size": 2.29,
    "file_size_unit": "MB",
    "format_name": "jpg",
    "height": 1179,
    "source_url": "https://mdl.artvee.com/sdl/52015jpsdl.jpg",
    "width": 1800
  },
  "origin": "Japanese, 1797 – 1858",
  "resource": "two-ronin-looking-into-yoshiwara",
  "title": "Two Ronin Looking into Yoshiwara",
  "url": "https://artvee.com/dl/two-ronin-looking-into-yoshiwara/"
}
$ hexdump -C ~/artvee/downloads/images/two-ronin-looking-into-yoshiwara.jpg
00000000  ff d8 ff e0 00 10 4a 46  49 46 00 01 01 01 01 2c  |......JFIF.....,|
  ...
002499c0  a2 b4 fe bf ad cc 4f ff  d9                       |......O..|
002499c9
```

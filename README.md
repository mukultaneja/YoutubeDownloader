
# YoutubeDownloader

**YoutubeDownloader** is an automated service to download multiple youtube videos at a time.

## About

**YoutubeDownloader** is written in `Python`. It uses ``Asynchronous Python Multiprocessing`` at its heart which facilitates user to download more than one video at a time.


**YoutubeDownloader** must use a configuration file. It supports a YAML / JSON format of configuration file. This configuration file gives structure and usability to the service. It defines what **videos/playlists** needs to be downloaded and how they are going to be stored.


## Configuration Syntax

**YoutubeDownloader** supports YAML / JSON configuration formats. **YoutubeDownloader** prefers YAML more than JSON. Below is the snippet of sample configurations in YAML / JSON format.

```
settings:
  process: 2
download:
  mostlyinsane:
    dirname: '../mostlyinsane'
    videos: 
      - 'https://www.youtube.com/watch?v=vcKPjDUc5EQ'
  trippling:
    dirname: 'trippling'
    playlists: 'https://www.youtube.com/watch?list=PLTB0eCoUXEraZe3d7fJRdB-znE5D0cMZ7'
  official-ceogiri:
    dirname: 'official-ceogiri'
    playlists:
    	- 'https://www.youtube.com/watch?list=PLTB0eCoUXEraZe3d7fJRdB-znE5D0cMZ7'
```

```
{
	"settings": {
		"process": 5
	},
	"download": {
		"mostlyinsane": {
			"dirname": "../mostlyinsane",
			"videos": [
				"https://www.youtube.com/watch?v=vcKPjDUc5EQ"
			]

		},
		"trippling": {
			"dirname": "trippling",
			"playlists": "https://www.youtube.com/watch?list=PLTB0eCoUXEraZe3d7fJRdB-znE5D0cMZ7"

		},
		"official-ceogiri": {
			"dirname": "official-ceogiri",
			"playlists": [
				"https://www.youtube.com/watch?list=PLTB0eCoUXEraZe3d7fJRdB-znE5D0cMZ7"
			]

		}
	}
}
```

`settings` defines service level variables. 
- `process` to force **YoutubeDownloader** to use `Asynchronous Python Multiprocessing` and tells how many processes should be deployed to download **videos/playlists** at a time.

`download` defines what **videos/playlists** to download. It tags **dirnames** with **videos/playlists** internally and store the downloaded **videos/playlists** in the respective **directory**.

- `dirname` **relative / absolute directory path** to store videos in.
- `videos` **single / array of youtube videos link** to download.
- `playlists` **single / array of youtube playlists link** to download.


## Install

This is a pure-Python package built for Python 2.6+ and Python 3.0+. To set up:

```
    sudo pip install ytdownloader
```

## Options

```
    ytdownloader --help
```

[reference]: https://github.com/mukultaneja/YoutubeDownloader/blob/master/docs/reference.png "YoutubeDownloader Reference"

- `config` specifies the location for the configuration file to **YoutubeDownloader**. If it omits, **YoutubeDownloader** looks in the current directory for the configuration file.
- `--version` specifies the currect version of **YoutubeDownloader**.
- `--about` about text for **YoutubeDownloader**


## Usage

```
	ytdownloader --version    // latest version of ytdownloader
```
```
	ytdownloader --about      // about text for ytdownloader
```
```
	ytdownloader              // start the ytdownloader and search config file in current directory
```
```
	ytdownloader docs/config.yaml // start the ytdownloader and use docs/config.yaml as config file
```

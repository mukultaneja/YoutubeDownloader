import os
import yaml
import glob
import json
import logging
import subprocess
import multiprocessing

logging.basicConfig(level=logging.DEBUG)
__VERSION__ = '0.1.11'


class YoutubeDownloader(object):
    def __init__(self):
        self.currentdir = os.getcwd()

    def search_config(self):
        logger = logging.getLogger(__name__)
        logger.info(' Looking for configuration...')
        yaml_path = os.path.join(self.currentdir, '*.yaml')
        json_path = os.path.join(self.currentdir, '*.json')
        config_file = glob.glob(yaml_path) or glob.glob(json_path)

        if len(config_file) > 0:
            return os.path.abspath(config_file[0])

        raise FileNotFoundError('Missing YAML / JSON configuration file! ')

    def read_config(self, config_file):
        if config_file.endswith('yaml'):
            with open(config_file) as c:
                return yaml.load(c, yaml.Loader)

        if config_file.endswith('json'):
            with open(config_file) as c:
                return json.load(c)

    def get_items_to_download(self, downloads):
        items_to_download = list()
        if downloads is not None:
            for _, items in downloads.items():
                items_to_download.append([items['dirname'],
                                          items.get('videos', []),
                                          items.get('playlists', [])])

        return items_to_download

    def download_items(self, item_to_download):
        dirname, videos, playlists = item_to_download
        dirname = os.path.abspath(os.path.expanduser(dirname))
        videos = videos if type(videos) is list else [videos]
        playlists = playlists if type(playlists) is list else [playlists]
        items = videos + playlists
        logger = logging.getLogger(__name__)

        if not items:
            logger.info(' {}: Finished downloading! Nothing to download.'.format(dirname))
            return 0

        if not os.path.exists(dirname):
            os.makedirs(dirname)

        os.chdir(dirname)
        items = ' '.join(items)
        logger.info(' Dumping videos into directory {}'.format(dirname))
        subprocess.check_call('youtube-dl ' + items, shell=True)
        logger.info(' Finished {} downloading! {} ready to consume.'.format(dirname, dirname))
        os.chdir(self.currentdir)

        return 0

    def start(self, config_file=None):
        logger = logging.getLogger(__name__)
        config_file = os.path.abspath(config_file) if config_file else self.search_config()
        logger.info(' Found configuration {}'.format(config_file))
        config = self.read_config(config_file)
        processes = config.get('settings').get('process', 1)
        downloads = config.get('download', None)
        items_to_download = self.get_items_to_download(downloads)
        if len(items_to_download) == 0:
            logger.info(' Nothing to download! Finished downloading!')
            return 0

        logger.info(' Starting YoutubeDownloader with {} workers.'.format(processes))
        pool = multiprocessing.Pool(processes)
        results = pool.map_async(self.download_items, items_to_download)
        results.wait()

        return results


if __name__ == '__main__':
    yt = YoutubeDownloader()
    yt.start('../docs/config.json')

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

    def read_config(self, config_file=None):
        logger = logging.getLogger(__name__)
        self.config_file = os.path.abspath(
            config_file) if config_file else self.search_config()
        logger.info(' Found configuration {}'.format(self.config_file))
        if self.config_file.endswith('yaml'):
            with open(self.config_file) as c:
                self.config = yaml.load(c, yaml.Loader)

        if self.config_file.endswith('json'):
            with open(self.config_file) as c:
                self.config = json.load(c)

        self.processes = self.config.get('settings').get('process', 1)
        self.download = self.config.get('download', None)
        logger.info(
            ' Starting YoutubeDownloader with {} workers.'.format(self.processes))

    def prepare_downloads(self):
        inputs = list()
        if self.download is not None:
            for _, value in self.download.items():
                inputs.append([value['dirname'], value.get(
                    'videos', value.get('playlists', None))])

        return inputs

    def download_videos(self, inputs):
        dirname, links = os.path.abspath(inputs[0]), inputs[1]
        logger = logging.getLogger(__name__)
        if links is None:
            logger.info(
                ' {}: Downloading Abort! Nothing to download.'.format(dirname))
            return -1

        if not os.path.exists(dirname):
            os.makedirs(dirname)

        os.chdir(dirname)
        links = ' '.join(links) if type(links) is list else links
        logger.info(' Dumping videos into directory {}'.format(dirname))
        subprocess.check_call('youtube-dl ' + links, shell=True)
        logger.info(
            ' Finished {} downloading! {} ready to consume.'.format(dirname, dirname))
        os.chdir(self.currentdir)

        return 0

    def start_download(self):
        logger = logging.getLogger(__name__)
        self.inputs = self.prepare_downloads()
        if len(self.inputs) == 0:
            logger.info(' Nothing to download! Finished downloading!')
            return 0

        pool = multiprocessing.Pool(self.processes)
        results = pool.map_async(self.download_videos, self.inputs)
        results.wait()

        return results

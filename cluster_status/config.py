from appdirs import AppDirs
import yaml
import os
from argparse import ArgumentParser

CONF_API_ID = "api_id"
CONF_API_HASH = "api_hash"
CONF_BOT_TOKEN = "bot_token"


def get_config_path():
    """Set the config path."""
    return AppDirs("cluster_status").user_config_dir + ".yaml"


def safe_config(config):
    """Safe the config file."""
    with open(get_config_path(), "w") as f:
        yaml.dump(config, f, Dumper=yaml.Dumper)


def read_config():
    """Read the config file."""
    if not os.path.isfile(get_config_path()):
        raise FileNotFoundError("We did not find a config for cluster_status.")

    with open(os.path.join(get_config_path())) as f:
        return yaml.load(f, Loader=yaml.FullLoader)


def delete_config():
    """Delete the config file."""
    print("deleting the configuration.")
    os.remove(get_config_path())


def setup(args):
    """Carry out the configuration."""

    if args.delete:
        delete_config()
        quit()

    if args.config or not os.path.isfile(get_config_path()):
        config = {}
        print("Get you bot token by starting a chat with the BotFather and creating a bot.\n"
              "More info: https://core.telegram.org/bots#6-botfather\n")
        config[CONF_BOT_TOKEN] = str(input("Input a bot token:"))
        print("Get your own api_id and api_hash from https://my.telegram.org, under API Development.\n"
              "More info: https://docs.telethon.dev/en/latest/basic/signing-in.html\n")
        config[CONF_API_ID] = int(input("Input an api id:"))
        config[CONF_API_HASH] = str(input("Input an api hash:"))

        safe_config(config)
        print("\nFinished the configuration.")


class ClusterStatusArgparser(ArgumentParser):
    """Class that deals with arguments for the cluster_status"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_argument(
            "-c",
            "--config",
            action='store_true',
            help="specify if you want to start the config",
        )
        self.add_argument(
            "-d",
            "--delete",
            action='store_true',
            help="specify if you want to remove your config",
        )






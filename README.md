# telegram_simulation_bot
Interact with your computing cluster via telegram to get realtime information on your running jobs.

## Install
Clone this repo and change into its directory. 
```
pip install -e .
```

## Usage:
Change into the directory of your simulation and type:
```
telegram_simulation_bot
```
You will be prompted (only once) to configure `telegram_simulation_bot`.

## Commands:
The following commands in telegram are possible:

* `list` - responds a list of currently running bots 
* `status <name>` - responds the status of `<name>` 
* `error <name>` - responds errors of `<name>`
* `progress <name>` - responds the progress of `<name>`

## Delete:
```
telegram_simulation_bot --delete
pip uninstall telegram_simulation_bot
```


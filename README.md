# cluster_status
Interact with your computing cluster via telegram to get realtime information on your running jobs.


## Install
Clone this repo and change into its directory. 
```
pip install -e .
```

## Usage:
Change into the directory of your simulation and type:
```
mitgcm_cluster_status
```
You will be prompted (only once) to configure `cluster_status`.

## Commands:
The following commands in telegram are possible:

* `list` - responds a list of currently running bots 
* `status <name>` - responds the status of `<name>` 
* `error <name>` - responds errors of `<name>`
* `progress <name>` - responds the progress of `<name>`

## Delete:
```
mitgcm_clustr_status --delete
pip uninstall cluster_status
```


Goagent IP Updater Version History
======================================
## version 0.1
|    |   |
| --------   | :----  |
| Update on | 2015-04-15 |
| Description | initial setup |

## version 0.1.1
|    |   |
| --------   | :----  |
| Update on | 2015-04-15 |
| Description | fix some link bugs in README.md |

## version 0.1.2
|    |   |
| --------   | :----  |
| Update on | 2015-04-16 |
| Description | 1.restuct the module hierarchy |
|          | 2.unify the prompt to ZH-CN character set |
|          | 3.add a config step to set the parallel threads amount |

## version 0.1.3
|    |   |
| --------   | :----  |
| Update on | 2015-04-19 |
| Description | 1.add the goagent auto-start/auto-restart function(if an earlier goagent process is running, it will be killed automatically), so that goagent don't have to be started by hand. The funtion only works on Windows right now, Linux to be developed. |
|          | 2.add validation to the parallel connection settings, restrict connection number in the range of 1 to 64 |

## version 0.1.4
|    |   |
| --------   | :----  |
| Update on | 2015-04-24 |
| Description | 1.update default ip list. |
|          | 2.add server certificate verification to ensure the usability of the ip, a certificate file is provided and required to make the script functional. |
|          | 3.the script will stop as soon as more than 20 reachable IPs are found. |
|          | 4.fix a bug that when no reachable IPs are found, the iplist field in goagent ini file would be set to empty. |
|          | 5.changed the prompt info. |
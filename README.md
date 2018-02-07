# Locust

[![Build Status](https://secure.travis-ci.org/locustio/locust.png)](http://travis-ci.org/locustio/locust) 
[![Gitter Chat](https://badges.gitter.im/locustio/locust.png)](https://gitter.im/locustio/locust) 

## Links

* Website: <a href="http://locust.io">locust.io</a>
* Documentation: <a href="http://docs.locust.io">docs.locust.io</a>

## Description

This is a fork from <a href="https://github.com/locustio/locust">this official git</a> (Locust 0.7.5)

## Addups
* **Distributed testing compactibility in the CLI mode**

  Master - Slave spawning can be done in CLI mode also. But the number of slaves is predefined unlike WebUI mode.
  
* **Timely Test Response stats available in CLI mode also (which can be used for plaotting)**

  In case of the WebUI, we get Locust data in JSON format visiting [http://localhost:8089/stats/requests] while test is on run. Same way, the WebUI also will generate the data is the same similar format. (Futher extended for plotting and others things while in CLI also)

"""
(ii) Write a program that reads a json file , performs following edits and store json back to the same file. update following fields -

A. Change firewall - protocol - from tcp to udp
B. Change 3rd vnics- portgroup name to EXT_VLAN_201b
C. Change ospf- enabled = false to true
D. Update holddowntimer = holddowntimer +keepalivetimer

"""

import collections
import json

with open("sample.json") as json_file:
    my_data = json.load(json_file)

    my_data["featureConfigs"]["features"][2]["firewallRules"]["firewallRules"][0]["application"]["service"][0][
        "protocol"] = "udp"

    my_data["vnics"]["vnics"][2]["portgroupName"] = "EXT_VLAN_201b"

    my_data["featureConfigs"]["features"][5]["ospf"]["enabled"] = "True"

    for i in range(0, 3):
        h_timer = my_data["featureConfigs"]["features"][5]["bgp"]["bgpNeighbours"]["bgpNeighbours"][i][
            "holdDownTimer"]
        k_alive = my_data["featureConfigs"]["features"][5]["bgp"]["bgpNeighbours"]["bgpNeighbours"][
            i]["keepAliveTimer"]

        h_timer += k_alive
        my_data["featureConfigs"]["features"][5]["bgp"]["bgpNeighbours"]["bgpNeighbours"][i][
            "holdDownTimer"] = h_timer

with open("sample.json", "w") as json_d:
    json_d.write(json.dumps(my_data))
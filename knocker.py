# Harom Ramos - 2018

import nmap
ns = nmap.PortScanner()

op = 0
cp = 0
ports = [1,5,7,9,11,13,17,18,19,20,21,22,23,25,37,39,42,43,49,50,53,63,67,68,69,70,71,72,73,73,79,80,88,95,101,102,105,107,109,110,111,113,115,117,119,123,137,138,139
,143,161,162,163,164,174,177,178,179,191,194,199,201,202,204,206,209,210,213,220,245,347,363,369,370,372,389,427,434,435,443,444,445,464,468,487,488,496,500,535,538
,546,547,554,563,565,587,610,611,612,631,636,674,694,749,750,751,752,754,760,765,767,873,992,993,994,995]

print(ns.nmap_version())
print('##############################################################')
print('')
hosts = input("hosts: (Enter=Todos)")
args = input("Argumentos: ")
if not hosts:
    hosts = ' '.join(ns.all_hosts())
# host up ?
ns.scan(str(hosts), '-sn')
print("----------------------------------------------------------")
# print('Host : %s (%s)' % (hosts, ns[hosts].hostname()))
# print('Estado : %s' % ns[hosts].state())
# print(ns[hosts].all_protocols())
for i in ports:
    index_val = ports.index(i)
    ns.scan(str(hosts), str(i), '-v', str(args))
    for proto in ns[hosts].all_protocols():
        lport = ns[hosts][proto].keys()
        for port in lport:
            if ns[hosts][proto][port]['state'] != 'closed':
                op = op + 1
                print('puerto : %s\testado : %s' % (port, ns[hosts][proto][port]['state']))
                print("----------------------------------------------------------")
            else:
                cp = cp + 1
print('Open/Filtered: ' + str(op))
print('Closed: ' + str(cp))

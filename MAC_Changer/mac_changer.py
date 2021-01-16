import subprocess
import optparse
import re


def get_arguments():
    '''Take arguments from TERMINAL to use as options'''

    parser = optparse.OptionParser()
    parser.add_option('-i', '--interface', dest='interface', help='Simple script program to change your MAC address.'
                                                                  + 'Type on TERMINAL "ifconfig" to know what interface you want to use.')
    parser.add_option('-m', '--mac', dest='new_mac', help='Insert the desired MAC address')
    options, _ = parser.parse_args()

    if not options.interface:
        parser.error('Please specify an interface, use --help if needed')

    elif not options.new_mac:
        parser.error('Please specify a MAC address, use --help if needed')

    return options


def change_mac(interface, new_mac):
    print(f'Changing {interface} MAC address to {new_mac}')

    subprocess.call(['ifconfig', interface, 'down'])
    subprocess.call(['ifconfig', interface, 'hw', 'ether', new_mac])
    subprocess.call(['ifconfig', interface, 'up'])


def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(['ifconfig', options.interface])
    result = re.search(r'(([a-e]|[0-9]){2}(:)){5}([a-e]|[0-9]){2}', str(ifconfig_result))

    if result:

        return (result.group(0))

    else:

        print('Something go wrong... Try again!')


options = get_arguments()

current_mac = get_current_mac(options.interface)
print(f'Actual MAC is {str(current_mac)}. Changing to the desired one, just wait...')

change_mac(options.interface, options.new_mac)

current_mac = get_current_mac(options.interface)

if current_mac == options.new_mac:

    print(f'MAC address was successfully changed to {current_mac}!')

else:

    print('Something go wrong, MAC address did not change')

import RouterABCStack as stack
import configparser

if __name__ == '__main__':

    iptable = configparser.ConfigParser()
    iptable.read('iptable.ini')
    config = configparser.ConfigParser()
    config.read('config.ini')

    if not iptable.has_option('DEFAULT', '0'):
        iptable['DEFAULT']['0'] = config['DEFAULT']['mac'].replace("'", "")
    
    abc = stack.RouterABCStack([stack.PhysicalLayer, stack.RouterDatalinkLayer])
    

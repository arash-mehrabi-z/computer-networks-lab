import requests

if __name__ == "__main__":
    session = requests.session()
    session.proxies = {}
    session.proxies['http'] = 'socks5h://localhost:9050'
    session.proxies['https'] = 'socks5h://localhost:9050'

    r = session.get('PUT_YOUR_ONION_ADDRESS_HERE')
    print(r.content)
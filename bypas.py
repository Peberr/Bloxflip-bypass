import cloudscraper
import requests

scraper = cloudscraper.create_scraper()

def bypass():
    bypass = scraper.get("https://rest-bf.blox.land/games/crash")

    print("Testing bypass!")

    if bypass.status_code == 200:
        print("bypassed!", bypass.status_code)

    elif bypass.status_code == 404:
        print("Not bypassed!", bypass.status_code)

def normal():
    print("Testing Non Bypass")

    r = requests.get("https://bloxflip.com")

    if r.status_code == 200:
        print("Bypassed!", r.status_code)
        
    elif r.status_code == 404:
        print("Failed get trough ", r.status_code)

    else:
        print("Failed to bypass:", r.status_code)

def main():
    print("Methods:\n1. Normal\n2. Bypass")

    methods = input("->")

    if methods == "1":
        normal()

    elif methods == "2":
        bypass()

if __name__ == "__main__":
    main()

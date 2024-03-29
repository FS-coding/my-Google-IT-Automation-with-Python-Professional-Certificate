import requests
#import json
import os


def read_reviews(path, ip_address):

    files = os.listdir(path)

    for file in files:
        # print(file)

        with open(path + file) as f:
            lines = [l.strip() for l in f.readlines()]
            # must drop "lbs" from weight
            f_data = {"name": lines[0], "weight": str(lines[1].strip(
                " lbs")), "desciption": lines[2], "image_name": lines[3] + ".jpeg"}

            try:
                response = requests.post(ip_address, data=f_data)
                print(response.raise_for_status())

            except Exception as e:
                print("An error occurred: {}").format(e)


def main():
    path = "~/supplier-data/descriptions/"
    ip_address = "http://<corpweb-external-IP>/fruits/"
    read_reviews(path, ip_address)


if __name__ == '__main__':
    main()

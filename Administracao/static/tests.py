from geopy.distance import distance, great_circle
from flask import request


def main():
    # request.args.get
    # position = '-19.8593807,-43.9189328'.split(',')
    # print(position.index())
    # print(position.index())
    casa_vida = (-19.8593807, -43.9189328)
    casa_creu = (-19.8596886, -43.918865)
    print(great_circle(casa_creu, casa_vida).m*1.15)


if __name__ == '__main__':
    main()


json = {
    "latitude1": -19.7808846, "latitude2": -20.0222052, "longitude1": -43.971382, "longitude2": -44.0275001
}

from django.http import HttpResponse
from django.template import loader
import ibm_boto3
from ibm_botocore.client import Config, ClientError
import json
import os
from os.path import exists

def get_fire_coords():
    fire_coords = []
    coords_file_name = "map/resources/fires.txt"

    # Uncomment when we have access to an IBM COS S3
    # coords_file = get_item(s3_bucket_name, coords_file_name)
    if exists(coords_file_name):
        with open(coords_file_name) as f:
            contents = f.readlines()
            for i in contents:
                coords_pair = i.split()
                # First part of the pair is lat and if it's bellow 30 - it might be a desert
                # in which case we don't want it (for now)
                # if float(coords_pair[0]) > 30.0:
                fire_coords.append(coords_pair)

    return fire_coords
    # IBM S3 example code
    # print("Retrieving item from bucket: {0}, key: {1}".format(bucket_name, item_name))
    # try:
    #     file = cos.Object(bucket_name, item_name).get()
    #     print("File Contents: {0}".format(file["Body"].read()))
    #     return file["Body"].read()
    # except ClientError as be:
    #     print("CLIENT ERROR: {0}\n".format(be))
    # except Exception as e:
    #     print("Unable to retrieve file contents: {0}".format(e))

def test_get_fire_coords_from_pi():
    os.system('rm /Users/mount40/Projects/sigma/sigma/map/resources/fires.txt')
    os.system('sshpass -p "toor" scp root@10.0.0.1:/work/fires.txt /Users/mount40/Projects/sigma/sigma/map/resources')

def firemap(request):
    # test_get_fire_coords_from_pi()
    fire_coords = get_fire_coords()
    template = loader.get_template('map/map.html')

    context = {
        'fire_coords': fire_coords,
    }
    return HttpResponse(template.render(context, request))

def home(request):
    template = loader.get_template('map/home.html')
    context = {}
    return HttpResponse(template.render(context, request))

def team(request):
    template = loader.get_template('map/team.html')
    context = {}
    return HttpResponse(template.render(context, request))

def fire_coords(request):
    fire_coords = get_fire_coords()
    return HttpResponse(json.dumps(fire_coords))
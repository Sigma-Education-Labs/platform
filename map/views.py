from django.http import HttpResponse
from django.template import loader
import ibm_boto3
from ibm_botocore.client import Config, ClientError

def get_item(bucket_name, item_name):
    print("Retrieving item from bucket: {0}, key: {1}".format(bucket_name, item_name))
    try:
        file = cos.Object(bucket_name, item_name).get()
        print("File Contents: {0}".format(file["Body"].read()))
        return file["Body"].read()
    except ClientError as be:
        print("CLIENT ERROR: {0}\n".format(be))
    except Exception as e:
        print("Unable to retrieve file contents: {0}".format(e))


def index(request):
    fire_coords = []
    s3_bucket_name = ""
    coords_file_name = "map/coords-01-09-2022.txt"

    # Uncomment when we have access to an IBM COS S3
    # coords_file = get_item(s3_bucket_name, coords_file_name)
    
    with open(coords_file_name) as f:
        contents = f.readlines()
        for i in contents:
            coords_pair = i.split()
            # First part of the pair is lat and if it's bellow 30 - it might be a desert
            # in which case we don't want it (for now)
            if float(coords_pair[0]) > 30.0:
                fire_coords.append(coords_pair)

    template = loader.get_template('map/map.html')


    context = {
        'fire_coords': fire_coords,
    }
    return HttpResponse(template.render(context, request))

import sys
import base64
import hashlib
from json import dumps
from base64 import b64encode
import oslearn

def convert_file_to_base64():
    """
    Converting file to base64 encoding
    For example - Used as for 'payloadData' value when creating new service based on CSAR file
    :return: base64_data
    """
    print(" =============================================================================")
    print("Command to use = python csar_operations.py <Csar File Path> <Csar File Name>")
    print(" =============================================================================\n")

    csar_location = sys.argv[1]
    origin_file = sys.argv[2]
    path = oslearn.path.join(csar_location, origin_file)
    try:
        with open(path, "rb") as image_file:
            base64_data = base64.b64encode(image_file.read())

        base64_string = base64_data.decode()
        json_body = {'payloadData': base64_string, 'payloadName': str(origin_file)}
        json_body_updated = dumps(json_body)
        with open(csar_location+'csar_base64.txt','w') as f:
            f.write(json_body_updated)
            print(sys.argv[2]," file is encoded in base64")
            print("Refer ",csar_location+'csar_base64.txt', " to see the base64encoded csar \n")
        content_MD5_header(csar_location,json_body_updated)
    except Exception as e:
        print("I am in covert_file_to_base64")
        print ("exception occurred: " + str(e))


def content_MD5_header(csar_location,json_body_updated):
        """
        Calculate checksum for header 'Content-MD5' based on json body
        :param json_body_updated
        :return: 'md5' checksum for 'Content-MD5' header
        """
        json_body = json_body_updated.encode('utf-8')
        try:
            checksum = hashlib.md5(json_body).hexdigest()
            checksum = checksum.encode('utf-8')
            checksum_base64 = base64.b64encode(checksum)
            checksum_base64 = checksum_base64.decode()

            with open(csar_location+'md5_checksum.txt', 'w') as f:
                f.write(checksum_base64)
                print("Refer ", csar_location + 'md5_checksum.txt', " to see the header \n")

        except Exception as e:
            print("exception occurred: " + str(e))



if __name__ == '__main__':
    convert_file_to_base64()

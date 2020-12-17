import boto3
import zipfile
import io
from io import BytesIO
import mimetypes
def lambda_handler(event,context):
    s3 = boto3.resource('s3')

    portfolio_bucket = s3.Bucket('portfolio.ithandymanny.net')

    for obj in portfolio_bucket.objects.all():
            print(obj.key)
            
    build_bucket = s3.Bucket('portfoliobuild.ithandymanny.net')

    build_bucket.download_file('buildportfolio', '/home/fitz2020/Downloads/buildportfolio')



    buildportfolio = BytesIO()

    build_bucket.download_fileobj('buildportfolio',buildportfolio)

            
    with zipfile.ZipFile(buildportfolio) as myzip:
        for nm in myzip.namelist():
            obj= myzip.open(nm)
            portfolio_bucket.upload_fileobj(obj, nm,
            ExtraArgs={'ContentType': mimetypes.guess_type(nm) [0]})
            portfolio_bucket.Object(nm).Acl().put(ACL='public-read')
    print("Job Well Done")
    return ("Hello from Manny's Lambda")

import os
class S3Sync:
    """
    First func syncs and stores all the artifacts to S3 bucket
    Second func syncs and stores all the artifacts from S3 bucket to project
    """

    def sync_folder_to_s3(self,folder,aws_bucket_url):
        command = f"aws s3 sync {folder} {aws_bucket_url}"
        os.system(command)

    def sync_folder_from_s3(self,folder,aws_bucket_url):
        command = f"aws s3 sync {aws_bucket_url} {folder}"
        os.system(command)

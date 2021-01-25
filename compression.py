import tarfile
from tqdm import tqdm

class Compression:

    def compress(self,tar_file, members):
        """
        Adds files (`members`) to a tar_file and compress it
        """
        # open file for gzip compressed writing
        tar = tarfile.open(tar_file, mode="w:gz")
        # with progress bar
        # set the progress bar
        progress = tqdm(members)
        for member in progress:
            # add file/folder/link to the tar file (compress)
            tar.add(member)
            # set the progress description of the progress bar
            progress.set_description(f"Compressing {member}")
        # close the file
        tar.close()

    def decompress(self,tar_file, path, members=None):
        
        tar = tarfile.open(tar_file, mode="r:gz")
        if members is None:
            members = tar.getmembers()
        # with progress bar
        # set the progress bar
        progress = tqdm(members)
        for member in progress:
            tar.extract(member, path=path)
            # set the progress description of the progress bar
            progress.set_description(f"Extracting {member.name}")
        # or use this
        # tar.extractall(members=members, path=path)
        # close the file
        tar.close()
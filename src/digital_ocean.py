import digitalocean
from dotenv import load_dotenv
import os

class DigitalOceanManager:
    def __init__(self):
        load_dotenv()
        self.token = os.getenv("DIGITALOCEAN_TOKEN")
        self.manager = digitalocean.Manager(token=self.token)
    
    def list_droplets(self):
        return self.manager.get_all_droplets()
    
    def get_droplet(self, droplet_id):
        return self.manager.get_droplet(droplet_id)
    
    def create_droplet(self, name, region, size, image):
        droplet = digitalocean.Droplet(
            token=self.token,
            name=name,
            region=region,
            size_slug=size,
            image=image
        )
        droplet.create()
        return droplet
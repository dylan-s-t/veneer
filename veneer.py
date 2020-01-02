class Art:
  def __init__(self, artist, title, medium, year, owner):
    self.artist = artist
    self.title = title
    self.medium = medium
    self.year = year
    self.owner = owner
    
  def __repr__(self):
    return '{artist}. "{title}". {year}, {medium}. {owner}, {location}.'.format(artist = self.artist, title = self.title, year = self.year, medium = self.medium, owner = self.owner.name, location = self.owner.location)


class Marketplace:
  def __init__(self):
    self.listings = []
    
  def add_listing(self, new_listing):
    self.listings.append(new_listing)
    
  def remove_listing(self, to_remove):
    self.listings.remove(to_remove)
    
  def show_listings(self):
    for listing in self.listings:
      print(listing)
      
veneer = Marketplace()

class Client:
  def __init__(self, name, location, is_museum):
    self.name = name
    self.location = location
    self.is_museum = is_museum
    self.wishlist = []
    self.wallet = 10000000
    
  def sell_artwork(self, artwork, price):
    if artwork.owner == self:
      new_listing = Listing(artwork, price, self.name)
      veneer.add_listing(new_listing)
      
  def buy_artwork(self, artwork):
    if artwork.owner != self:
      for listing in veneer.listings:
        if listing.art == artwork:
          art_listing = artwork
          art_listing.owner = self
          veneer.remove_listing(listing)
          print(self.name + " has " + str(self.wallet)+ " dollars")
          self.wallet -= listing.price
          print(self.name + " has " + str(self.wallet)+ " dollars after buying " + art_listing.title)
          
  def add_wishlist(self, artwork):
    if artwork.owner != self:
      self.wishlist.append(artwork)
    else:
      print("you already own this!")
      
class Listing:
  def __init__(self, art, price, seller):
    self.art = art
    self.price = price
    self.seller = seller
  
  def __repr__(self):
    return '{title} costs {price}'.format(title = self.art.title, price = self.price)
          
edytta = Client("Edytta Halpirt", "Private Collection", False)   

moma = Client("The MOMA", "New York", True)

girl_with_mandolin = Art("Picasso, Pablo", "Girl with a Mandolin (Fanny Tellier)", "1910", "oil on canvas", edytta)

print(girl_with_mandolin)
    
edytta.sell_artwork(girl_with_mandolin, 6000000)
    
veneer.show_listings()

moma.buy_artwork(girl_with_mandolin)

print(girl_with_mandolin)
veneer.show_listings()

moma.add_wishlist(girl_with_mandolin)

